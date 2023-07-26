class Course:
    def __init__(self, name) -> None:
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        self.modules.pop(indx)


class Module:
    def __init__(self, name) -> None:
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        self.lessons.pop(indx)


class LessonItem:
    attrs = {'title': str, 'practices': int, 'duration': int}

    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if key in self.attrs and self.attrs[key] == type(value):
            if key in ('practices', 'duration') and value < 0:
                raise TypeError("Неверный тип присваиваемых данных.")
            super().__setattr__(key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __getattr__(self, key):
        return False

    def __delattr__(self, key):
        if key in ('title', 'practices', 'duration'):
            return
        super().__delattr__(key)
