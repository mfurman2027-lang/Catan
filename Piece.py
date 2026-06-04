from enum import Enum

class Color(Enum):
    RED = 0
    BLUE = 1
    ORANGE = 2
    WHITE = 3
class PieceType(Enum):
    ROAD = 0
    SETTLE = 1
    CITY = 2
class Piece:
    Color = 0
    PieceType = 0
    def __init__(self, color, pieceType):
        Color = color
        PieceType = pieceType
        return