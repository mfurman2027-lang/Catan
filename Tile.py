from Board import TileTypes
# brick orange 1
# wood green 2
# ore purple 3
# sheep lime 4
# wheat yellow 5
# desert tan 6

# types of tiles
# forest 4, pasture 4, field 4, mountain 3, hill 3, desert 1

class Tile:
    positionDict = {}

    def __init__(self, pos, type):
        self.type = type
        self.image = f"CatanPictures\\Tiles\\{type}Tile.png"

class Edge:
    def __init__(self):
        return
        

class Vertex:
    def __init__(self):
        return


