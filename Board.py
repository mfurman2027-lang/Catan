from Tile import TileTypes, Tile, Edge, Vertex
import random

class Board:
    def __init__(self):
        self.tileDict = Board.makeBoard()
        self.vertDict = Board.addVerts()
        self.edgeDict = Board.addEdges()

        self.setUpTiles()

    def setUpTiles(self):
        return
        #self.tileDict[0].edgeList = [self.edgeDict[], ]
        #sel

    def addEdges():
        edgeDict = {}

        for i in range(72):
            newEdge = Edge()
            edgeDict[i] = newEdge

        return edgeDict

    def addVerts():
        vertDict = {}

        for i in range(54):
            newVertex = Vertex()
            vertDict[i] = newVertex
        
        return vertDict
        
    def makeBoard():
        tileDict = {}
        
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
                newTile = Tile(randomType, 7)
            else:
                randomProb = random.choice(allNums)
                allNums.pop(allNums.index(randomProb))

                newTile = Tile(randomType, randomProb)
            
            tileDict[i] = newTile

        return tileDict

testBoard = Board()
print(testBoard.edgeDict[0])