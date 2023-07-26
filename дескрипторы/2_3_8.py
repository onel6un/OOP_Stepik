class ValidateString:
    def __init__(self, min_length, max_length) -> None:
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        return self.min_length <= len(string) <= self.max_length


class StringValue:
    def __init__(self, validator):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instnce, value):
        if self.validator.validate(value):
            setattr(instnce, self.name, value)


class RegisterForm:
    login = StringValue(ValidateString(min_length=3, max_length=100))
    password = StringValue(ValidateString(min_length=3, max_length=100))
    email = StringValue(ValidateString(min_length=3, max_length=100))

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        print(
            '<form>\n'
            f'Логин: {self.login}\n'
            f'Пароль: {self.password}\n'
            f'Email: {self.email}\n'
            '</form>'
        )


form = RegisterForm('88', 'пароль', 'email')
form.show()
