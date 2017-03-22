def maxPathProduct(matrix, maxLen):
    """
    Take a 2D Array of ints
    and return the largest Product of list of ints of length maxLen
    and the product of the list integers
    """ 
    maxProduct = -1
    maxList = [] 
    if len(matrix) == 0 or len(matrix) < maxLen and len(matrix[0]) < maxLen:
        return maxProduct, maxList
    numRows = len(matrix)
    numCols = len(matrix[0])
    numDiagonals = numRows + numCols -1
    directions = [(1, 0,numCols), (0, 1,numRows), (1, 1,numDiagonals)]
    
    for i in range(len(directions)):
        #Set numLines based on the current direction 
        numLines = directions[i][2]

        for line in range (0,numLines):
            pathProduct = 1
            pathLen = 0
            if i == 0:
                headRow = 0
                headCol = line
            elif i ==1:
                headCol = 0
                headRow = line
            else:
                headRow =  0 if line  >= numRows else line
                headCol =  line-numRows if line  >= numRows else 0
            tailRow = headRow
            tailCol = headCol
            pathList = []
            while headRow < numRows  and headCol < numCols:
                pathList.append(matrix[headRow][headCol])
                pathProduct *= matrix[headRow][headCol]
                pathLen+=1
                if pathLen > maxLen:
                    pathProduct /= matrix[tailRow][tailCol]
                    pathList = pathList[1:]

                    tailRow += directions[i][0]
                    tailCol += directions[i][1]
                    # if direction== 1:
                    #     tailRow += 1
                    # elif direction == 2:
                    #     tailCol += 1
                    # elif direction == 3:
                    #     tailCol += 1
                    #     tailRow += 1
                if pathProduct > maxProduct:
                    maxProduct = pathProduct
                    maxList = pathList
                headRow += directions[i][0]
                headCol += directions[i][1]
                # if direction== 1:
                #         headRow += 1
                # elif direction == 2:
                #     headCol += 1
                # elif direction == 3:
                #     headCol += 1
                #     headRow += 1
        return maxProduct, maxList
matrix = [[1,2,3,4,5], [1,1,2,3,5], [3,4,5,5,5], [3,4,5,9,5], [1,1,5,5,25]]

print maxPathProduct(matrix,3)