import random
import time



class Being:

    ALIVE = " ⬢ "
    DEAD = "   "

    def __init__(self, kind=Being.DEAD):
        self.kind = kind

    def isDead(self):
        return self.kind == Being.DEAD


class GameMatrix:
    matrix = []

    def __init__(self, ySize=0, xSize=0):
        row = []
        for _ in range(ySize):
            row = []
            for _ in range(xSize):
                row.append(Being())
            self.matrix.append(row)


class Game:
    
    @staticmethod
    def printState():
        pass

    @staticmethod
    def updateState():
        pass

    @staticmethod
    def run():
        pass