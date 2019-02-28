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
    
tags_1 = [1,2,3,7,4,5,6]
tags_2 = [2,3,7,8]
print(interest_factor_func(tags_1, tags_2))