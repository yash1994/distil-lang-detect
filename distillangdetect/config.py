# coding: utf-8
from __future__ import unicode_literals

import os

class Configs(object):

    def __init__(self):
        self.model_name = "distilbert-base-multilingual-cased"
        self.tokenizer_name = "distilbert-base-multilingual-cased"
        self.n_classes = 91
        self.pre_trained_model_path = "/tmp/distil_detect_model/"
        self.storage_link = ""


class LangISO3CodesToCommonName:

    def __init__(self):
        self.common_name_map = {
            'icr': 'Islander Creole English', 'new': 'Newari', 'pms': 'Piemontese',
            'fin': 'Finnish', 'tgl': 'Tagalog', 'tel': 'Telugu', 'afr': 'Afrikaans',
            'rus': 'Russian', 'arz': 'Egyptian Arabic', 'lit': 'Lithuanian',
            'swa': 'Swahili (macrolanguage)', 'kat': 'Georgian', 'ben': 'Bengali',
            'msa': 'Malay (macrolanguage)', 'spa': 'Spanish', 'bos': 'Bosnian',
            'lat': 'Latin', 'aze': 'Azerbaijani', 'ara': 'Arabic', 'mya': 'Burmese',
            'cym': 'Welsh', 'vie': 'Vietnamese', 'pan': 'Punjabi', 'ido': 'Ido',
            'bre': 'Breton', 'hat': 'Haitian Creole', 'ell': 'Modern Greek (1453-)',
            'hin': 'Hindi', 'kan': 'Kannada', 'ita': 'Italian', 'tha': 'Thai',
            'tat': 'Tatar', 'bul': 'Bulgarian', 'che': 'Chechen', 'jvn': 'Caribbean Javanese',
            'eng': 'English', 'als': 'Tosk Albanian', 'ukr': 'Ukrainian',
            'dan': 'Danish', 'ron': 'Romanian', 'slk': 'Slovak', 'guj': 'Gujarati',
            'heb': 'Hebrew', 'kor': 'Korean', 'hun': 'Hungarian', 'nld': 'Flemish',
            'scn': 'Sicilian', 'sqi': 'Albanian', 'urd': 'Urdu', 'ast': 'Leonese',
            'hrv': 'Croatian', 'lad': 'Ladino', 'cat': 'Valencian', 'glg': 'Galician',
            'mlg': 'Malagasy', 'ind': 'Indonesian', 'jav': 'Javanese', 'swe': 'Swedish',
            'oci': 'Occitan (post 1500)', 'srp': 'Serbian', 'ces': 'Czech', 'nds': 'Low Saxon',
            'eus': 'Basque', 'mon': 'Mongolian', 'bak': 'Bashkir', 'bel': 'Belarusian',
            'yor': 'Yoruba', 'ota': 'Ottoman Turkish (1500-1928)', 'hyw': 'Western Armenian',
            'isl': 'Icelandic', 'hbo': 'Ancient Hebrew', 'ltz': 'Luxembourgish',
            'acf': 'Saint Lucian Creole French', 'bar': 'Bavarian', 'azb': 'South Azerbaijani',
            'fra': 'French', 'tur': 'Turkish', 'hwc': "Hawai'i Pidgin", 'jpn': 'Japanese',
            'pol': 'Polish', 'est': 'Estonian', 'pdc': 'Pennsylvania German', 'mkd': 'Macedonian',
            'mal': 'Malayalam', 'crh': 'Crimean Turkish', 'sco': 'Scots', 'mar': 'Marathi',
            'slv': 'Slovenian'}

    def get_common_name(self, iso3_code):
        return self.common_name_map[iso3_code]


class LangIDToISO3Codes(object):

    def __init__(self):
        self.lang_code_map = {
            "icr_CO": "icr", "new_NP": "new", "pms_IT": "pms", "fi_FI": "fin",
            "tl_PH": "tgl", "tel_IN": "tel", "af_ZA": "afr", "ru_RU": "rus",
            "arz_EG": "arz", "lt_LT": "lit", "sw_KE": "swa", "ka_GE": "kat",
            "ben_BD": "ben", "zlm_ID": "msa", "es_ES": "spa", "bs_BA": "bos",
            "la_XX": "lat", "az_AZ": "aze", "ar_XX": "ara", "my_MM": "mya",
            "cy_GB": "cym", "vi_VN": "vie", "pan_IN": "pan", "io_XX": "ido",
            "br_FR": "bre", "ht_HT": "hat", "el_GR": "ell", "hi_IN": "hin",
            "kn_IN": "kan", "it_IT": "ita", "th_TH": "tha", "tat_SU": "tat",
            "bg_BG": "bul", "ce_RU": "che", "jvn_GF": "jvn", "en_UK": "eng",
            "als_AL": "als", "uk_UA": "ukr", "da_DK": "dan", "ro_RO": "ron",
            "sk_SK": "slk", "guj_IN": "guj", "he_IL": "heb", "ko_KR": "kor",
            "hu_HU": "hun", "sw_TZ": "swa", "nl_NL": "nld", "scn_IT": "scn",
            "alb_AL": "sqi", "ur_PK": "urd", "ast_PT": "ast", "hr_HR": "hrv",
            "lad_EU": "lad", "urd_IN": "urd", "ca_ES": "cat", "gl_ES": "glg",
            "mg_MG": "mlg", "ind_ID": "ind", "jv_ID": "jav", "sv_SE": "swe",
            "oc_FR": "oci", "sr_SR": "srp", "cs_CZ": "ces", "nds_NL": "nds",
            "eu_ES": "eus", "mn_MN": "mon", "ba_RU": "bak", "bel_BY": "bel",
            "yo_NG": "yor", "ota_XX": "ota", "hy_AM": "hyw", "is_IS": "isl",
            "hbo_IL": "hbo", "lb_LU": "ltz", "acf_DM": "acf", "bar_DE": "bar",
            "azb_IR": "azb", "fr_FR": "fra", "en_GB": "eng", "tr_TR": "tur",
            "hwc_US": "hwc", "ja_JP": "jpn", "pl_PL": "pol", "et_EE": "est",
            "pdc_US": "pdc", "mk_MK": "mkd", "ml_IN": "mal", "crh_AF": "crh",
            "sco_GB": "sco", "mr_IN": "mar", "sl_SL": "slv"}

    def get_language_iso3code(self, language_id):
        return self.lang_code_map[language_id]


