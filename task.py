#spec6

dict_file = open("./Downloads/dictionary-data.csv", "r", encoding="UTF-8")
dict_line = dict_file.read()
word_list = dict_line.split(",")
id_dict = dict()

id = 0
for word in word_list:
    id += 1
    id_dict[id] = word

user_input = input("辞書IDを入力してください：")
if user_input != "":
    id_num = int(user_input)
    term = id_dict[id_num]
    print(f"{id_num}:{term}")
else:
    for id_num in id_dict:
        term = id_dict[id_num]
        print(f"{id_num}:{term}")
dict_file.close()
