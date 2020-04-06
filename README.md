# <img src="https://i.imgur.com/ALMguVt.png" width="64px" height="64px"/> Distil-Lang-Detect

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/) [![Build Status](https://travis-ci.org/yash1994/distil-lang-detect.svg?branch=master)](https://travis-ci.org/yash1994/distil-lang-detect)

Distil-lang-detect is text language detection module based on sequence classification technique [DistilBERT](https://github.com/huggingface/transformers/tree/master/examples/distillation) by 🤗 [Huggingface Transformers](https://github.com/huggingface/transformers).

## Getting Started

Distil-Lang-Detect can be easily fired-up. Just need to the following.

### Requirements

* python 3.5
* torch >= 1.2.0
* transformers >= 2.2.2

### Installation

```bash
git clone https://github.com/yash1994/distil-lang-detect.git
cd dframcy
python setup.py install
```

## Usage

```python
from distillangdetect.detector import Detector
dct = Detector(device="cpu")
det = dct.detect("I love retro computing.")
print(det)
```

>'English'

## Todos

* [ ] Extensive testing.
* [ ] Add training and evaluation scripts.
* [ ] Output format options.
* [ ] Batch Processing.
* [ ] Bechmarking on different datasets.
