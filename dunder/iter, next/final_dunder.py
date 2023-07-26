from random import randint


class TicTacToe:
    FREE_CELL = 0      # свободная клетка
    HUMAN_X = 1        # крестик (игрок - человек)
    COMPUTER_O = 2     # нолик (игрок - компьютер)

    def __init__(self) -> None:
        self.init()

    @staticmethod
    def _check_indx(indx):
        i, j = indx
        if (
            not (isinstance(i, int) or isinstance(i, int))
            or (i < 0 or j < 0)
            or (i > 3 or j > 3)
        ):
            raise IndexError('некорректно указанные индексы')

    @classmethod
    def _check_value(cls, value):
        if value not in (cls.FREE_CELL, cls.HUMAN_X, cls.COMPUTER_O):
            raise IndexError('некорректно указано значение')

    def _check_empty_cell(self):
        for row in self.pole:
            for cell in row:
                if cell.value == self.FREE_CELL:
                    return True

        return False

    def _check_row(self, row, fl):
        return all(map(lambda x: x.value == fl, row))

    def _check_win(self, who):
        diag_l = []
        indx_l = 0

        diag_r = []
        indx_r = 2

        for row in self.pole:
            if self._check_row(row, who):
                return True

            diag_l.append(row[indx_l])
            indx_l += 1

            diag_r.append(row[indx_r])
            indx_r -= 1

        if (self._check_row(diag_l, who) or self._check_row(diag_r, who)):
            return True

        indx = 0
        while indx != 3:
            lst_cell = []
            for row in self.pole:
                lst_cell.append(row[indx])
            if self._check_row(row, lst_cell):
                return True
            indx += 1

        return False

    @property
    def is_human_win(self):
        return self._check_win(self.HUMAN_X)

    @property
    def is_computer_win(self):
        return self._check_win(self.COMPUTER_O)

    def _get_cell(self, indx):
        self._check_indx(indx)
        i, j = indx
        return self.pole[i][j]

    def __getitem__(self, indx):
        cell = self._get_cell(indx)
        return cell.value

    def __setitem__(self, indx, value):
        self._check_value(value)
        cell = self._get_cell(indx)
        cell.value = value

    def __bool__(self):
        if self.is_human_win:
            return False
        if self.is_computer_win:
            return False
        if not self._check_empty_cell():
            return False
        return True

    def init(self):
        self.pole = tuple([tuple([Cell() for i in range(3)]) for i in range(3)])

    def show(self):
        for row in self.pole:
            lst_value = list(map(lambda x: x.value, row))
            print(lst_value)

    def human_go(self):
        indx = list(map(lambda x: int(x), input('Координаты клетки: ').split()))
        cell = self._get_cell(indx)
        if cell:
            cell.value = self.HUMAN_X
        else:
            print('Клетка занята')
            self.human_go()

    def computer_go(self):
        i, j = randint(0, 2), randint(0, 2)
        cell = self.pole[i][j]
        if cell:
            cell.value = self.COMPUTER_O
        else:
            self.computer_go()


class Cell:
    def __init__(self) -> None:
        self.value = 0

    def __bool__(self):
        return self.value == 0

game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")