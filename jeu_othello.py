import vector
from tabulate import tabulate
#matrix = [[0 for _ in range(8)] for _ in range(8)]
#print(tabulate(matrix, tablefmt = "fancy_grid"))
class Cell:
    def __init__(self, value=0):
        self.__value = value
    def __repr__(self):
        return str(self.__value)
    @property
    def value(self):
        return self.__value
    def get_value(self):
        return self.__value
    def set_value(self, new_value):
        v = ["noir", "blanc", "vide"]
        if new_value in v:
            self.__value = new_value
        pass
class Othellier:
    def __init__(self, row:int,col:int):
        self.matrix = [[Cell() for _ in range(row)] for _ in range(col)]
    def set_cell(self, value, row, col):
            self.matrix[row][col].set_value(value)
    def __str__(self):
        return ' '.join([' '.join([str(cell) for cell in row]) for row in self.matrix])
        pass
    def appercu(self):
        print(tabulate(self.matrix, tablefmt = "fancy_grid"))
    
    
matrix = Othellier(8,8)
print(matrix.appercu())

