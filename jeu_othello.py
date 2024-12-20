from tabulate import tabulate
 
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

    def get_cell(self, row, col):
            return self.matrix[row][col].get_value()

    def __str__(self):
        return ' '.join([' '.join([str(cell) for cell in row]) for row in self.matrix])

    #method display initial and current
    def display(self):
        print(tabulate(self.matrix, tablefmt = "fancy_grid"))
    
    #method count points and display scores
    def count_points(self):
        score_white = 0
        score_black = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.get_cell(i, j) == '\u26aa':
                    score_white +=1
                if self.get_cell(i, j) == '\u26ab':
                    score_black +=1
        print('white score =', score_white)
        print('black score =', score_black)

 

class Rules(Othellier):

    #method is_valid_move for black
    def valid_moves_black(self):
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
        self.display()     
        return valid_places
    
    #method is_valid_move for white
    def valid_moves_white(self):
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
        self.display()     
        return valid_places
    
    #method input coordinates of the next move
    def input_coordinates(self):
        string_input = input( 'write down the row and column without any space (example: 5B )')
        row_input = int(string_input[0])-1 #indexation entre 0 et 1
        col_input = string_input[1].upper()
        col_input = list('ABCDEFGH').index(col_input) #indexation entre 0 et 1
        tuple_input = (row_input, col_input)
        print('Requested move:', tuple_input)
        return tuple_input

    



    
if __name__ == '__main__':

    matrix = Rules(8,8)

    matrix.set_cell('\u26aa',4,4) #white
    matrix.set_cell('\u26aa',3,3) #white
    matrix.set_cell('\u26ab',3,4) #black
    matrix.set_cell('\u26ab',4,3) #black

    # print(matrix.display())
    matrix.valid_moves_black()
    matrix.count_points()
    matrix.input_coordinates()

    print('black = \u26aa')
    print('white = \u26ab')
    print('green = \u2705')
