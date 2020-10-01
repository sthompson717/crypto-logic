# Stephen Thompson
# CS 230 001 21721
# Project 1 04/06/20
# Chooses a random word from a text file, scrambles it, and allows user to guess each letter in order

import random
import time

mode = ""


def game_mode():
    # receives input from user of desired game mode
    global mode
    mode = input("Please enter your desired game mode: ").lower()
    while mode not in ("easy", "medium", "hard", "dyslexia"):
        mode = input("Please enter a valid game mode: ").lower()


def import_words():
    # reads the word list file and stores in a list the words which are relevant based on game mode
    word_list = []
    with open("wordlist.txt", "r") as file:
        for line in file:
            if mode == "easy" and len(line.strip()) <= 6:
                word_list.append(line.strip())
            elif mode == "medium" and len(line.strip()) == 7:
                word_list.append(line.strip())
            elif mode == "hard" and len(line.strip()) >= 8:
                word_list.append(line.strip())
            elif mode == "dyslexia":
                word_list.append(line.strip())
    return word_list


def remove_chosen_words():
    # removes words found in the guessed words file from the word list file
    with open("wordlist.txt", "r") as unselected_word_list:
        unselected_words = unselected_word_list.readlines()
    with open("guessedwords.txt", "r") as selected_word_list:
        selected_words = selected_word_list.readlines()
    edited_word_list = open("wordlist.txt", "w")
    for word in unselected_words:
        if word not in selected_words:
            edited_word_list.write(word)
    edited_word_list.close()


def choose_word():
    # chooses a word from the word list at random, adds it to guessed words file, and removes it from word list file
    word_list = import_words()
    word = random.choice(word_list)
    with open("guessedwords.txt", "a") as guessed_words:
        guessed_words.write(word + "\n")
    remove_chosen_words()
    return word


def scramble_word():
    # splits the word into letters and scrambles the letters if mode is not dyslexia
    word = choose_word()
    ordered_letters = list(word)
    scrambled_letters = ordered_letters
    if mode != "dyslexia":
        scrambled_letters = random.sample(ordered_letters, len(ordered_letters))
    return ordered_letters, scrambled_letters


def print_letters(scrambled_letters, correct_letters, incorrect_guesses):
    # prints to the screen the incorrect guesses, the scrambled word, and the correctly guessed letters so far
    print("Incorrect guesses: " + str(incorrect_guesses))
    print(''.join(scrambled_letters).upper())
    print(''.join(correct_letters).upper())


def game_round():
    # receives user guesses for each letter of the word in order, tallies incorrect guesses, calculates elapsed time
    start_time = time.time()
    correct_letters = []
    ordered_letters, scrambled_letters = scramble_word()
    incorrect_guesses = 0
    for i in ordered_letters:
        print_letters(scrambled_letters, correct_letters, incorrect_guesses)
        guess = input("Guess a letter: ")
        while guess != i:
            incorrect_guesses += 1
            print_letters(scrambled_letters, correct_letters, incorrect_guesses)
            guess = input("Guess a letter: ")
        correct_letters.append(i)
    elapsed_time = time.time() - start_time
    return ordered_letters, incorrect_guesses, elapsed_time


def continue_game():
    # prints congratulations message and continues or terminates game based on user input
    ordered_letters, incorrect_guesses, elapsed_time = game_round()
    if incorrect_guesses == 1:
        guesses = "guess"
    else:
        guesses = "guesses"
    print("Congratulations! You solved the word " + ''.join(ordered_letters).upper() + " in " + str(round(elapsed_time))
          + " seconds with " + str(incorrect_guesses) + " incorrect " + guesses + ".")
    game_state = input("Would you like to play another game? ")
    while game_state.lower() not in ("yes", "no"):
        game_state = input("Would you like to play another game? ")
    if game_state.lower() == "yes":
        return True
    else:
        return False


def main():
    print("Welcome to Crypto-Logic!\n"
          "Guess the jumbled word, one letter at a time!")
    game_mode()
    while continue_game():
        game_mode()


main()
