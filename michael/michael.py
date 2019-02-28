import numpy as np

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
        for index in INDEXES: # and for each index
            if type(index) == int: # if index is int type
                
                if tag in inputData[index][2:]: # test if tag in this indexed photo
                    
                    INDEXES_with_common_tags.append(index)
                
            else: # if index is tuple type
                
                for sub_index in index: # for each index in the double-photo slide

                    if tag in inputData[sub_index][2:]: # test if tag in this indexed photo
                    
                        INDEXES_with_common_tags.append(index)
                    
    return INDEXES_with_common_tags

def produce_referencable_edge_weights_array():
    """ FROM inputData IT PRODUCES A LARGE ARRAY OF THE WEIGHTS OF THE EDGES BETWEEN THE POSSIBLE SLIDES IT CAN GO FROM AND TO! """
    global inputData
    
    N = np.zeros([len(inputData), len(inputData)])
    
    for f, index_from in enumerate(inputData):
        for t, index_to in enumerate(inputData):
            
            N[f, t] = interest_factor_func(index_from, index_to)
            
    return N




