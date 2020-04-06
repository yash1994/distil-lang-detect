# coding: utf-8
from __future__ import unicode_literals

import pytest

from distillangdetect.detector import Detector
from distillangdetect.config import LangIDToISO3Codes, LangISO3CodesToCommonName
from data.devtestsets import DEVTEST_LONG, DEVTEST_MEDIUM, DEVTEST_SHORT, DEVTEST_TINY

dct = Detector(device="cpu")
lang_id_to_iso3_codes = LangIDToISO3Codes()
lang_iso3_codes_to_common_name = LangISO3CodesToCommonName()


@pytest.mark.parametrize("text", ["I love retro computing."])
def test_detect(text):
    det = dct.detect(text)
    assert det == "English"


@pytest.mark.parametrize("devtest_long", [DEVTEST_LONG])
def test_detect_for_devtest_long_sentences(devtest_long):
    tp_count = 0
    for k, v in devtest_long.items():
        det = dct.detect(v)
        class_iso3_code = lang_id_to_iso3_codes.get_language_iso3code(k)
        class_common_name = lang_iso3_codes_to_common_name.get_common_name(
            class_iso3_code
        )
        if det == class_common_name:
            tp_count += 1
    assert tp_count == 59


@pytest.mark.parametrize("devtest_medium", [DEVTEST_MEDIUM])
def test_detect_for_devtest_medium_sentences(devtest_medium):
    tp_count = 0
    for k, v in devtest_medium.items():
        det = dct.detect(v)
        class_iso3_code = lang_id_to_iso3_codes.get_language_iso3code(k)
        class_common_name = lang_iso3_codes_to_common_name.get_common_name(
            class_iso3_code
        )
        if det == class_common_name:
            tp_count += 1
    assert tp_count == 55


@pytest.mark.parametrize("devtest_short", [DEVTEST_SHORT])
def test_detect_for_devtest_short_sentences(devtest_short):
    tp_count = 0
    for k, v in devtest_short.items():
        det = dct.detect(v)
        class_iso3_code = lang_id_to_iso3_codes.get_language_iso3code(k)
        class_common_name = lang_iso3_codes_to_common_name.get_common_name(
            class_iso3_code
        )
        if det == class_common_name:
            tp_count += 1
    assert tp_count == 65


@pytest.mark.parametrize("devtest_tiny", [DEVTEST_TINY])
def test_detect_for_devtest_tiny_sentences(devtest_tiny):
    tp_count = 0
    for k, v in devtest_tiny.items():
        det = dct.detect(v)
        class_iso3_code = lang_id_to_iso3_codes.get_language_iso3code(k)
        class_common_name = lang_iso3_codes_to_common_name.get_common_name(
            class_iso3_code
        )
        if det == class_common_name:
            tp_count += 1
    assert tp_count == 67
