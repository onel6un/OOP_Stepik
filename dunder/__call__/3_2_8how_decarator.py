class HandlerGET:
    def __init__(self, func) -> None:
        self.func = func

    def get(self, func, request, *args, **kwargs):
        method = request.get('method', 'GET')
        if method == 'GET':
            return f"GET: {func(request)}"
        return None

    def __call__(self, arg):
        return self.get(self.func, arg)



@HandlerGET
def contact(request):
    return "Сергей Балакирев"

res = contact({"method": "GET", "url": "contact.html"})
print(res)