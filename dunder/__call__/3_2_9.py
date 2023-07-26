class Handler:
    def __init__(self, methods=('GET',)) -> None:
        self.methods = methods

    def get(self, func, request, *args, **kwargs):
        return f"GET: {func(request)}"

    def post(self, func, request, *args, **kwargs):
        return f"POST: {func(request)}"

    def __call__(self, func):
        def wrapper(request):
            method = request.get('method', 'GET')
            if method in self.methods:
                if method == 'GET':
                    return self.get(func, request)
                if method == 'POST':
                    return self.post(func, request)
            return None
        return wrapper


@Handler(methods=('GET', 'POST'))
def contact(request):
    return "Сергей Балакирев"

res = contact({"method": "POST", "url": "contact.html"})
print(res)


#  Повторим это без синтаксического сахара
# Объявим еще одну функцию
def contact2(request):
    return "Сергей Балакирев"

# Создадим экземпляр класса Handler, передадим в инициализатор именовыанный аргумент 'methods'(параметр декоратора)
dec = Handler(methods=('GET', 'POST'))
# Вызовим экземпляр, с параметром - функцией которую будем декорировать.
# происходит вызов __call__(func), который возвращает вспомогательную wrapper функцию, функция(contact2) которую передали в декоратор, замыкаеться в пространстве имен
f = dec(contact2)
# Вызовем wrapper функцию и передадим в нее парметры для декорируемой функции
res2 = f({"method": "POST", "url": "contact.html"})
print(res2)
