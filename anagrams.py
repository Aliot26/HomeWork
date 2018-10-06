import csv
file_name = 'anagrams.csv'
list_words = []
dict_words = {}


def read_file():
    with open(file_name, 'r', newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            list_words.append(row)
        #print(list_words)
        list_words_s = sorted(list_words)
        print(list_words_s)


read_file()
