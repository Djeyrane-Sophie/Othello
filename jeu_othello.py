
from tabulate import tabulate

#matrix = [[0 for _ in range(8)] for _ in range(8)]
#print(tabulate(matrix, tablefmt = "fancy_grid"))

class Cell:

    def __init__(self, value='.'):
        self.__value = value

    def __repr__(self):
        return str(self.__value)

    #getter
    def get_value(self):
        return self.__value
    
    #setter
    def set_value(self, new_value):
        self.__value = new_value


class Othellier:

    def __init__(self, row:int,col:int):
        self.matrix = [[Cell() for _ in range(row)] for _ in range(col)]

    def set_cell(self, value, row, col):
            self.matrix[row][col].set_value(value)

    def __str__(self):
        return ' '.join([' '.join([str(cell) for cell in row]) for row in self.matrix])

    def display(self):
        print(tabulate(self.matrix, tablefmt = "fancy_grid"))
    

matrix = Othellier(8,8)
# print(matrix.appercu())

matrix.set_cell('\u26aa',4,4) #white
matrix.set_cell('\u26aa',3,3) #white
matrix.set_cell('\u26ab',3,4) #black
matrix.set_cell('\u26ab',4,3) #black
print(matrix.display())
print('\u26aa')
print('\u26ab')
