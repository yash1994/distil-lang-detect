# coding: utf-8
from __future__ import unicode_literals

import os
import torch
import transformers
import numpy as np
from torch import nn

from distillangdetect import utils
from distillangdetect import config
from distillangdetect.cleaner import Cleaner


class Detector:
    def __init__(self, model="distillangdetect_91_langs_0.0.1", device=None):

        if not device:
            if torch.cuda.is_available():
                self.device = torch.device("cuda")
                print("There are %d GPUs available." % torch.cuda.device_count())
                print("GPU will be used: ", torch.cuda.get_device_name(0))
            else:
                print("No GPU available, using the CPU instead.")
                self.device = torch.device("cpu")
        else:
            if device == "cuda" and torch.cuda.is_available():
                self.device = torch.device("cuda")
            else:
                self.device = torch.device("cpu")

        self.max_sequence_length = 64

        self.model_name = model
        self.text_cleaner = Cleaner()
        self.model_download_config = config.ModelDownloadConfig()
        self.language_map = config.LanguageMap()
        self.language_id_to_iso3_codes = config.LangIDToISO3Codes()
        self.language_iso3_codes_to_common_name = config.LangISO3CodesToCommonName()

        print("Loading DistilBert model and tokenizer...")

        self.model, self.tokenizer = self.load_model_and_tokenizer()
        self.model.to(self.device)
        self.model.eval()

        print("Model loading complete.")

    def load_model_and_tokenizer(self):
        if self.model_download_config.check_model_presence(self.model_name):
            (
                integrity,
                model_path,
            ) = self.model_download_config.get_model_path_and_varify_integrity(
                self.model_name
            )
            if not integrity:
                print(
                    "Language detection model not present, download it using: {}".format(
                        "distillangdetect download -m distillangdetect_91_langs_0.0.1"
                    )
                )
                return None, None
            try:
                model = transformers.DistilBertForSequenceClassification.from_pretrained(
                    model_path
                )
                tokenizer = transformers.DistilBertTokenizer.from_pretrained(model_path)
                return model, tokenizer
            except Exception as e:
                print("Error in loading model and tokenizer: ", str(e))
        else:
            print(
                "Language detection model specified is not avilable try one from {}".format(
                    list(self.model_download_config.get_model_list())
                )
            )

    def model_inference(self, text):

        tokenized_text = self.tokenizer.encode_plus(
            text=text,
            add_special_tokens=True,
            max_length=self.max_sequence_length,
            pad_to_max_length=True,
            return_attention_mask=True,
            return_tensors="pt",
        )

        input_ids = tokenized_text["input_ids"]
        attention_mask = tokenized_text["attention_mask"]

        with torch.no_grad():
            input_ids = input_ids.to(self.device)
            attention_mask = attention_mask.to(self.device)
            output = self.model(input_ids, attention_mask=attention_mask)

        logits = output[0].detach().cpu().numpy()
        class_idx = np.argmax(logits, axis=1)[0]
        return class_idx

    def detect(self, text):
        text = self.text_cleaner.clean_text(text)
        class_idx = self.model_inference(text)
        class_id = self.language_map.get_language_identifier(class_idx)
        class_iso3_code = self.language_id_to_iso3_codes.get_language_iso3code(class_id)
        class_common_name = self.language_iso3_codes_to_common_name.get_common_name(
            class_iso3_code
        )
        return class_common_name
