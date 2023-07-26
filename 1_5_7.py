# здесь объявляются все необходимые классы
class Graph():
    def __init__(self, data, is_show=True):
        self.data = data.copy()
        self.is_show = is_show

    def set_data(self, data):
        self.data = data

    def _get_str_data(self):
        return ' '.join(map(str, self.data))

    def show_table(self):
        if self.is_show is False:
            return print("Отображение данных закрыто")

        return print(self._get_str_data())

    def show_graph(self):
        if self.is_show is False:
            return print("Отображение данных закрыто")

        return print(f'Графическое отображение данных: {self._get_str_data()}')

    def show_bar(self):
        if self.is_show is False:
            return print("Отображение данных закрыто")

        return print(f'Столбчатая диаграмма: {self._get_str_data()}')

    def set_show(self, fl_show):
        self.is_show = fl_show


# считывание списка из входного потока (эту строку не менять)
data_graph = list(map(int, input().split()))

# здесь создаются объекты классов и вызываются нужные методы
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()
