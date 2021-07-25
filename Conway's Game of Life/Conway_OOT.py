import random
import time


class Being:

    ALIVE = " ⬢ "
    DEAD = "   "

    def __init__(self, kind=DEAD):
        self.kind = kind

    def isDead(self):
        return self.kind == Being.DEAD

    def isAlive(self):
        return self.kind == Being.ALIVE

    def kill(self):
        self.kind = Being.DEAD
    
    def revive(self):
        self.kind = Being.ALIVE



class GameMatrix:

    matrix = []

    def __init__(self, ySize=0, xSize=0):
        self.ySize = ySize
        self.xSize = xSize
        for _ in range(ySize):
            row = []
            for _ in range(xSize):
                row.append(Being())
            self.matrix.append(row)


    def randomize(self, bound=10):
        for row in self.matrix:
            for being in row:
                being.revive() if random.randint(0, bound) == 0 else being.kill()



class Game:
    
    def __init__(self, gameMatrix):
        self.gameMatrix = gameMatrix
        

    def printState(self):
        print(len(self.gameMatrix))
        exit()
        for row in self.gameMatrix.matrix:
            for cell in row:
                print(cell.kind, end="")
            print()


    def updateState(self):
        newMatrix = self.gameMatrix.matrix
        x = self.gameMatrix.xSize
        y = self.gameMatrix.ySize
        for yCoord in range(y):
            for xCoord in range(x):

                cell = newMatrix[yCoord][xCoord]
                surroundingCellTally = 0
                
                surroundingCellTally += 1 if newMatrix[yCoord - 1][xCoord].isAlive() else 0
                if yCoord != y - 1:
                    surroundingCellTally += 1 if newMatrix[yCoord + 1][xCoord].isAlive() else 0
                if xCoord != 0:
                    surroundingCellTally += 1 if newMatrix[yCoord][xCoord - 1].isAlive() else 0
                if xCoord != x - 1:
                    surroundingCellTally += 1 if newMatrix[yCoord][xCoord + 1].isAlive() else 0

                if yCoord != 0 and xCoord != 0:
                    surroundingCellTally += 1 if newMatrix[yCoord - 1][xCoord - 1].isAlive() else 0
                if yCoord != 0 and xCoord != x - 1:
                    surroundingCellTally += 1 if newMatrix[yCoord - 1][xCoord + 1].isAlive() else 0
                if yCoord != y - 1 and xCoord != 0:
                    surroundingCellTally += 1 if newMatrix[yCoord + 1][xCoord - 1].isAlive() else 0
                if yCoord != y - 1 and xCoord != x - 1:
                    surroundingCellTally += 1 if newMatrix[yCoord + 1][xCoord + 1].isAlive() else 0
                
                if cell.isAlive():
                    if surroundingCellTally < 2 or surroundingCellTally > 3:
                        newMatrix[yCoord][xCoord].kill()
                elif cell.isDead():
                    if surroundingCellTally == 3:
                        newMatrix[yCoord][xCoord].revive()
        return newMatrix


    def run(self, limit=100):
        i = 0
        while i < limit:
            self.gameMatrix = self.updateState()
            self.printState()

            i += 1
            time.sleep(.5)


# Implementation

matrix = GameMatrix(50, 50)
matrix.randomize

game = Game(matrix)
game.run()
