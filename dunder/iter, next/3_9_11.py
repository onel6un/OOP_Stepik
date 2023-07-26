class Matrix:
    def __init__(self, *args):
        if len(args) == 1:
            mtrx = args[0]
            self._check_mtrx(mtrx)
            self.rows = len(mtrx)
            self.cols = len(mtrx[0])
            self.mtrx = mtrx
        else:
            self._check_args(*args)
            rows, cols, fill_value = args
            self.rows = rows
            self.cols = cols
            self.mtrx = [[fill_value for i in range(cols)] for i in range(rows)]

    @staticmethod
    def _check_args(rows, cols, fill_value):
        if not all((isinstance(rows, int), isinstance(cols, int),
                    isinstance(fill_value, (int, float)))):
            raise TypeError(
                'аргументы rows, cols - целые числа;'
                'fill_value - произвольное число'
            )

    @staticmethod
    def _check_mtrx(mtrx):
        frst_row = mtrx[0]
        for row in mtrx:
            if len(frst_row) != len(row):
                raise TypeError('список должен быть прямоугольным,'
                                ' состоящим из чисел')
        for i in mtrx:
            for j in i:
                if not isinstance(j, int):
                    raise TypeError('список должен быть прямоугольным,'
                                    ' состоящим из чисел')

    @staticmethod
    def _check_value(value):
        if not isinstance(value, (int, float)):
            raise TypeError('значения матрицы должны быть числами')

    @staticmethod
    def _eq_mtrx(mtrx1, mtrx2):
        if len(mtrx1) != len(mtrx2) or len(mtrx1[0]) != len(mtrx2[0]):
            raise ValueError('операции возможны только с матрицами равных размеров')

    def _check_indx(self, i, j):
        if (not isinstance(i, int) or not isinstance(j, int)):
            raise IndexError('недопустимые значения индексов')
        if (0 > i or i >= self.rows) or (0 > j or j >= self.cols):
            raise IndexError('недопустимые значения индексов')

    def __getitem__(self, indx):
        self._check_indx(*indx)
        i, j = indx
        return self.mtrx[i][j]

    def __setitem__(self, indx, value):
        self._check_value(value)
        self._check_indx(*indx)
        i, j = indx
        self.mtrx[i][j] = value

    def __add__(self, other):
        mtrx1 = [row[:] for row in self.mtrx]
        if isinstance(other, self.__class__):
            mtrx2 = [row[:] for row in other.mtrx]
            self._eq_mtrx(mtrx1, mtrx2)
            for i, rows in enumerate(mtrx2):
                for j, value in enumerate(rows):
                    mtrx1[i][j] = mtrx1[i][j] + value
            return Matrix(mtrx1)

        for i, rows in enumerate(mtrx1):
            for j, value in enumerate(rows):
                mtrx1[i][j] = mtrx1[i][j] + other
        return Matrix(mtrx1)

    def __sub__(self, other):
        mtrx1 = [row[:] for row in self.mtrx]
        if isinstance(other, self.__class__):
            mtrx2 = [row[:] for row in other.mtrx]
            self._eq_mtrx(mtrx1, mtrx2)
            for i, rows in enumerate(mtrx2):
                for j, value in enumerate(rows):
                    mtrx1[i][j] = mtrx1[i][j] - value
            return Matrix(mtrx1)

        for i, rows in enumerate(mtrx1):
            for j, value in enumerate(rows):
                mtrx1[i][j] = mtrx1[i][j] - other
        return Matrix(mtrx1)
