import json
from conf import *


def load_key():
    with open(KEY, 'r', encoding='utf-8') as f:
        key_data = json.load(f)
        return key_data['key'].upper()


def load_source_text():
    with open(SOURCE_PATH, 'r', encoding='utf-8') as f:
        return f.read().upper()