#MAIN PROGRAM FILE
import numpy as np
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

def interest_factor_func(index_1, index_2):
    """ CREATES INTEREST FACTOR FROM THE INDEXES (WHICH MAY BE A TUPLE) OF THE TWO SLIDE CANDIDATES """
    # find tags_1 and tags_2 
    if type(index_1) == int:
        tags_1 = inputData[index_1][2:]
    else:
        tags_1 = inputData[index_1[0]][2:] + inputData[index_1[1]][2:]
    
    if type(index_2) == int:
        tags_2 = inputData[index_2][2:]
    else:
        tags_2 = inputData[index_2[0]][2:] + inputData[index_2[1]][2:]
        
        
    interest_factor_1 = set(tags_1 + tags_2)   # Common tags
    intersect = tags_1 + tags_2
    for tag in interest_factor_1:
        intersect.remove(tag)
    
    interest_factor_2 = tags_1
    interest_factor_3 = tags_2
    for tag in intersect:
        interest_factor_2.remove(tag)
        interest_factor_3.remove(tag)
        
    return min([len(interest_factor_1), len(interest_factor_2), len(interest_factor_3)])
    






def find_common_tags(tags_current, INDEXES): # INDEXES represents every available slide that can occur =>> a tuple represents a pair of pictures for a vertical picture
    """ TAKES LIST OF INDEXES OF PHOTOS (INC TUPLES REPRESENTING VERTICAL SLIDES)
    AND THE CURRENT TAGS AND RETURNS A LIST OF INDEXES WHICH HAVE A TAG IN COMMON """
    global inputData
    
    INDEXES_with_common_tags = []
    # tags_current is a list of the tags of the current slide
    
    
        
    for tag in tags_current: # for each tag of the current slide
        
        for index in INDEXES:
            
            if type(index) == int:
                
                if tag in inputData[index]: # assuming tag isn't H, V or a number
                    
                    INDEXES_with_common_tags.append(index)
                
            else: # assuming tuple then
                
                for sub_index in index:
                    
                    if tag in inputData[sub_index]: 
                    
                        INDEXES_with_common_tags.append(index)
                    
    return INDEXES_with_common_tags

def slide_combiner(slide_id_list):

    output = [0]

    for i in range(len(slide_id_list)):
        max_score = 0
        max_score_id = None
        for j in range(i+1, len(slide_id_list)):
            score = interest_factor_func(slide_id_list[i], slide_id_list[j])

            if score > max_score:
                max_score = score
                max_score_id = slide_id_list[j] # Need to make sure no repeated id.

        output.append(max_score_id)
    
    return output

def slide_combiner_2(slide_id_list):

    output = [0]

    for i in range(len(slide_id_list)):
        max_score = 0
        max_score_id = None
        compatible_slides = find_common_tags(slide_id_list[i])
        slide_score_dict = {}
        for j in range(len(compatible_slides)):
            
            if compatible_slides[j] in output:
                pass

            else:
                score = interest_factor_func(slide_id_list[i], compatible_slides[j])

                if score > max_score:
                    max_score = score
                    max_score_id = compatible_slides[j]
                
        output.append(max_score_id)
    
    return output


def output_file(output):

    with open("output.txt", 'w') as fileout:
        for i in output:
            if type(i) == list:
                fileout.write("{} {}\n".format(i[0], i[1]))

            else:
                fileout.write("{}\n".format(i))

        
        fileout.close()