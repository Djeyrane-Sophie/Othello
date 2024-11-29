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

    def cleaning(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.get_cell(i, j) == '\u2705':
                    self.set_cell('.',i, j)  

    def flip_cell(self, row, col):
        self.matrix[row][col].flip()



 

class Rules(Othellier):

    #method is_valid_move for black
    def valid_moves_black(self):
        valid_places =[]
        valid_place_coordinates = []
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
                              valid_place_coordinates.append((new_i, new_j)) 
                              self.set_cell('\u2705',new_i, new_j)    
        self.display()     
        print(valid_place_coordinates)
        return valid_place_coordinates
    
    #method is_valid_move for white
    def valid_moves_white(self):
        valid_places =[]
        valid_place_coordinates = []
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
                              valid_place_coordinates.append((new_i, new_j)) 
                              self.set_cell('\u2705',new_i, new_j)                         
        self.display()   
        print(valid_place_coordinates)  
        return valid_place_coordinates
    
    def flip_black(self, i_input, j_input): 
        black = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.get_cell(i,j) == '\u26ab':
                    black.append((i,j))
        for tuple in black:
            # print(tuple)
            # print(i_input,j_input)
            delta_x = i_input - tuple[0]
            delta_y = j_input - tuple[1]
            if delta_x == 0 and delta_y < 0:
                ready_to_flip_x_pos = []
                ready_to_flip_values_x_pos = []
                for j_1 in range(1,abs(delta_y)):
                    ready_to_flip_x_pos.append((tuple[0],tuple[1] - j_1))
                for t_x_pos in ready_to_flip_x_pos:
                    ready_to_flip_values_x_pos.append(self.get_cell(t_x_pos[0],t_x_pos[1]))
                if all(element_x_pos == '\u26aa' for element_x_pos in ready_to_flip_values_x_pos):
                    for t_x_pos in ready_to_flip_x_pos:
                            self.flip_cell(t_x_pos[0],t_x_pos[1])
                else:
                    break
                
            elif delta_x == 0 and delta_y > 0:
                ready_to_flip_x_neg = []
                ready_to_flip_values_x_neg = []
                for j_1 in range(1,abs(delta_y)):
                    ready_to_flip_x_neg.append((tuple[0],tuple[1] + j_1))
                for t_x_neg in ready_to_flip_x_neg:
                    ready_to_flip_values_x_neg.append(self.get_cell(t_x_neg[0],t_x_neg[1]))
                if all(element_x_neg == '\u26aa' for element_x_neg in ready_to_flip_values_x_neg):
                    for t_x_neg in ready_to_flip_x_neg:
                        self.flip_cell(t_x_neg[0],t_x_neg[1])
                else:
                    break
        
        for tuple in black:
            delta_x = i_input - tuple[0]
            delta_y = j_input - tuple[1]
            # print(delta_x)
            if delta_y == 0 and delta_x < 0:
                ready_to_flip_y_pos = []
                ready_to_flip_values_y_pos = []
                for i_1 in range(1,abs(delta_x)):
                    ready_to_flip_y_pos.append((tuple[0] - i_1, tuple[1]))
                for t_y_pos in ready_to_flip_y_pos:
                    ready_to_flip_values_y_pos.append(self.get_cell(t_y_pos[0],t_y_pos[1]))
                if all(element_y_pos == '\u26aa' for element_y_pos in ready_to_flip_values_y_pos):
                    for t_y_pos in ready_to_flip_y_pos:
                            self.flip_cell(t_y_pos[0],t_y_pos[1])
                else:
                    break      
            elif delta_x > 0 and delta_y == 0:
                ready_to_flip_y_neg = []
                ready_to_flip_values_y_neg = []
                for i_1 in range(1,abs(delta_x)):
                    ready_to_flip_y_neg.append((tuple[0] + i_1, tuple[1]))
                for t_y_neg in ready_to_flip_y_neg:
                    ready_to_flip_values_y_neg.append(self.get_cell(t_y_neg[0],t_y_neg[1]))
                if all(element_y_neg == '\u26aa' for element_y_neg in ready_to_flip_values_y_neg):
                    for t_y_neg in ready_to_flip_y_neg:
                            self.flip_cell(t_y_neg[0],t_y_neg[1])
                else:
                    break
        self.display()

    def flip_white(self, i_input, j_input): 
        white = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.get_cell(i,j) == '\u26aa':
                    white.append((i,j))
        for tuple in white:
            # print(tuple)
            # print(i_input,j_input)
            delta_x = i_input - tuple[0]
            delta_y = j_input - tuple[1]
            if delta_x == 0 and delta_y < 0:
                ready_to_flip_x_pos = []
                ready_to_flip_values_x_pos = []
                for j_1 in range(1,abs(delta_y)):
                    ready_to_flip_x_pos.append((tuple[0],tuple[1] - j_1))
                for t_x_pos in ready_to_flip_x_pos:
                    ready_to_flip_values_x_pos.append(self.get_cell(t_x_pos[0],t_x_pos[1]))
                if all(element_x_pos == '\u26ab' for element_x_pos in ready_to_flip_values_x_pos):
                    for t_x_pos in ready_to_flip_x_pos:
                            self.flip_cell(t_x_pos[0],t_x_pos[1])
                else:
                    break
                
            elif delta_x == 0 and delta_y > 0:
                ready_to_flip_x_neg = []
                ready_to_flip_values_x_neg = []
                for j_1 in range(1,abs(delta_y)):
                    ready_to_flip_x_neg.append((tuple[0],tuple[1] + j_1))
                for t_x_neg in ready_to_flip_x_neg:
                    ready_to_flip_values_x_neg.append(self.get_cell(t_x_neg[0],t_x_neg[1]))
                if all(element_x_neg == '\u26ab' for element_x_neg in ready_to_flip_values_x_neg):
                    for t_x_neg in ready_to_flip_x_neg:
                        self.flip_cell(t_x_neg[0],t_x_neg[1])
                else:
                    break
        
        for tuple in white:
            delta_x = i_input - tuple[0]
            delta_y = j_input - tuple[1]
            # print(delta_x)
            if delta_y == 0 and delta_x < 0:
                ready_to_flip_y_pos = []
                ready_to_flip_values_y_pos = []
                for i_1 in range(1,abs(delta_x)):
                    ready_to_flip_y_pos.append((tuple[0] - i_1, tuple[1]))
                for t_y_pos in ready_to_flip_y_pos:
                    ready_to_flip_values_y_pos.append(self.get_cell(t_y_pos[0],t_y_pos[1]))
                if all(element_y_pos == '\u26aa' for element_y_pos in ready_to_flip_values_y_pos):
                    for t_y_pos in ready_to_flip_y_pos:
                            self.flip_cell(t_y_pos[0],t_y_pos[1])
                else:
                    break      
            elif delta_x > 0 and delta_y == 0:
                ready_to_flip_y_neg = []
                ready_to_flip_values_y_neg = []
                for i_1 in range(1,abs(delta_x)):
                    ready_to_flip_y_neg.append((tuple[0] + i_1, tuple[1]))
                for t_y_neg in ready_to_flip_y_neg:
                    ready_to_flip_values_y_neg.append(self.get_cell(t_y_neg[0],t_y_neg[1]))
                if all(element_y_neg == '\u26aa' for element_y_neg in ready_to_flip_values_y_neg):
                    for t_y_neg in ready_to_flip_y_neg:
                            self.flip_cell(t_y_neg[0],t_y_neg[1])
                else:
                    break
        self.display()

    #method input coordinates of the next move
    def input_coordinates(self, list_of_valid_moves):
        string_input = input( 'write down the row and column without any space (example: 5B )')
        # while True:
        #     print(string_input[0])
        #     print(type(string_input[0]))
        #     if string_input[0] not in list('12345678'):
        #         print('choix incorrect, recommence')
        #         break
            # if not string_input[1] in list('ABCDEFGH'):
                # break
        row_input = int(string_input[0])-1 #indexation entre 0 et 1
        col_input = string_input[1].upper()
        col_input = list('ABCDEFGH').index(col_input) #indexation entre 0 et 1
        tuple_input = (row_input, col_input)
        print('Requested move:', tuple_input)
        # print(self.valid_moves_black())
        boolean_to_return = tuple_input in list_of_valid_moves
        return [boolean_to_return, tuple_input]





if __name__ == '__main__':

    matrix = Rules(8,8)

    matrix.set_cell('\u26aa',4,4) #white
    matrix.set_cell('\u26aa',3,3) #white
    matrix.set_cell('\u26ab',3,4) #black
    matrix.set_cell('\u26ab',4,3) #black
    print('black = \u26aa')
    print('white = \u26ab')
    print('valid move = \u2705')

    current_color = '\u26ab'  # noirs
    list_of_valid_moves_black = matrix.valid_moves_black()
    if len(list_of_valid_moves_black) > 0:
        print("Black player can play")
        # while True:
        input_data = matrix.input_coordinates(list_of_valid_moves_black)[1]
        # bool_input_data = matrix.input_coordinates(list_of_valid_moves_black)[0]
            # if not bool_input_data:
            #     break
        print(input_data)
        # if not input[0]:
        #     print('Recommence tout depuis le début')
        coordinates_to_place = input_data
        matrix.set_cell(current_color, coordinates_to_place[0], coordinates_to_place[1])
        matrix.flip_black(coordinates_to_place[0], coordinates_to_place[1])
        matrix.count_points()
        


    matrix.cleaning()
    matrix.display()
    current_color = '\u26aa'  #white
    list_of_valid_moves_white = matrix.valid_moves_white()
    if len(list_of_valid_moves_white) > 0:
        print("White player can play")
        input_data = matrix.input_coordinates(list_of_valid_moves_white)[1]
        print(input_data)
        coordinates_to_place = input_data
        matrix.set_cell(current_color, coordinates_to_place[0], coordinates_to_place[1])
        matrix.flip_white(coordinates_to_place[0], coordinates_to_place[1])
        matrix.count_points()

    matrix.cleaning()
    matrix.display()
    current_color = '\u26ab'  # noirs
    list_of_valid_moves_black = matrix.valid_moves_black()
    if len(list_of_valid_moves_black) > 0:
        print("Black player can play")
        input_data = matrix.input_coordinates(list_of_valid_moves_black)[1]
        print(input_data)
        coordinates_to_place = input_data
        matrix.set_cell(current_color, coordinates_to_place[0], coordinates_to_place[1])
        matrix.flip_black(coordinates_to_place[0], coordinates_to_place[1])
        matrix.count_points()

    matrix.cleaning()
    matrix.display()
    current_color = '\u26aa'  #white
    list_of_valid_moves_white = matrix.valid_moves_white()
    if len(list_of_valid_moves_white) > 0:
        print("White player can play")
        input_data = matrix.input_coordinates(list_of_valid_moves_white)[1]
        print(input_data)
        coordinates_to_place = input_data
        matrix.set_cell(current_color, coordinates_to_place[0], coordinates_to_place[1])
        matrix.flip_white(coordinates_to_place[0], coordinates_to_place[1])
        matrix.count_points()

    matrix.cleaning()
    matrix.display()
    current_color = '\u26ab'  # noirs
    list_of_valid_moves_black = matrix.valid_moves_black()
    if len(list_of_valid_moves_black) > 0:
        print("Black player can play")
        input_data = matrix.input_coordinates(list_of_valid_moves_black)[1]
        print(input_data)
        coordinates_to_place = input_data
        matrix.set_cell(current_color, coordinates_to_place[0], coordinates_to_place[1])
        matrix.flip_black(coordinates_to_place[0], coordinates_to_place[1])
        matrix.count_points()

    matrix.cleaning()
    matrix.display()
    current_color = '\u26aa'  #white
    list_of_valid_moves_white = matrix.valid_moves_white()
    if len(list_of_valid_moves_white) > 0:
        print("White player can play")
        input_data = matrix.input_coordinates(list_of_valid_moves_white)[1]
        print(input_data)
        coordinates_to_place = input_data
        matrix.set_cell(current_color, coordinates_to_place[0], coordinates_to_place[1])
        matrix.flip_white(coordinates_to_place[0], coordinates_to_place[1])
        matrix.count_points()
        

    print("Game Over!")