import random
import time

# Generating the game state

gameMatrix = []
x = 40
y = 40

ALIVE = " ⬢ "
DEAD = "   "

upperBound = 10

for i in range(y):
    row = []
    for j in range(x):
        if random.randint(0, upperBound) == 0:
            row.append(ALIVE)
        else:
            row.append(DEAD)
    gameMatrix.append(row)


def printGameState(matrix):
    print("\n" * 10)
    for row in matrix:
        for cell in row:
            print(cell, end="")
        print()

def updateGameState(matrix):
    newMatrix = matrix
    for yCoord in range(y):
        for xCoord in range(x):

            cell = matrix[yCoord][xCoord]
            surroundingCellTally = 0

                surroundingCellTally += 1 if matrix[yCoord - 1][xCoord] == ALIVE else 0
            if yCoord != y - 1:
                surroundingCellTally += 1 if matrix[yCoord + 1][xCoord] == ALIVE else 0
            if xCoord != 0:
                surroundingCellTally += 1 if matrix[yCoord][xCoord - 1] == ALIVE else 0
            if xCoord != x - 1:
                surroundingCellTally += 1 if matrix[yCoord][xCoord + 1] == ALIVE else 0

            if yCoord != 0 and xCoord != 0:
                surroundingCellTally += 1 if matrix[yCoord - 1][xCoord - 1] == ALIVE else 0
            if yCoord != 0 and xCoord != x - 1:
                surroundingCellTally += 1 if matrix[yCoord - 1][xCoord + 1] == ALIVE else 0
            if yCoord != y - 1 and xCoord != 0:
                surroundingCellTally += 1 if matrix[yCoord + 1][xCoord - 1] == ALIVE else 0
            if yCoord != y - 1 and xCoord != x - 1:
                surroundingCellTally += 1 if matrix[yCoord + 1][xCoord + 1] == ALIVE else 0
            
            if cell == ALIVE:
                if surroundingCellTally < 2 or surroundingCellTally > 3:
                    newMatrix[yCoord][xCoord] = DEAD
            elif cell == DEAD:
                if surroundingCellTally == 3:
                    newMatrix[yCoord][xCoord] = ALIVE
    return matrix



            
printGameState(gameMatrix) # initial state
time.sleep(2)


i = 0
limit = 100

while i < limit:

    gameMatrix = updateGameState(gameMatrix)
    printGameState(gameMatrix)

    i += 1
    time.sleep(.5)
    



