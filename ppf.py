words = ['go', 'hold', 'see', 'hide', 'sit', 'travel', 'look', 'die']
exceptionVerbs = ['be', 'see', 'flee', 'knee']
vowels = ['a', 'e', 'i', 'u', 'o', 'y']

ing = 'ing'

for verb in words:
    if verb[-1] == 'e' and verb[-2] != 'i' and verb not in exceptionVerbs:
        verb = verb[0:len(verb) - 1] + ing
    elif verb[-1] == 'e' and verb[-2] == 'i':
        verb = verb[0:len(verb) - 2] + 'y' + ing
    elif verb[-1] not in vowels and verb[-2] in vowels and verb[
            -3] not in vowels:
        verb = verb + verb[-1] + ing
    else:
        verb = verb + ing
    print(verb)
