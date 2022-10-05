#    Hangman Game

#     '''
#     secretWord: string, the secret word to guess.

#     Starts up an interactive game of Hangman.

#     * At the start of the game, let the user know how many 
#       letters the secretWord contains.

#     * Ask the user to supply one guess (i.e. letter) per round.

#     * The user should receive feedback immediately after each guess 
#       about whether their guess appears in the secret word.

#     * After each round, you should also display to the user the 
#       partially guessed word so far, as well as letters that the 
#       user has not yet guessed.
#   '''

import time
from random import choice


def hangman():
    word_list = ['flamingo', 'tiger', 'lion', 'rhino', 'monkey', 'turtle', 'eagle', 'rabbit', 'fish', 'mouse', 'frog', 'dog', 'cat', 'bat', 'rat', 'goat', 'pig', 'horse', 'cow', 'moose']
    word = choice(word_list)

    wrong_guess = []
    correct_guess = []
    for i in range(len(word)):
        correct_guess.append('__')

    print("\n")
    print('Hi there. Lets play Hang Man!')
    time.sleep(1)
    print("\n")
    print("The word I am thinking of is an animal with", len(word), "letters.")
    time.sleep(1)

    guesses = 6

    while guesses:
        print("\n")
        guess = input('Please guess a letter! ')
        if guess in wrong_guess:
            print("\n")
            print('You have already guessed that, try another letter.')
        elif guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    correct_guess[i] = word[i]
            print(
                'That is a correct letter! Let me put it in the right spot.')
        elif guess not in word:
            wrong_guess.append(guess)
            guesses -= 1
            print('Sorry, that is an incorrect letter, try again! You have',
                  guesses, "guesses left!")

        guessed_word = (''.join(correct_guess))
        if guessed_word == word:
            print("\n")
            print('You guessed the word:', word,'. Great job!')
            print("\n")
            time.sleep(1)
            break

        if guesses == 0:
            if guessed_word != word:
                print("\n")
                print('Oh my, so sorry. You did are out of guesses. The word was', word)
                print("\n")
                time.sleep(1)
            break

        time.sleep(1)
  
        print("\n")
        print(' '.join(correct_guess))
        print("\n")

        time.sleep(1)


hangman()