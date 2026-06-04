from Tile import Tile, TileTypes
import random

class Board:
    PieceList = []

    def __init__(self):
        self.tileList = Board.makeBoard()
    
    def placePiece(self, pieceType, spot, color):
        return
        #if (self.isValidMove(pieceType, spot, color)):
        #    PieceList[spot] = Piece(color)
        #    return
        #else:
        #    return
        
    def grabBoard(self):
        return
        #return [TileList, PieceList]
        
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

testBoard = Board()
for tile in testBoard.tileList:
    print(tile.type)