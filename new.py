import csv
file_name = 'anagrams.csv'
list_words = []


def is_anagram(str1, str2):
    temp1 = str1
    temp2 = str2
    if str1 == str2:
        return False
    """list_str1 = list(temp1)
    list_str1.sorted()
    list_str2 = list(temp2)
    list_str2.sorted()"""
    return (sorted(str1) == sorted(str2))

    #return (list_str1 == list_str2)


def read_file():
    with open(file_name, 'r', newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            list_words.append(str(row))

        for word1 in list_words:
            for word2 in list_words:
                if is_anagram(word1, word2):
                    print(word1, word2)


read_file()
"""
"""