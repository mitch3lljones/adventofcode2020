import numpy as np

def processFile():
    arr = np.array([])
    file = open("input.txt", "r")
    lines = file.readlines()

    for line in lines:
        arr = np.append(arr, int(line))

    file.close()
    return arr

def findTwoEntries():
    arrayOfValues = processFile()
    index1 = 0
    index2 = 0
    for i in range(len(arrayOfValues)):
        for j in range(len(arrayOfValues)):
            if i != j:
                if arrayOfValues[i] + arrayOfValues[j] == 2020:
                    index1 = i
                    index2 = j
                    break
    answer = arrayOfValues[index1] * arrayOfValues[index2]
    print(answer)

def findThreeEntries():
    arrayOfValues = processFile()
    index1 = 0
    index2 = 0
    index3 = 0
    for i in range(len(arrayOfValues)):
        for j in range(len(arrayOfValues)):
            for k in range(len(arrayOfValues)):
                if i != j and j != k and i != k:
                    if arrayOfValues[i] + arrayOfValues[j] + arrayOfValues[k] == 2020:
                        index1 = i
                        index2 = j
                        index3 = k
                        break
    answer = arrayOfValues[index1] * arrayOfValues[index2] * arrayOfValues[index3]
    print(answer)

findTwoEntries()
findThreeEntries()