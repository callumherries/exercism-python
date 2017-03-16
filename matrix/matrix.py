class Matrix(object):
    def __init__(self, matrix_string):
        self._rows = [[int(x) for x in row.split()] for row in matrix_string.split("\n")]
        self._cols = [list(x) for x in zip(*self.rows)]

    @property
    def rows(self):
        return [row[:] for row in self._rows]

    @property
    def cols(self):
        return [col[:] for col in self._cols]