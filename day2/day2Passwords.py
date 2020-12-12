import pandas as pd

def processFile():
    df = pd.DataFrame(columns=['Min_Length', 'Max_Length', 'Required_Char', 'Password'])
    file = open("passwords.txt", "r")

    lines = file.readlines()
    for line in lines:
        lineLength = len(line)
        dashIndex = line.index("-")
        minLength = int(line[:dashIndex])
        firstSpaceIndex = line.find(" ")
        maxLength = int(line[dashIndex+1:firstSpaceIndex])
        requiredChar = line[firstSpaceIndex+1:firstSpaceIndex+2]
        colonIndex = line.index(":")
        password = line[colonIndex+2:lineLength-1]
        rowToAdd = {'Min_Length':minLength, 'Max_Length':maxLength, 'Required_Char':requiredChar, 'Password':password}
        df = df.append(rowToAdd, ignore_index=True)
    return df

def checkPasswordsPartOne(df):
    numberCorrectPasswords = 0
    for i, row in df.iterrows():
       numRequiredCharInstances = row['Password'].count(row['Required_Char'])
       if numRequiredCharInstances >= row['Min_Length'] and numRequiredCharInstances <= row['Max_Length']:
           numberCorrectPasswords = numberCorrectPasswords + 1

    return numberCorrectPasswords

def checkPasswordsPartTwo(df):
    numberCorrectPasswords = 0
    for i, row in df.iterrows():
        password = row['Password']
        if (password[row['Min_Length']-1] == row['Required_Char']) ^ (password[row['Max_Length']-1] == row['Required_Char']):
            numberCorrectPasswords = numberCorrectPasswords + 1

    return numberCorrectPasswords

dfPasswords = processFile()
numCorrectPasswordsOne = checkPasswordsPartOne(dfPasswords)
print(numCorrectPasswordsOne)
numCorrectPasswordsTwo = checkPasswordsPartTwo(dfPasswords)
print(numCorrectPasswordsTwo)