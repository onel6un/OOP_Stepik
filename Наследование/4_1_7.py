class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):
    def get(self, request):
        if not isinstance(request, dict):
            raise TypeError('request не является словарем')
        if 'url' not in request:
            raise TypeError('request не содержит обязательного ключа url')
        return f"url: {request['url']}"

    def render_request(self, request, method):
        if method not in self.methods:
            raise TypeError('данный запрос не может быть выполнен')
        func = getattr(self, method.lower())
        return func(request)


dv = DetailView()
html = dv.render_request({'url': 'https://site.ru/home'}, 'GET') 
print(html)