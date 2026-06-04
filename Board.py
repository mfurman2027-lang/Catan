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
    TileList = []
    PieceList = []
    def __init__(self):
        self.tileList = Board.makeBoard()
    
    def placePiece(self, pieceType, spot, color):
        if (self.isValidMove(pieceType, spot, color)):
            PieceList[spot] = Piece(color)
            return
        else:
            return
    def grabBoard(self):
        return [TileList, PieceList]
        
    def makeBoard():
        tileList = []
        
        allTiles = [TileTypes.FOREST, TileTypes.FOREST, TileTypes.FOREST, TileTypes.FOREST, 
                    TileTypes.PASTURE, TileTypes.PASTURE, TileTypes.PASTURE, TileTypes.PASTURE, 
                    TileTypes.FIELD, TileTypes.FIELD, TileTypes.FIELD, TileTypes.FIELD, 
                    TileTypes.MOUNTAIN, TileTypes.MOUNTAIN, TileTypes.MOUNTAIN, 
                    TileTypes.HILL, TileTypes.HILL, TileTypes.HILL,
                    TileTypes.DESERT]

        for i in range(19):
            randomType = random.choice(allTiles)
            newTile = Tile(i, randomType)
            tileList.append(newTile)
            allTiles.pop(allTiles.index(randomType))

        return tileList
