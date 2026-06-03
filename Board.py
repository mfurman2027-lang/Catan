from Tile import Tile
import random
from enum import Enum


class TileTypes(Enum):
    FOREST = 0
    PASTURE = 1
    FIELD = 2
    MOUNTAIN = 3
    HILL = 4
    DESERT = 5


class Board:
    def __init__(self):
        til0 = Tile(0)
    
    def placePiece(self, pieceType, spot):
    
    def grabBoard(self):
        #return [tileList, pieceList]
        return
        
    def makeBoard(self):
        tileList = []
        
        allTiles = [TileTypes.FOREST, TileTypes.FOREST, TileTypes.FOREST, TileTypes.FOREST, 
                    TileTypes.PASTURE, TileTypes.PASTURE, TileTypes.PASTURE, TileTypes.PASTURE, 
                    TileTypes.FIELD, TileTypes.FIELD, TileTypes.FIELD, TileTypes.FIELD, 
                    TileTypes.MOUNTAIN, TileTypes.MOUNTAIN, TileTypes.MOUNTAIN, 
                    TileTypes.DESERT]

        for i in range(19):
            randomTile = random.choice(allTiles)
            tileList.append(randomTile)
            allTiles.pop(allTiles.index(randomTile))

        return tileList