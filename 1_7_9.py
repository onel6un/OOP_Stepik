from string import ascii_lowercase, digits
import re 


class CardCheck():
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        pattern = re.compile("^\d{4}\-\d{4}\-\d{4}\-\d{4}$")
        if pattern.match(number):
            return True
        return False

    @staticmethod
    def check_name(name):
        pattern = re.compile('^[A-Z]{1,100}\s[A-Z]{1,100}$')
        if pattern.match(name):
            return True
        return False

is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")

print(is_name, is_number)