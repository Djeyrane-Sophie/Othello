from tabulate import tabulate
 
class Cell:
    def __init__(self, value='.'):
        self.__value = value
    def __repr__(self):
        return str(self.__value)
    def get_value(self):
        return self.__value
    def set_value(self, new_value):
        self.__value = new_value
    def flip(self): 
        if self.__value == '\u26aa':
            self.__value = '\u26ab'
        else:
            self.__value = '\u26aa'

class Othellier:
    def __init__(self, row:int,col:int):
        self.matrix = [[Cell() for _ in range(row)] for _ in range(col)]
    def set_cell(self, value, row, col):
            self.matrix[row][col].set_value(value)
    def get_cell(self, row, col):
            return self.matrix[row][col].get_value()
    def flip_cell(self, row, col):
        self.matrix[row][col].flip()
    def __str__(self):
        return ' '.join([' '.join([str(cell) for cell in row]) for row in self.matrix]) 
    def appercu(self):
        print(tabulate(self.matrix, tablefmt = "fancy_grid"))



class Rules(Othellier):
    def valid_moves_black(self):
        valid_places =[]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
               if self.get_cell(i,j) == '\u26ab':
                  direction = [(0,1),(1,0),(0,-1),(-1,0)]
                  for dx, dy in direction:
                      new_i = i + dx
                      new_j = j + dy
                      if 0 < new_i < len(self.matrix) and 0 < new_j < len(self.matrix):
                          if self.get_cell(new_i, new_j) == '.':
                              valid_places.append(self.matrix[new_i][new_j])
                              self.set_cell('\u2705',new_i, new_j)    
        self.appercu()     
        return valid_places

    def valid_moves_white(self):
        valid_places =[]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
               if self.get_cell(i,j) == '\u26aa':
                  direction = [(0,1),(1,0),(0,-1),(-1,0)]
                  for dx, dy in direction:
                      new_i = i + dx
                      new_j = j + dy
                      if 0 < new_i < len(self.matrix) and 0 < new_j < len(self.matrix):
                          if self.get_cell(new_i, new_j) == '.':
                              valid_places.append(self.matrix[new_i][new_j])
                              self.set_cell('\u2705',new_i, new_j)    
        self.appercu()     
        return valid_places

    def flip_black(self, i_input, j_input): 
        black = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.get_cell(i,j) == '\u26aa':
                    black.append((i,j))
        for tuple in black:
            delta_x = tuple[0] - i_input
            delta_y = tuple[1] - j_input
            if delta_x == 0:
                for j_1 in range(1,abs(delta_y)):
                    if delta_y > 0:
                        if self.get_cell(i_input , j_input + j_1) == '\u26aa' or self.get_cell(i_input , j_input + j_1) == '.':
                            break
                        else:
                            self.flip_cell(i_input , j_input + j_1)
                    elif delta_y < 0:
                        if self.get_cell(i_input , j_input - j_1) == '\u26aa' or self.get_cell(i_input , j_input - j_1) == '.':
                            break
                        else:
                            self.flip_cell(i_input , j_input - j_1)


            elif delta_y == 0:
                for i_1 in range(1,abs(delta_x)):
                    if delta_x < 0:
                        if self.get_cell(i_input + i_1 , j_input) == '\u26aa' or self.get_cell(i_input + i_1 , j_input) == '.':
                            break
                        else:
                            self.flip_cell(i_input + i_1 , j_input)
                    elif delta_x < 0:
                        if (i_input + i_1 , j_input) == '\u26aa' or self.get_cell(i_input , j_input - j_1) == '.':
                            break
                        else:
                            self.flip_cell(i_input + i_1 , j_input)
            # if abs(delta_y) == abs(delta_x):
            #     for i_2 in range(1,abs(delta_x)):
            #         for j_2 in range(1,abs(delta_y)):
            #             if delta_y:
            #                 if self.get_cell(t_3[0]+ i_2,t_3[1] + j_2) == '\u26aa' or self.get_cell(t_3[0]+ i_2,t_3[1] + j_2) == '.':







        #self.appercu()
                


matrix = Rules(8,8)


matrix.set_cell('\u26aa',4,4)
matrix.set_cell('\u26aa',3,3)
matrix.set_cell('\u26ab',3,4)
matrix.set_cell('\u26ab',4,3)
matrix.set_cell('\u26aa',4,5)
#matrix.flip_cell(4,4)
#matrix.appercu()
#matrix.valid_moves_white()
#matrix.flip_black(4,5)
# print('black = \u26aa')
# print('white = \u26ab')
# print('green =\u2705')
#matrix.flip_black()
#        flip_x_direction = []
#flip_y_direction = [] flip_x_y_direction = []

