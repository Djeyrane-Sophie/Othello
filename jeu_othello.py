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
    def __str__(self):
        return ' '.join([' '.join([str(cell) for cell in row]) for row in self.matrix])
    #method display initial and current
    def display(self):
        # print('_ A _ B _ C _ D _ E _ F _ G _ H')
        print(tabulate(self.matrix, tablefmt = "fancy_grid", \
            headers=list('ABCDEFGH'), showindex=list('12345678')))
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


    def has_valid_move(self, color):
#  je vérifie si un joueur (noir ou blanc) a des mouvements valides.
 
        if color == '\u25cf': # black
            current_moves=self.valid_moves_black() 
        else: #white 
            current_moves=self.valid_moves_white()
#je verifie si le joueur adv peut jouer : 
        if color == '\u25cf': # black
            opponent_moves= self.valid_moves_black() 
        else: #white 
            opponent_moves=self.valid_moves_white()
      
        current_player_can_play= len(current_moves)>0
        opponent_player_can_play=len(opponent_moves)>0

        game_over=not current_player_can_play and not opponent_player_can_play
        return current_player_can_play, game_over 

if __name__ == "__main__":
    board = Rules(8, 8)
    board.set_cell('\u25cf', 3, 3)
    board.set_cell('\u25cb', 3, 4)
    board.set_cell('\u25cb', 4, 3)
    board.set_cell('\u25cf', 4, 4)

    board.display()
    current_color = '\u25cf'  # je commence avec les noirs
    while True:

        can_play, game_over = board.has_valid_move(current_color)
        if game_over:
            print("Game Over!")
            break
        elif can_play:
            print(f"{current_color} est ton tour.Fais un mouvement.")
            #le tour du joueur.
        else:
            print(f"{current_color} ne peut pas jouer.Passe ton tour .")
        #  je passe au joueur suivant
        current_color = '\u25cb' if current_color == '\u25cf' else '\u25cf'