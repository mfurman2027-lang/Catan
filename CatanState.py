from Player import Player
from Board import Board
from Piece import Color


class CatanState:
# only handles game, does not interfere with display
    def __init__(self, numOfPlayers):
        self.board = Board()
        self.players = CatanState.makePlayers(numOfPlayers) 
        #self.turn

    def makePlayers(num):
        playerList = []
        
        for player in range(num):
            newPlayer = Player(Color(player), 5, 4, 15, [])
            playerList.append(newPlayer)

        return playerList
