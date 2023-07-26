import re


class FileAcceptor:
    def __init__(self, *args) -> None:
        self.lst_acc = list(args)

    def __call__(self, str):
        ext_patt = '|'.join(self.lst_acc)
        pattern = f'([A-Za-z0-9._]+)\.({ext_patt})'
        return re.match(pattern, str)

    def __add__(self, other):
        lst_acc = self.lst_acc.copy()
        for ext in other.lst_acc:
            if ext not in self.lst_acc:
                lst_acc.append(ext)

        return FileAcceptor(*lst_acc)


acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
acceptor12 = acceptor1 + acceptor2
print(acceptor12.lst_acc)