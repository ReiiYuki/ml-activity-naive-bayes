import os,json

'''
    Count word from json files in directory
    dir = directory of json file
    ** Make sure only json files are in dir
    ** If exception please check each of your json file if it is correct or not, or try to prettify it
    return tuple(counted word dictionary, number of word)
'''
def read_dict_from_dir(dir) :
    word_list = dict()
    num_word = 0
    #Read File's name from fir
    for filename in os.listdir(dir) :
        #Load Json file as dictionary in Python
        with open(dir+"/"+filename) as data :
            #Iterate on each sentences
            for sentence in json.load(data)["sentences"] :
                #Iterate each word in senteces
                for token in sentence["tokens"] :
                    #Count word
                    if token["word"] in word_list :
                        word_list[token["word"]] += 1
                    else :
                        word_list[token["word"]] = 1
                    #Add number of word
                    num_word += 1
    return (word_list,num_word)

'''
    Calculate probability of each word in data sets
    counted_dicts = counted word dictionaries from data sets
    total_num_word = total number of word in two data set
    return dictionaries of probability of each word in each data sets
'''
def calculate_prob(counted_dicts,total_num_word) :
    #Iterate on each counted word dictionary of each data set
    for counted_dict in counted_dicts :
        #Iterate on each word of each dictionary
        for key in counted_dict :
            #Make it probability
            counted_dict[key] /= float(num_word)
    return counted_dicts

if __name__ == '__main__':
    sci_result = read_dict_from_dir("sci.electronics")
    comp_result = read_dict_from_dir("comp_result")

    # result = calculate_prob([result[0],result[1])
    #
    # for key in result[0] :
    #     print (result[0][key])
