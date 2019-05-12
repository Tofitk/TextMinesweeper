from classes import tile_class, board_class

def create_board(height,lenght, mines): #a function to create the board array
    board_skeleton = []
    for i in range(height): #creates the array of coordinates
        board_skeleton.append([j for j in range(lenght)])
    for i in range(0,height): #adds all the coordinates to be members of Tile
        for j in range(0,lenght):
            board_skeleton[i][j] = tile_class.Tile()
    board = board_class.Board(height,lenght,mines,board_skeleton)
    return board

def user_move(board):
    move = input("enter your move (column row action(r = reveal tile, f = flag tile, d = deflag tile,) example 64r): ")
    while True:
        if board.input_validity(move):
            return (move)
        else:
            move = input("invalid input, try again: ")
