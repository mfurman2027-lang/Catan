from Player import Player
from enum import Enum


class Color(Enum):
    RED = 1
    BLUE = 2
    ORANGE = 3
    WHITE = 4

class CatanState:
# only handles game, does not interfere with display
    def __init__(self, numOfPlayers):
        self.board = Board()
        self.players = CatanState.makePlayers(numOfPlayers) 
        self.turn

    def makePlayers(num):
        playerList = []
        
        for player in range(num):
            newPlayer = Player(Color(player))
            playerList.append(newPlayer)

        return playerList
