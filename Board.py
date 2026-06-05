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

        allNums = [12, 11, 11, 10, 10, 9, 9, 8, 8, 6, 6, 5, 5, 4, 4, 3, 3, 2]

        for i in range(19):
            randomType = random.choice(allTiles)
            allTiles.pop(allTiles.index(randomType))
            newTile = None

            if randomType == TileTypes.DESERT:
                newTile = Tile(i, randomType, 7)
            else:
                randomProb = random.choice(allNums)
                allNums.pop(allNums.index(randomProb))

                newTile = Tile(i, randomType, randomProb)
            
            tileList.append(newTile)

        return tileList

testBoard = Board()
for tile in testBoard.tileList:
    print(f"type {tile.type} and prob {tile.prob}")