class LanguageMap:

    def __init__(self):
        self.language_map = {
            0: "icr_CO", 1: "new_NP", 2: "pms_IT", 3: "fi_FI", 4: "tl_PH",
            5: "tel_IN", 6: "af_ZA", 7: "ru_RU", 8: "arz_EG", 9: "lt_LT",
            15: "sw_KE", 16: "ka_GE", 17: "ben_BD", 18: "zlm_ID", 19: "es_ES",
            20: "bs_BA", 21: "la_XX", 22: "az_AZ", 23: "ar_XX", 24: "my_MM",
            25: "cy_GB", 26: "vi_VN", 27: "pan_IN", 28: "io_XX", 29: "br_FR",
            30: "ht_HT", 31: "el_GR", 32: "hi_IN", 33: "kn_IN", 34: "it_IT",
            35: "th_TH", 36: "tat_SU", 37: "bg_BG", 38: "ce_RU", 39: "jvn_GF",
            40: "en_UK", 41: "als_AL", 42: "uk_UA", 43: "da_DK", 44: "ro_RO",
            45: "sk_SK", 46: "guj_IN", 47: "he_IL", 48: "ko_KR", 49: "hu_HU",
            50: "sw_TZ", 51: "nl_NL", 52: "scn_IT", 53: "alb_AL", 54: "ur_PK",
            55: "ast_PT", 56: "hr_HR", 57: "lad_EU", 58: "urd_IN", 59: "ca_ES",
            60: "gl_ES", 61: "mg_MG", 62: "ind_ID", 63: "jv_ID", 64: "sv_SE",
            65: "oc_FR", 66: "sr_SR", 67: "cs_CZ", 68: "nds_NL", 69: "eu_ES",
            70: "mn_MN", 71: "ba_RU", 72: "bel_BY", 73: "yo_NG", 74: "ota_XX",
            75: "hy_AM", 76: "is_IS", 77: "sl_SL", 78: "hbo_IL", 79: "lb_LU",
            80: "acf_DM", 81: "bar_DE", 82: "azb_IR", 83: "fr_FR", 84: "en_GB",
            85: "tr_TR", 86: "hwc_US", 87: "ja_JP", 88: "pl_PL", 89: "et_EE",
            90: "pdc_US", 91: "mk_MK", 92: "ml_IN", 93: "crh_AF", 94: "sco_GB",
            95: "mr_IN"}

    def get_language_identifier(self, idx):
        return self.language_map[idx]

class ModelDownloadConfig:
    def __init__(self):
        
        self.torch_models_cache_dir = os.path.join(os.environ["HOME"], ".cache/torch")
        self.distillangdetect_model_parent = os.path.join(self.torch_models_cache_dir, "distillangdetect_models")
        
        self.model_files_req = set([
            "class_map.json",
            "config.json",
            "pytorch_model.bin",
            "special_tokens_map.json",
            "tokenizer_config.json",
            "vocab.txt"])
        
        self.link_map = {
            "distillangdetect_91_langs_0.0.1": "https://www.dropbox.com/s/y9ejzqkyuizcpk5/distillangdetect_91_langs_0.0.1.zip?dl=0"
        }
    
    def check_model_presence(self, model_name):
        return True if model_name in self.link_map else False
    
    def get_model_link(self, model_name):
        return self.link_map[model_name]
    
    def get_model_list(self):
        return self.link_map.keys()
    
    def get_model_path(self, model_name):
        return os.path.join(self.distillangdetect_model_parent, model_name)
    
    def get_model_path_and_varify_integrity(self, model_name):
        model_path = os.path.join(self.distillangdetect_model_parent, model_name)
        if os.path.exists(model_path):
            if set([i for i in os.listdir(model_path)]) == self.model_files_req:
                return True, model_path
            else:
                return False, model_path
        else:
            return False, model_path    