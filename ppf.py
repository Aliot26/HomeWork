def main():
    words = inputWord()
    toParticiple(words)


def inputWord():
    words = list()
    verb = input("Input verb: ")
    words = verb.split()
    return words


def toParticiple(words):
    exceptionVerbs = ['be', 'see', 'flee', 'knee']
    vowels = ['a', 'e', 'i', 'u', 'o', 'y']
    ing = 'ing'
    for verb in words:
        if verb[-1] == 'e' and verb[-2] != 'i' and verb not in exceptionVerbs:
            verb = verb[0:len(verb) - 1] + ing
            print(verb)
        elif verb[-1] == 'e' and verb[-2] == 'i':
            verb = verb[0:len(verb) - 2] + 'y' + ing
            print(verb)
        elif verb[-1] not in vowels and verb[-2] in vowels and verb[
                -3] not in vowels:
            verb = verb + verb[-1] + ing
            print(verb)
        else:
            verb = verb + ing
            print(verb)


main()