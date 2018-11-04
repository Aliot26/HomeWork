import sys
import argparse


def main():
    fileName = "ideabank.txt"
    if __name__ == '__main__':
        parser = createParser()
        namespace = parser.parse_args(sys.argv[1:])
    if namespace.list:
        listIdea = readIdea(fileName)
        printIdea(listIdea)
    elif namespace.delete:
        listIdea = readIdea(fileName)
        listIdea.remove(listIdea[namespace.delete-1])
        listIdea = rewriteList(fileName, listIdea)
        printIdea(listIdea)
    else:
        idea = inputIdea()
        writeIdea(fileName, idea)
        listIdea = readIdea(fileName)
        printIdea(listIdea)


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', action="store_const", const=True)
    parser.add_argument('--delete', type=int, default=0)
    return parser


def readIdea(fileName):
    with open(fileName, 'r') as file:
        listIdea = [row.rstrip() for row in file]
    return listIdea


def printIdea(listIdea):
    print("Your ideabank: ")
    i = 1
    for item in listIdea:
        print(i, ". ", item)
        i += 1


def inputIdea():
    inpIdea = input("What is you new idea: ")
    return inpIdea


def writeIdea(fileName, idea):
    with open(fileName, 'a', newline="") as file:
        file.write(idea + "\n")


def rewriteList(fileName, listIdea):
    with open(fileName, 'w', newline="") as file:
        for item in listIdea:
            file.write(item + "\n")
    return listIdea


main()
