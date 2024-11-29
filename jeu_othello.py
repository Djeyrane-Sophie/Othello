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
    def flip(self):  #si la coleur est noir retourner noir et si la couleur est blanc retourner blanc
        if self.color=='\u25cf': #black
            self.color='\u25cb' #white
        else:
            self.color='\u25cf'

class Othellier:
    def __init__(self, row:int,col:int):
        self.matrix = [[Cell() for _ in range(row)] for _ in range(col)]
    def set_cell(self, value, row, col):
            self.matrix[row][col].set_value(value)
    def get_cell(self, row, col):
            return self.matrix[row][col].get_value()
    def update_cell(self,value,row,col):
        if value in ['\u25cf','\u25cb']:
            self.matrix[row][col].set_value(value)
            print(f"Cell ({row},{col} update to {value})")
        else:
            print(f"invalid value! Please use '\u25cf' for black or '\u25cb' for white")
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
                  direction = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
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
                  direction = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
                  for dx, dy in direction:
                      new_i = i + dx
                      new_j = j + dy
                      if 0 < new_i < len(self.matrix) and 0 < new_j < len(self.matrix):
                          if self.get_cell(new_i, new_j) == '.':
                              valid_places.append(self.matrix[new_i][new_j])
                              self.set_cell('\u2705',new_i, new_j)    
        self.appercu()     
        return valid_places
    
    def has_valid_move(self, color):
#  Vérifie si un joueur (noir ou blanc) a des mouvements valides.
 
        if color == '\u25cf': # black
            return bool(self.valid_moves_black()) # Si la liste des mouvements est non vide, renvoie True.
        if color == '\u25cb': # white
            return bool(self.valid_moves_white())      
        
        if has_move:
            print(f"{color.capitalized()} a des mouvements valides")

        else: print(f"{color.capitalized()} n'a pas de mouvements valides")
        return has_move

matrix = Rules(8, 8)

matrix.set_cell('\u25cf', 4, 4)
matrix.set_cell('\u25cf', 3, 3)
matrix.set_cell('\u25cb', 3, 4)
matrix.set_cell('\u25cb', 4, 3)

matrix.has_valid_move('\u25cf')
matrix.has_valid_move('\u25cb')