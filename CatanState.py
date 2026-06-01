from Player import Player
from Board import Board
from enum import Enum


class Color(Enum):
    RED = 0
    BLUE = 1
    ORANGE = 2
    WHITE = 3

class CatanState:
# only handles game, does not interfere with display
    def __init__(self, numOfPlayers):
        self.board = Board()
        self.players = CatanState.makePlayers(numOfPlayers) 
        #self.turn

    def makePlayers(num):
        playerList = []
        
        for player in range(num):
            newPlayer = Player(Color(player), 5, 4, 15)
            playerList.append(newPlayer)

        return playerList
