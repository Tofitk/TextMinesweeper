class Tile():
    """the class for tiles.
    self variables:
    mine: if its true it means the tile has a mine, if it has no mine its false
    visible: the tiles state, meaning if its revealed (1) or not (0)
    flagged: if the flagged
    nearby_mines: the amount of mines nearby

    functions:
    reveal: the function to swap the state of the tile to be revealed
    flag: the function to swap the state of the tile to be flagged
    place_mine: the function to swap the state of the tile to have a mine
    """
    def __init__(self, has_mine=False, visible=False, flagged=False):
        self.visible = visible
        self.mine = has_mine
        self.flagged = flagged
        self.nearby_mines = 0

    def reveal(self):
        self.visible = True

    def flag(self):
        self.flagged = True

    def deflag(self):
        self.flagged = False

    def place_mine(self):
        self.mine = True
    
    def nearby_mines_update(self, amount):
        self.nearby_mines = amount