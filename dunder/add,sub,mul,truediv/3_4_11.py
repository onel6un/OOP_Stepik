class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    @staticmethod
    def _get_empty_mtrx(matrix, step, size):
        rows = len(matrix)
        cols = len(matrix[0])
        stx, sty = step
        sx, sy = size
        wdht_mtrx = (rows - stx) // sx + 1
        hght_mtrx = (cols - sty) // sy + 1
        return [[0 for i in range(wdht_mtrx)] for i in range(hght_mtrx)]

    def __call__(self, matrix):
        if not all(map(lambda x: True if len(matrix[0]) == len(x) else False, matrix)):
            raise ValueError(
                        "Неверный формат для первого параметра matrix."
                    )
        for i in matrix:
            for ii in i:
                if type(ii) not in (int, float):
                    raise ValueError(
                        "Неверный формат для первого параметра matrix."
                    )
        empty_mtrx = self._get_empty_mtrx(matrix, self.step, self.size)
        step_y = 0
        for i, field in enumerate(empty_mtrx):
            lst_f = matrix[step_y:self.size[1]+step_y]
            step_y += self.step[1]
            step_x = 0
            for j, cell in enumerate(field):
                lst_v = []
                for field in lst_f:
                    lst_v += field[step_x:self.size[0]+step_x]
                empty_mtrx[i][j] = max(lst_v)
                step_x += self.step[0]
        return empty_mtrx


mp = MaxPooling(step=(1, 1), size=(3,3))
res = mp([[1, 2, 3, 4],
          [5, 6, 7, 8],
          [1, 2, 3, 4],
          [9, 8, 7, 6],
          [5, 4, 3, 2]])
print(res)