def interest_factor_func(tags_1, tags_2):
    """ CREATES INTEREST FACTOR FROM THE TAG LISTS OF THE TWO SLIDE CANDIDATES """
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

