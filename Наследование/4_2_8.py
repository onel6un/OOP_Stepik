class VideoItem:
    def __init__(self, title, descr, path) -> None:
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()


class VideoRating:
    __rating = 0

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        print(value)
        if not isinstance(value, int) or (0 > value or value > 5):
            raise ValueError('неверное присваиваемое значение')
        self.__rating = value


v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР', 'D:/videos/python_oop.mp4')
print(v.rating.rating) # 0
v.rating.rating = 5
print(v.rating.rating) # 5
title = v.title
descr = v.descr
v.rating.rating = 6