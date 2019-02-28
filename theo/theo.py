"""
Google Hash Code 2019
Author: T.T. Ouzounellis Kavlakonis
Date: 28 Feb 2019
"""
#create function to read input data
def initialize():
    #declare empty dictionary to hold input data
    inputData = {}
    #open the input file for reading
    filename = "C:\\Users\\Theodore\\Documents\\Coding Projects\\Google-Hash-Code-2019\\theo\\a_example.txt"
    inputFile = open(filename,"r")
    inputData["N"] = int(inputFile.readline())

    #get input data for each pictures
    for i in range(inputData["N"]):
        picData = inputFile.readline().rstrip('\n')
        picDataList = picData.split(" ")
        inputData[str(i)]=picDataList

    #create empty arrays to hold id's of horizontally and vertically oriented pictures
    picturesH = []
    picturesV = []
    for pictureNo in range(inputData["N"]):
        if inputData[str(pictureNo)][0] == 'H':
            picturesH.append(pictureNo)
        else:
            picturesV.append(pictureNo)

    #create new dictionary to hold list of tags
    pictureTags={}
    for pictureNo in range(inputData["N"]):
        pictureTags[str(pictureNo)] = inputData[str(pictureNo)][2:]

