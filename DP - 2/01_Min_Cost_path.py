from sys import stdin
MAX_VALUE = 2147483647

def minCostPathHelper(input, mRows, nCols, currRow, currCol) :
    if (currRow >= mRows) or (currCol >= nCols) :
        return MAX_VALUE

        
    if currRow == (mRows - 1) and currCol == (nCols - 1) :
        return input[currRow][currCol]

    downCost = minCostPathHelper(input, mRows, nCols, (currRow + 1), currCol)
    diagonalCost = minCostPathHelper(input, mRows, nCols, (currRow + 1), (currCol + 1))
    leftCost = minCostPathHelper(input, mRows, nCols, currRow, (currCol + 1))

    return input[currRow][currCol] + min(diagonalCost, downCost, leftCost)



def minCostPath(input, mRows, nCols) :
    if mRows == 0 :
        return MAX_VALUE
    
    return minCostPathHelper(input, mRows, nCols, 0, 0)

def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    mRows = int(li[0])
    nCols = int(li[1])
    
    if mRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(mRows)]
    return mat, mRows, nCols


#main
mat, mRows, nCols = take2DInput()
print(minCostPath(mat, mRows, nCols))