import csv


def main():
    fileName = 'anagrams.csv'
    readFile(fileName)


def isAnagram(str1, str2):
    if str1 == str2:
        return False
    return (sorted(str1) == sorted(str2))


def readFile(fileName):
    listWords = []
    with open(fileName, 'r', newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            listWords.append(str(row))

        for word1 in listWords:
            for word2 in listWords:
                if isAnagram(word1, word2):
                    print(word1, word2)


main()
