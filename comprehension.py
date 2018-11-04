# This program randomly makes a number from 1 to 20 for user guessing.
import random  # add random module

guesses_taken = 0  # assign 0 to guesses_taken variable

print('Hello! What is your name?')  # print the message
myName = input()  # assign value printed by user to myName variable

number = random.randint(1, 20)  # assign a random integer to number variable

# print the message
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while guesses_taken < 6:  # start the while loop
    print('Take a guess.')  # print the message
    guess = input()  # assign value printed by user to guess variable
    guess = int(guess)  # cast string to integer

    guesses_taken += 1  # update counter

    if guess < number:  # check if guess less than number
        print('Your guess is too low.')  # print the message

    if guess > number:  # check if guess more than number
        print('Your guess is too high.')  # print the message

    if guess == number:  # check if guess equals number
        break  # interrupt the while loop

if guess == number:  # check if guess equals number
    guesses_taken = str(guesses_taken)  # cast string to integer
    print('Good job, ' + myName + '! You guessed my number in ' +
          guesses_taken + ' guesses!')  # print the message

if guess != number:  # check if guess does not equal number
    number = str(number)  # cast integer to string
    print('Nope. The number I was thinking of was ' + number)  # print the message
