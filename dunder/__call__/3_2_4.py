import re


class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, str):
        ext_patt = '|'.join(self.extensions)
        pattern = f'([A-Za-z0-9._]+)\.({ext_patt})'
        return re.match(pattern, str)
