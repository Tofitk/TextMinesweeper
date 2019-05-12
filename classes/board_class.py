import random

class Board():
    """the class for the board.
    self variables
    height: the height of the board
    lenght: the lenght of the board
    mines: the amount of mines
    remaining_mines: a variable to handle the remaining mines for victory calculation
    board: we save the array of tile member coordinates here
    functions
    get_surroundings_mines: counts the amount of bombs next to the tile
    get_surroundings_coords: gets the coordinates for the tiles next to the picked tile
    is_in_play_area: used to ignore tiles that do not exist on the playing board
    place_the_mines: places the mines on the board
    input_validity: here we check the validity of the user inputed move
    reveal_tile: here we check if the revealed tile is a mine and reveal it, if its a mine we end the game
    flag_tile: here we flag a tile
    deflag_tile: here we deflag a tile
    check_victory: here we check if you win every time after you do a move
    """
    def __init__(self, height, lenght,mines,board):
        self.height = height
        self.lenght = lenght
        self.mines = mines
        self.remaining_mines = mines
        self.board = board
        self.loss = False
        self.victory = False
    
    def __str__(self):
        row_string = "  "
        print("\nRemaining mines: " + str(self.mines)+"\n")
        for i in range(0,self.lenght):
            row_string += str(i)
        row_string += "\n__"  
        for i in range(0,self.lenght):
            row_string += "_" 
        row_string += "\n" 
        for colum_num in range(0,self.height):
            row_string += str(colum_num) +"|"
            for row_num in range(0,self.lenght):
                if self.board[colum_num][row_num].visible:
                    if self.board[colum_num][row_num].mine:
                        row_string += "M"
                    else:
                        row_string += str(self.board[colum_num][row_num].nearby_mines)
                elif self.board[colum_num][row_num].flagged:
                    row_string += "F"
                else:
                    row_string += "X"
            row_string += "\n"   
        return row_string

    def get_surroundings_mines(self, colum_num, row_num):#checks how many bombs are in the surrounding tiles
        mine_amount = 0
        for (surrounding_colum, surrounding_row) in self.get_surroundings_coords(colum_num,row_num):
            if self.is_in_play_area(surrounding_colum, surrounding_row) and self.board[surrounding_colum][surrounding_row].mine:
                mine_amount += 1
        self.board[colum_num][row_num].nearby_mines_update(mine_amount)
        return mine_amount
    
    def get_surroundings_coords(self, colum_num, row_num): #gets the coordinates for the tiles next to the one we picked
        surrounding_coordinates = ([-1,-1],[-1,0],[-1,1],
                                   [0,-1],       [0,1],
                                   [1,-1],[1,0],[1,1])#written in this way as it is easier to grasp what the tupels represent
        surrounding_tiles = []
        for [surrounding_colum, surrounding_row] in surrounding_coordinates:
            if not (colum_num+surrounding_colum < 0 or colum_num+surrounding_colum >= self.height or row_num+surrounding_row < 0 or row_num+surrounding_row >= self.lenght):
                surrounding_tiles.append([colum_num+surrounding_colum, row_num+surrounding_row])
        return surrounding_tiles
        
    def is_in_play_area(self,colum_num,row_num):#checks if the tile we are looking at is in the play area
        if colum_num < self.height and colum_num >= 0 and row_num < self.lenght and row_num >= 0:
            return True
        else:
            return False

    def place_the_mines(self,start_colum,start_row):
        for i in range (0, self.mines): #places the mines on the array
            while True:
                colum_num = random.randint(0,self.height-1)
                row_num = random.randint(0,self.lenght-1)
                #print(str(colum_num)+" "+str(row_num)) for debugging the random placement func
                if self.board[colum_num][row_num].mine == False and not (colum_num == start_colum and row_num == start_row):
                    self.board[colum_num][row_num].place_mine()
                    break
        for colum in range(0,self.height-1):
            for row in range(0,self.lenght-1):
                self.get_surroundings_mines(colum,row)

    def input_validity(self,move):
        if len(move) == 3:
            colum_num = int(move[0])
            row_num = int(move[1])
            action = move[2]
            if colum_num <= self.height-1 and colum_num >= 0 and row_num <= self.lenght-1 and row_num >= 0:
                if self.board[colum_num][row_num].visible:
                    return False
                elif (action == "f" or action == "F") and self.board[colum_num][row_num].flagged:
                    return False
                elif (action == "d" or action == "D") and not self.board[colum_num][row_num].flagged:
                    return False
                else:
                    return True
            else:
                return False
        else:
            return False

    def reveal_tile(self,colum_num,row_num):
        if self.board[colum_num][row_num].mine:
            self.loss = True
            self.board[colum_num][row_num].reveal()
        else:
            self.board[colum_num][row_num].reveal()
            if self.board[colum_num][row_num].nearby_mines == 0:
                self.surroundings_reveal(colum_num,row_num)

    def surroundings_reveal(self,colum_num,row_num):
        surrounding_tiles = self.get_surroundings_coords(colum_num,row_num)
        for i in range (0,len(surrounding_tiles)):
            if not self.board[surrounding_tiles[i][0]][surrounding_tiles[i][1]].visible and not self.board[surrounding_tiles[i][0]][surrounding_tiles[i][1]].mine:
                print(surrounding_tiles[i][0],surrounding_tiles[i][1])
                self.reveal_tile(surrounding_tiles[i][0],surrounding_tiles[i][1])

    def flag_tile(self,colum_num,row_num):
        self.board[colum_num][row_num].flag()

    def deflag_tile(self,colum_num,row_num):
        self.board[colum_num][row_num].deflag()

    def check_victory(self):
        for i in range(0,self.height-1):
            for j in range(0,self.lenght-1):
                if not self.board[i][j].visible and not self.board[i][j].mine:
                    return False
        self.victory = True
        return True