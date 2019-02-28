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
                max_score_id = slide_id_list # Need to make sure no repeated id.

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
