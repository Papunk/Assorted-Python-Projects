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
        self.ySize = ySize
        self.xSize = xSize
        for _ in range(ySize):
            row = []
            for _ in range(xSize):
                row.append(Being())
            self.matrix.append(row)



class Game:
    
    def __init__(self, ySize=0, xSize=0):
        self.gameMatrix = GameMatrix(ySize, xSize)
        

    def printState(self):
        for row in self.gameMatrix.matrix:
            for cell in row:
                print(cell.kind, end="")
            print()


    def updateState(self):
        newMatrix = self.gameMatrix.matrix
        for yCoord in range(self.gameMatrix.ySize):
            for xCoord in range(self.gameMatrix.ySize):

        #         
        

    def run(self):
        pass