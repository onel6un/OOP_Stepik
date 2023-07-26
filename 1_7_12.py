class Viber:
    list_msg = []

    @classmethod
    def add_message(cls, msg):
        """добавление нового сообщения в список сообщений;
        """
        cls.list_msg.append(msg)

    @classmethod
    def remove_message(cls, msg):
        """удаление сообщения из списка;
        """
        cls.list_msg.remove(msg)

    @staticmethod
    def set_like(msg):
        """поставить/убрать лайк для сообщения msg 
        (если лайка нет то он ставится, если уже есть, то убирается);
        """
        if msg.fl_like is True:
            msg.fl_like = False
        else:
            msg.fl_like = True

    @classmethod
    def show_last_message(cls, i):
        """отображение последних сообщений;
        """
        if len(cls.list_msg) > i:
            return cls.list_msg
        return cls.list_msg[:i]

    @classmethod
    def total_messages(cls):
        """звращает общее число сообщений.
        """
        return len(cls.list_msg)


class Message:
    """позволяет создавать объекты-сообщения со следующим 
    набором локальных свойств:
    text - текст сообщения (строка);
    fl_like - поставлен или не поставлен лайк у сообщения 
    (булево значение True - если лайк есть и False - в противном 
    случае, изначально False);
    P.S. Как хранить список сообщений, решите самостоятельно.
    """
    def __init__(self, text) -> None:
        self.text = text
        self.fl_like = False


msg = Message("Всем привет!")

print(msg.fl_like)
Viber.set_like(msg)

print(msg.fl_like)
Viber.set_like(msg)

print(msg.fl_like)