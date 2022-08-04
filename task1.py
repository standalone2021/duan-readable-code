#spec1
#print('上手')

#spec5
with open("/Users/名前/Downloads/dictionary-data.txt") as dictionary_file:
    dictionary = dictionary_file.read()
    word_list = dictionary.split("\n")
    for id in range(len(word_list)):
        print("{}: {}".format(id, word_list[id]))
