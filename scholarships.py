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
    directions = [(1, 0,numCols), (0, 1,numRows), (1, 1,numDiagonals)] #list containing protocol for iterating through lines based on direction
    for i in range(len(directions)):
        numLines = directions[i][2] #Set numLines based on the current direction 
        for line in range (0,numLines):
            pathProduct = 1
            pathLen = 0
            if i == 0: #iterate through columns
                headRow = 0 #reset the start of the path to the first row
                headCol = line #reset the start of the path to the current column
            elif i ==1:#iterate through rows
                headCol = 0
                headRow = line
            else:#iterate through diagonals
                headRow =  0 if line  >= numRows else line #if all diagonal paths have been considered in bottom half of matrix, reset row start to the first row
                headCol =  line-numRows if line  >= numRows else 0 #if all diagonal paths have been considered in bottom half of matrix, reset column for each unexplored diagonal
            tailRow = headRow
            tailCol = headCol
            pathList = []
            while headRow < numRows  and headCol < numCols: #iterate while the current column and row are inside the matrix
                pathList.append(matrix[headRow][headCol]) #add current element to the current path
                pathProduct *= matrix[headRow][headCol] #accumulate the product
                pathLen+=1
                if pathLen > maxLen: 
                    pathProduct /= matrix[tailRow][tailCol] #if current pathLen is greater than maxLen, shave off first element
                    pathList = pathList[1:]
                    tailRow += directions[i][0] #move beginning (tail) of path by one
                    tailCol += directions[i][1]
                if pathProduct > maxProduct: #if current pathProduct is best seen so far, update max value
                    maxProduct = pathProduct
                    maxList = pathList
                headRow += directions[i][0] #move end (head) of path by one
                headCol += directions[i][1]
                
    return maxProduct, maxList

matrix = [[1,2,3,4,5], [1,1,2,3,5], [3,4,5,5,5], [3,4,5,9,5], [1,1,5,5,25]]

print maxPathProduct(matrix,3)
