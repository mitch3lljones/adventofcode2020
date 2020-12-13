import numpy as np

def processFile():
    arr = np.empty((0, 31))
    file = open("trees.txt", "r")

    lines = file.readlines()

    for line in lines:
        lineArray = list(line)
        arrayToAdd = np.array(lineArray)
        arrayToAdd = arrayToAdd[:-1]
        arr = np.vstack([arr,[arrayToAdd]])
    
    return arr

def traverseSlope(arr, rightShift, downShift):
    row = 0
    col = 0
    numTreesHit = 0
    while not row >= len(arr)-1:
        row = row + downShift
        col = col + rightShift
        if col >= len(arr[0]):
            col = col - len(arr[0])
        if arr[row][col] == "#":
            numTreesHit = numTreesHit + 1

    return numTreesHit

mapOfTrees = processFile()
numberTreesHitPart1 = traverseSlope(mapOfTrees, 3, 1)
numberTreesHitPart2 = traverseSlope(mapOfTrees, 1, 1) * traverseSlope(mapOfTrees, 3, 1) * traverseSlope(mapOfTrees, 5, 1) * traverseSlope(mapOfTrees, 7, 1) * traverseSlope(mapOfTrees, 1, 2)
print("Part 1:", numberTreesHitPart1)
print("Part 2:", numberTreesHitPart2)