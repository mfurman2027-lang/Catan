from enum import Enum

# brick orange 1
# wood green 2
# ore purple 3
# sheep lime 4
# wheat yellow 5
# desert tan 6

# types of tiles
# forest 4, pasture 4, field 4, mountain 3, hill 3, desert 1

class TileTypes(Enum):
    FOREST = 0
    PASTURE = 1
    FIELD = 2
    MOUNTAIN = 3
    HILL = 4
    DESERT = 5

class Tile:
    positionDict = {}

    def __init__(self, type, number):
        self.number = number
        self.type = type
        self.image = f"CatanPictures\\Tiles\\{type.name}.png"
        self.edgeList = []
        self.vertexList = []

class Edge:
    def __init__(self):
        return
        

class Vertex:
    def __init__(self):
        return


