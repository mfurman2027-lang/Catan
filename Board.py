from Tile import Tile

class Board:
    def __init__(self):
        self.tileList = Board.makeTileList()

    def makeTileList():
        resources = []

        for tile in range(19):
            newTile = Tile(tile, )
