import random


class Cell():
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole():
    def __init__(self, N, M):
        if N**2/2 < M:
            return 'Мин слишком много'
        self.N = N
        self.M = M

    def _field_creator(self):
        return [Cell() for i in range(self.N)]

    def _empty_pole(self):
        self.pole = [self._field_creator() for i in range(self.N)]

    def _set_mine(self):
        pole = self.pole
        field = random.choice(pole)
        cell = random.choice(field)
        if cell.mine is False:
            cell.mine = True
        else:
            self._set_mine()

    def _fill_pole(self):
        for i in range(self.M):
            self._set_mine()

    def _set_ard_mines(self):
        i_last_filed = self.N - 1
        i_last_cell = self.N - 1
        for i_f, field in enumerate(self.pole):
            for i_c, cell in enumerate(field):
                if cell.mine is True:
                    continue

                try:
                    # Клетка слева диагонально вверху
                    l_diag_u_cell = self.pole[i_f-1][i_c-1]
                except IndexError:
                    pass

                try:
                    # Клетка слева от текущей
                    l_cell = self.pole[i_f][i_c-1]
                except IndexError:
                    pass

                try:
                    # Клетка слева диагонально внизу
                    l_diag_d_cell = self.pole[i_f+1][i_c-1]
                except IndexError:
                    pass

                try:
                    # Клетка внизу от текущей
                    d_cell = self.pole[i_f+1][i_c]
                except IndexError:
                    pass

                try:
                    # Клетка справа диагонально внизу
                    r_diag_d_cell = self.pole[i_f+1][i_c+1]
                except IndexError:
                    pass

                try:
                    # Клетка справа
                    r_cell = self.pole[i_f][i_c+1]
                except IndexError:
                    pass

                try:
                    # Клетка справа диагонально вверху
                    r_diag_u_cell = self.pole[i_f-1][i_c+1]
                except IndexError:
                    pass

                try:
                    # Клетка вверху
                    u_cell = self.pole[i_f-1][i_c]
                except IndexError:
                    pass

                # Левая верхняя
                if i_c == 0 and i_f == 0:
                    list_cell = list(map(lambda x: x.mine, [r_cell, r_diag_d_cell, d_cell]))
                    cell.around_mines = list_cell.count(True)
                    continue
                # Правая верхняя
                if i_c == i_last_cell and i_f == 0:
                    cell.around_mines = list(map(lambda x: x.mine, [l_cell, d_cell, l_diag_d_cell])).count(True)
                    continue 
                # Левая нижняя
                if i_c == 0 and i_f == i_last_filed:
                    cell.around_mines = list(map(lambda x: x.mine, [u_cell, r_cell, r_diag_u_cell])).count(True)
                    continue
                # Правая нижняя
                if i_c == i_last_cell and i_f == i_last_filed:
                    cell.around_mines = list(map(lambda x: x.mine, [u_cell, l_cell, l_diag_u_cell])).count(True)
                    continue

                # Проверка если верхнее поле
                if i_f == 0: 
                    cell.around_mines = list(map(lambda x: x.mine, [l_cell, l_diag_d_cell, d_cell, r_diag_d_cell, r_cell])).count(True)
                    continue
                # Проверка если нижнее поле
                if i_f == i_last_filed:
                    cell.around_mines = list(map(lambda x: x.mine, [l_cell, u_cell, r_cell, r_diag_u_cell, l_diag_u_cell])).count(True)
                    continue
                # Проверка если поле слева
                if i_c == 0:
                    cell.around_mines = list(map(lambda x: x.mine, [u_cell, r_cell, d_cell, r_diag_u_cell, r_diag_d_cell])).count(True)
                    continue
                # проверка если поле справа
                if i_c == i_last_cell:
                    cell.around_mines = list(map(lambda x: x.mine, [u_cell, l_cell, d_cell, l_diag_u_cell, l_diag_d_cell])).count(True)
                    continue

                cell.around_mines = list(map(lambda x: x.mine, [u_cell, l_cell, d_cell, r_cell, l_diag_u_cell, l_diag_d_cell, r_diag_u_cell, r_diag_d_cell])).count(True)

    def init(self):
        self._empty_pole()
        self._fill_pole()
        self._set_ard_mines()

    def _show_cell(self, obj):
        if obj.mine:
            return '*'
        '''if obj.fl_open is False:
            return '#'''
        return f'{obj.around_mines}'

    '''def show(self):
        # Отображение полей
        print("   ".join([str(i) for i in range(self.N)]))
        print("   ".join(['_' for i in range(self.N)]))
        for i, field in enumerate(self.pole):
            # Отоброжение строк поля
            print("   ".join(list(map(self._show_cell, field)))+str(f'|  {i}'))'''
    
    def show(self):
        for i, field in enumerate(self.pole):
            # Отоброжение строк поля
            print(list(map(self._show_cell, field)))

    def click(self, i_c, i_f):
        if self.pole[i_f][i_c].mine:
            return print('You lose!')
        self.pole[i_f][i_c].fl_open = True
        '''for i in range(5):
            cell = self.pole[i_f + random.randint(-2, 2)][i_c + random.randint(-2, 2)]
            if cell.mine:
                continue
            cell.fl_open = True'''


txt_priv = 'Введите размер, кол-во мин (N, M): '
txt_choice_cell = 'Введите координаты (X X): '

a, b = list(map(lambda x: int(x), input(txt_priv).split()))  
gp = GamePole(a, b)
gp.init()

while True:
    gp.show()
    a, b = list(map(lambda x: int(x), input(txt_choice_cell).split()))
    gp.click(a, b)
