from Tile import Tile
import random

class Board:
    def __init__(self):
        til0 = Tile(0)
    def placePiece(self, pieceType, spot):
    
    def grabBoard(self):
        return [tileList, pieceList]
        
    def makeBoard(self):
        tileList = []
        tileValues = [4, 1, 4, 4, 3, 3]
        for i in range(19):
            currTileVal = random.randint(0, 5)
            while (tileValues[currTileVal] == 0):
                currTileVal = random.randint(0, 5)
            currTile = Tile(i, currTileVal, random.randint(2, 12))
            tileValues[currTileVal] = tileValues[currTileVal] - 1
            tileList.append(currTile)