from random import randint

text = ''  # text will hold a random word from our file
word = []  # our word will be kept in an array so we can remove certain characters
display_word = []  # display word will be used to show the user's progress
guess = ''  # guess will be the user's guess
wrong_letters = []  # this array will keep track of the wrong guesses

word_length = 7  # the minimum length we want for the word

wrong_guesses = 0
max_wrong = 6

game_over = False

filename = 'google-10000-english.txt'


def greeting():
    print("Welcome to Hangman!")


def get_word():
    global text
    global word
    global display_word
    global guess
    global wrong_letters

    # clear these variables for when the user wants to play again
    text = ''
    word = []
    display_word = []
    guess = ''
    wrong_letters = []

    file = open(filename)
    all_lines = file.readlines()

    text = all_lines[randint(0, 9999)]

    # keep getting a word if it's less than our desired word length
    while True:
        if len(text) < word_length:
            text = all_lines[randint(0, 9999)]
        else:
            break

    text = text.rstrip()
    # append text into the word array
    for letter in text:
        word.append(letter)
    create_visual_word()
    print("\nThe word is " + str(len(word)) + " characters long.")


def create_visual_word():  # create an array that can showcase the user's progress
    for letter in word:
        display_word.append('-')
    show_progress()


def show_progress():  # show the user's progress in string format
    print("\nWord: " + ''.join(display_word))


def show_wrong_letters():
    if len(wrong_letters) == 0:
        pass
    else:
        print("\nWrong letters: " + ' '.join(wrong_letters))


def get_user_input():  # receive the user's input
    global word
    global guess
    match_found = False

    while not game_over:
        show_wrong_letters()
        enter_letter()

        for letter in word:  # look through every letter in the word array
            if guess == letter:  # if the user's guess matches the letter
                match_found = True  # we have found a match, so user is not incorrect
                num = word.index(letter)  # get the index of the matched letter
                display_word[num] = letter  # set this index in our display array to this letter
                word[num] = ''  # set the letter at this index of the word array to this, to remove duplicates
            elif guess != letter:  # if the guess does not match up with a letter, pass
                pass

        # after we check through the word, see if there's any matches
        if match_found:  # if there is a match found
            correct_guess()  # the user was correct
            match_found = False  # set match_found to false
        else:  # if there was no match found
            wrong_letters.append(guess)
            wrong_guess()  # the user was wrong


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

    print("Correct!")
    if text == display_string:
        game_over = True
        print("You win!")
        play_again()
    else:
        pass

    show_progress()


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
        print("The word was " + text + ".")
        play_again()
    else:
        pass


def play_again():
    global game_over

    while True:
        again = input("\nWould you like to play again? (Y/N).")
        again = again.lower()

        if again == 'y':
            play()
            game_over = False
            break
        elif again == 'n':
            print("Thanks for playing!")
            break
        else:
            print("Not a valid input.")
            again = input("\nWould you like to play again? (Y/N).")
            again = again.lower()


def play():
    get_word()
    get_user_input()


greeting()
play()
