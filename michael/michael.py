def interest_factor_func(tags_1, tags_2):
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
    

def find_common_tags(tags_current, H):
    global inputData
    
    H_with_common_tags = []
    # tags_current is a list of the tags of the current slide
    
    for index in H:
        
        for tag in tags_current:
            
            if tag in inputData[index]: # assuming tag isn't H or a number
                
                H_with_common_tags.append(index)
                
    return H_with_common_tags

