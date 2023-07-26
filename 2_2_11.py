class PhoneNumber:
    def __init__(self, number, fio) -> None:
        self.number = number
        self.fio = fio


class PhoneBook:
    phone_lst = []

    def add_phone(self, phone):
        self.phone_lst.append(phone)

    def remove_phone(self, indx):
        self.phone_lst.pop(indx)

    def get_phone_list(self):
        return self.phone_lst
