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
            counted_dict[key] /= float(total_num_word)
            counted_dict[key] +=1
    return counted_dicts

'''
    Find which data set that input might be in?
    inp = input text
    prob_dicts = list of probability dictionary
    total_num_word = total number of word in two data sets
    num_word_lists = list of number of word in each data sets
    return index of data set that input might be in
'''
def where(inp,prob_dicts,total_num_word,num_word_lists) :
    #Split input into individual word as list
    list_word = inp.split()
    #List of calculated probability of each data sets
    prob_values = [0]*len(prob_dicts)
    #Iterate on dictionary of probability
    for i in range(0,len(prob_dicts)) :
        #Calculate probability of each data set
        prob = num_word_lists[i]/float(total_num_word)
        #Iterate on each word in input
        for word in list_word :
            #Product probability to total
            if word in prob_dicts[i] :
                prob *= prob_dicts[i][word]
        prob_values[i] = prob
    #Find the best answer by most probability
    current_prob = 0
    ans = -1
    for i in range(0,len(prob_values)) :
        if prob_values[i] > current_prob :
            current_prob = prob_values[i]
            ans = i
    return ans

if __name__ == '__main__':

    #Count word from each data set
    sci_result = read_dict_from_dir("sci.electronics")
    comp_result = read_dict_from_dir("comp.windows.x")

    #sum total word from two data set
    total_num_word = sci_result[1]+comp_result[1]

    #calculate probability
    prob_dicts = calculate_prob([sci_result[0],comp_result[0]],total_num_word)

    #Sample input from 64830 in comp.windows.x
    input = "Your entry need not do well under all, or in most tests.  In certain X    cases, a test is not important.  Entries that compete for the X    'strangest/most creative source layout' need not do as well as X   others in terms of their algorithm."
    ans = where(input,prob_dicts,total_num_word,[sci_result[1],comp_result[1]])

    #Show answer
    if ans == 1 :
        print ("comp.windows.x")
    elif ans == 0 :
        print ("sci.electronics")
    else :
        print ("No data set")
