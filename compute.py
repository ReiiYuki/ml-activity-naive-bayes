import os,json

def read_dict_from_dir(dir) :
    word_list = dict()
    num_word = 0
    for filename in os.listdir(dir) :
        with open(dir+"/"+filename) as data :
            for part in json.load(data)["sentences"] :
                for token in part["tokens"] :
                    if token["word"] in word_list :
                        word_list[token["word"]] += 1
                    else :
                        word_list[token["word"]] = 1
                    num_word += 1
    return (word_list,num_word)

def calculate_prob(counted_dict,num_word) :
    for key in counted_dict :
        counted_dict[key] /= float(num_word)
    return counted_dict

result = read_json("sci.electronics")

result = calculate_prob(result[0],result[1])

for key in result :
    print (result[key])
