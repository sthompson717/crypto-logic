# Description #
This project is a word jumble game which was created as a final project for CS 230 Fundamentals of Computing in Spring 2020.

The game begins with a short welcome message which says "Welcome to Crypto-Logic! Guess the jumbled word, one letter at a time!" The program then asks the user to choose a game mode by typing the name of the game mode from the list of options and pressing enter. There are four options for game modes: Easy, Medium, Hard, and Dyslexia.
* Easy: All words will be 6 letters in length or shorter
* Medium: All words will be 7 letters in length
* Hard: All words will be 8 letters in length or longer
* Dyslexia: Any word from the word bank can be chosen but the letters will not be scrambled

If the user does not type one of the four acceptable game modes from the provided list, the program will continue to ask for the user to choose a valid game mode until they do so.

Once a valid game mode has been selected, the program will read a text file called "wordlist.txt" which contains a list of 300 words written one word per line. ***The text file must be stored in the same folder as the project code file in order for the program to work successfully.*** As the program reads the list of words, it will save only the words which apply to the mode selected by the user and store those words in a word bank.

When the program has finished reading the text file, it will then randomly choose one word from the created word bank. It then removes that word from the "wordlist.txt" text file so that it cannot be chosen again when the user plays the game again in the future. It also writes the chosen word onto another text file called "guessedwords.txt" so that words that have been previously guessed are available to be added back to the original "wordlist.txt" file if the user wants to reset the game.

In order to scramble the randomly selected word, the program first splits the word up into its individual letters and stores those letters in a list called "ordered letters". The program then shuffles those letters into a random order and stores the shuffled letters into another list called "scrambled letters". If the user has selected the game mode "Dyslexia", the word will still be split up into its individual letters, but the letters will not be scrambled.

Now that the program has successfully selected a word and scrambled the letters of that word, the main game can begin. As soon as the game begins, the program starts a timer which ends as soon as the user correctly guesses the entire word. The total length of time it takes the user to correctly guess the word will be shown in seconds at the end of the game. At the start of each turn, the program will show the user the number of incorrect guesses so far, the scrambled letters of the word from the list scrambled letters, and the correctly guessed letters of the word so far which are stored in a new list called "correct letters". At the start of the game, incorrect guesses are automatically set to 0 and the list of correct letters is empty.

The user is prompted to guess the first letter of the word by typing it in and pressing enter. If the letter which is typed in by the user matches the first letter of the unscrambled word which is stored in the list called "ordered letters", then that letter is added to the list of correctly guessed letters called "correct letters" and the number of incorrect guesses remains the same. If the letter which is typed in by the user does not match the first letter in the list called "ordered letters", then the number of incorrect guesses is increased by 1 and user is reprompted to guess the first letter of the word.



which randomly selects a word from a text file, scrambles the letters, and tracks how many turns it takes the user to correctly guess the scrambled word.
