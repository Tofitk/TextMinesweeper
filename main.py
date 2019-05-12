from classes import board_class, tile_class
from functions import functions

height = int(input("give the height of the playing board (max 10): "))
lenght = int(input("give the lenght of the playing board (max 10): "))
max_mines = str((height * lenght) - 1)
mines = int(input("give the amount of mines you want (max " + max_mines + "): "))
board = functions.create_board(height,lenght,mines)
turn = 0
while not board.loss and not board.victory:
    print(board)
    move = functions.user_move(board)
    if turn == 0:
        board.place_the_mines(int(move[0]),int(move[1]))
        turn += 1
    if move[2] == "f" or move[2] == "F":
        board.flag_tile(int(move[0]),int(move[1]))
    if move[2] == "r" or move[2] == "R":
        board.reveal_tile(int(move[0]),int(move[1]))
        board.check_victory()
    if move[2] == "d" or move[2] == "D":
        board.deflag_tile(int(move[0]),int(move[1]))
print(board)
if board.loss:
    print("You revealed a mine, you die.")
if board.victory:
    print("You win, graz")
