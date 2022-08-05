#spec1
#print('上手')

#spec5
with open("/Users/名前/Downloads/dictionary-data.txt") as dictionary_file:
    dictionary = dictionary_file.read()
    word_list = dictionary.split("\n")
    id_by_word = dict()
    for id in range(len(word_list)):
        id_by_word[id] = word_list[id]
    
    input_id = int(input())
    if input != "":
        print("{}: {}".format(input_id, id_by_word[input_id]))
    else:
        for term in id_by_word.items():
            print("{}: {}".format(term[0], term[1]))
