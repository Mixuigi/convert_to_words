import sys
import os
import re


def convert_words(textpath):
    with open(textpath, 'r') as f:
        text = f.read()
    old_text_len = len(text)
    while True:
        text = re.sub(r'(.)\1', '', text)
        if len(text) == old_text_len:
            break
        else:
            old_text_len = len(text)
    print("".join(text))


if __name__ == '__main__':
    textpath = sys.argv[-1]
    if os.path.exists(textpath):
        convert_words(textpath)
    else:
        print('Invalid file path')