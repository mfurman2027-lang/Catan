from enum import Enum
class Type(Enum):
    KNIGHT = 1
    ROAD = 2
    PLENTY = 3
    MONOPOLY = 4
    VICTORY = 5
    BRICK = 6
    LUMBER = 7
    WOOL = 8
    GRAIN = 9
    ORE = 10
class Card:
    def __init__(self):
