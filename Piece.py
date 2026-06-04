from enum import Enum

class Color(Enum):
    RED = 0
    BLUE = 1
    ORANGE = 2
    WHITE = 3

class Piece:
    Color = 0
    def __init__(self, color):
        Color = color
        return