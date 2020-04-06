# coding: utf-8
from __future__ import unicode_literals

import re


class Cleaner:
    def __init__(self):
        self.email_re_pattern = (
            r"[-_.0-9A-Za-z]{1,64}@[-_0-9A-Za-z]{1,255}[-_.0-9A-Za-z]{1,255}"
        )
        self.url_re_pattern = r"https?://[-_.?&~;+=/#0-9A-Za-z]{1,2076}"

        # http://stackoverflow.com/a/13752628/6762004
        self.emoji_re_pattern = r"[\U00010000-\U0010ffff]"

    def clean_text(self, text):
        text = re.sub(self.email_re_pattern, " ", text)
        text = re.sub(self.url_re_pattern, " ", text)
        text = re.sub(self.emoji_re_pattern, " ", text)

        return text
