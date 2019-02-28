import numpy as np

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

def slide_combiner_3(slide_id_list):

    # a list of slide ids for output
    output = [0]

    # start with slide 0
    i = 0

    # Iterate through each slide from i=0 and find the most compatible subsequent slide. 
    while(len(slide_id_list) > 0):
        max_score = 0
        max_score_id = None

        # find compatible slides
        compatible_slides = find_common_tags(i)

        # remove compatible slides that are already in output
        compatible_slides = [x for x in compatible_slides not in output]
        
        # Iterate through each compatible slide to find the best one
        for j in range(len(compatible_slides)):
            
            #if compatible_slides[j] in output:
             #   pass

            #else:

            score = interest_factor_func(i, compatible_slides[j])

            # Update max_score_id for the best slide
            if score > max_score:
                max_score = score
                max_score_id = compatible_slides[j]
               
        output.append(max_score_id)
        slide_id_list.remove(max_score_id) 

        i = max_score_id

    return output



def output_file(output):

    with open("output.txt", 'w') as fileout:
        for i in output:
            if type(i) == list:
                fileout.write("{} {}\n".format(i[0], i[1]))

            else:
                fileout.write("{}\n".format(i))

        
        fileout.close()
