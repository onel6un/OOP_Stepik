class Data():
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


class Server():
    list_serv = []

    @classmethod
    def _get_ip(cls):
        if len(cls.list_serv) == 0:
            return 1
        i = len(cls.list_serv)
        return i + 1

    def __init__(self) -> None:
        self.buffer = []
        self.ip = self._get_ip()
        self.connect_r = None
        Server.list_serv.append(self)

    def send_data(self, data):
        self.connect_r.buffer.append(data)

    def get_data(self):
        data = self.buffer.copy()
        self.buffer = []
        return data

    def get_ip(self):
        return self.ip


class Router():
    def __init__(self) -> None:
        self.buffer = []
        self.connects_s = []

    def link(self, server):
        self.connects_s.append(server)
        server.connect_r = self

    def unlink(self, server):
        self.connects_s.remove(server)

    def _get_server(self, ip):
        return list(filter(lambda x: x.ip == ip, self.connects_s))[0]

    def send_data(self):
        for pac in self.buffer:
            try:
                server = self._get_server(pac.ip)
                server.buffer.append(pac)
            except IndexError:
                continue
        self.buffer = []


assert hasattr(Router, 'link') and hasattr(Router, 'unlink') and hasattr(Router, 'send_data'), "в классе Router присутсвутю не все методы, указанные в задании"
assert hasattr(Server, 'send_data') and hasattr(Server, 'get_data') and hasattr(Server, 'get_ip'), "в классе Server присутсвутю не все методы, указанные в задании"

router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()

router.unlink(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
router.send_data()
msg_lst_to = sv_to.get_data()
assert msg_lst_to == [], "метод get_data() вернул неверные данные, возможно, неправильно работает метод unlink()"
