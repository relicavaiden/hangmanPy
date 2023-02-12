import random
from words import words 
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # What has been guessed already
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    # get user input
    while len(word_letters) > 0 and lives > 0:

        # Letters guessed
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # What the current word is with stars
        word_list = [letter if letter in used_letters else '*' for letter in word]
        print('Current word: ', ' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 # minus one live each time that you make a mistake
                print('This letter is not in the word')

        elif user_letter in used_letters:
            print('You have already choosen this letter. Please choose again.')

        else:
            print('Please use only letters A to Z. No numbers or characters.')

    if lives == 0:
        print('Sorry you lost, the word was:', word)
    else:
        print('Congratulations you guessed the word', word, 'correctly!!')

     

hangman()