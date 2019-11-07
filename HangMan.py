from random import randint

word = []
text = ''
display_word = []
guess = ''

wrong_guesses = 0
max_wrong = 6

game_over = False

filename = 'google-10000-english.txt'


def greeting():
    print("Welcome to Hangman!")


def get_word():
    global word
    global text

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
    print(text)
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
    letter_count = 0

    while not game_over:
        enter_letter()

        for letter in word:
            if guess == letter:
                match_found = True
                num = word.index(letter)
                display_word[num] = letter
                word[num] = ''
                letter_count += 1
            elif guess != letter:
                letter_count += 1

        if match_found:
            print("Correct!")
            show_progress()
            correct_guess()
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


def correct_guess():
    global game_over

    display_string = ''.join(display_word)

    if text == display_string:
        game_over = True
        print("You win!")
        show_progress()
    else:
        pass


def wrong_guess():
    global game_over
    global wrong_guesses

    print("Sorry, that letter is not in the word.")
    wrong_guesses += 1
    guesses_left = max_wrong - wrong_guesses
    print("\nGuesses left: " + str(guesses_left))
    show_progress()

    if wrong_guesses == max_wrong:
        game_over = True
        print("\nGame Over!")
    else:
        pass


greeting()
get_word()
get_user_input()
