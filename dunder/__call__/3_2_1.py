from random import randint, choice


class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        return ''.join([choice(self.psw_chars) for i in range(randint(self.min_length, self.max_length))])


psw = RandomPassword(
    min_length=5,
    max_length=20,
    psw_chars="qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
)

lst_pass = [psw() for i in range(3)]


# Реализация с помощью замыкания
def random(psw_chars, min_length, max_length):
    def generate():
        return ''.join([choice(psw_chars) for i in range(randint(min_length, max_length))])
    return generate


psw = random(
    min_length=5,
    max_length=20,
    psw_chars="qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
)

print(psw())
print(psw())
print(psw())
