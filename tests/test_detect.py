# coding: utf-8
from __future__ import unicode_literals

import pytest

from distillangdetect.detector import Detector

dct = Detector(device="cpu")

@pytest.mark.parametrize("text", ["I love retro computing."])
def test_detect(text):
    det = dct.detect(text)
    assert det == "English"