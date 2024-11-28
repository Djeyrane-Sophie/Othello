
from tabulate import tabulate

class Cell:
    def __init__(self, value='  '):
        self.__value = value
    def __repr__(self):
        return str(self.__value)
    def get_value(self):
        return self.__value
    def set_value(self, new_value):
        self.__value = new_value

class Othellier:
    def __init__(self, row:int,col:int):
        self.matrix = [[Cell() for _ in range(row)] for _ in range(col)]
    def set_cell(self, value, row, col):
            self.matrix[row][col].set_value(value)
    def __str__(self):
        return ' '.join([' '.join([str(cell) for cell in row]) for row in self.matrix])

    def appercu(self):
        print(tabulate(self.matrix, tablefmt = "fancy_grid"))
    
    
matrix = Othellier(8,8)

matrix.set_cell('\u25cf',4,4)
matrix.set_cell('\u25cf',3,3)
matrix.set_cell('\u25cb',3,4)
matrix.set_cell('\u25cb',4,3)
print(matrix.appercu())
print('\u25cf')
print('\u25cb')

