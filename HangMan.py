from random import randint

word = []
display_word = []
guess = ''

wrong_guesses = 0
max_wrong = 6

filename = 'google-10000-english.txt'


def greeting():
    print("Welcome to Hangman!")


def get_word():
    global word

    file = open(filename)
    all_lines = file.readlines()
    while True:
        text = all_lines[randint(0, 9999)]
        if len(text) < 6:
            text = all_lines[randint(0, 9999)]
        else:
            break
    text = text.rstrip()
    text = 'aabbaac'
    for letter in text:
        word.append(letter)
    create_visual_word()
    print("\nThe word is " + str(len(word)) + " characters long.")


def create_visual_word():
    for letter in word:
        display_word.append('-')
    show_progress()


def show_progress():
    print("\nWord: " + ''.join(display_word))


def get_user_input():
    global word
    global guess
    match_found = False
    word_length = len(word)
    letter_count = 0

    while True:
        enter_letter()

        for letter in word:
            if guess == letter:
                match_found = True
                num = word.index(letter)
                print(num)
                word[num] = ''
                letter_count += 1
            elif guess != letter:
                letter_count += 1

        if match_found:
            print("Correct!")
            match_found = False
        else:
            wrong_guess()


def enter_letter():
    global guess

    guess = input("\nPlease enter one letter:")
    while True:
        if len(guess) != 1:
            guess = input("\nPlease enter a single letter: ")
        else:
            break


def wrong_guess():
    global wrong_guesses

    print("Sorry, that letter is not in the word.")
    wrong_guesses += 1
    guesses_left = max_wrong - wrong_guesses
    print("\nGuesses left: " + str(guesses_left))

    if wrong_guesses == max_wrong:
        print("\nGame Over!")


greeting()
get_word()
get_user_input()
