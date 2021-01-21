# IDEA: Make it generate string polynomials
# Optimization: If we are only interested in the nth row, delete rows as you go

def pascalPyramid(n = 1):
    pyramid = [[1]]
    for i in range(1, n):
        pyramid.append(generateNextRow(pyramid[i - 1]))
    return pyramid

def generateNextRow(lastRow) -> [int]:
    nextRow = [1]
    for i in range(0, len(lastRow)):
        if i == len(lastRow) - 1:
            break
        nextRow.append(lastRow[i] + lastRow[i + 1])
    nextRow.append(1)
    return nextRow


def printPyramid(pyramid):
    for row in pyramid:
        print(row)


printPyramid(pascalPyramid(11))