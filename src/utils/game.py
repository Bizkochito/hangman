import random
import re
from typing import List

class Hangman:

    def __init__(self) -> None:
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = self.possible_words[random.randint(0,len(self.possible_words)-1)]
        self.lives = 5
        self.correctly_guessed_letters = ["_"]*len(self.word_to_find)
        self.correct_letters_count = 0
        self.wrongly_guessed_letters =[]
        self.turn_count = 0
        self.error_count = 0

    
    def play(self) -> None:
        """
        Method launching a playing round. Increments the turn first.
        Checks whether the input is valid (if it isnt, starts over until 
        it is valid).
        Then, increments the turn count and evaluates the guess.
        Evaluation happens in other methods.
        """

        guess = ""
        while not self.check_input(guess):
            guess = input("Give me a letter: ")
        self.evaluate(guess) 
            
    def check_input(self, guess: str) -> bool:
        """
        Method used to check the validity of the guess input.
        Returns False and prints a relevant message if the input
        is not a single letter or was already tried before.
        Returns True otherwise.
        :param guess: A string of which you need to check the validity.
        :return: True if the string is valide, False otherwise.
        """
        if type(guess) != str:
            print("You can only try letters.")
            return False
        if len(guess)!=1:
            print("You can only try a single letter at a time.")
            return False
        if guess in self.wrongly_guessed_letters:
            print("You already tried this one, and it was wrong.")
            return False
        if guess in self.correctly_guessed_letters:
            print("You already tried this one, and it is correct.")
            return False
        return True

    def evaluate(self, guess: str) -> None:
        """
        Decides if the guess is right or wrong, then calls the corresponding method.
        :param guess: A string that needs to be compared to the word to find.
        """

        if guess in self.word_to_find:
            self.good_guess(guess)
        else:
            self.bad_guess(guess)

    def good_guess(self, guess: str) -> None:
        """
        Method called when a good guess was identified. Prints a message,
        then calls a method to apply changes.
        :param guess: a str letter matching the word to find.
        """
        print('Good guess!')
        self.update_correctly_guessed(guess)

    def bad_guess(self, guess) -> None:
        """
        Method called when a wrong guess was identified. Prints a message,
        then applies needed changes:
        stores the wrong guess in wrongly_guessed_letters, increments
        error_count and decrements lives.
        :param guess: a single letter string that doesn't match word_to_find.
        """
        print('Wrong guess.')
        self.wrongly_guessed_letters.append(guess)
        self.error_count += 1
        self.lives -= 1

    def update_correctly_guessed(self, guess) -> None:
        """
        Method called to apply consequences of a correct guess from the user.
        Makes sure to find all the matches in the word, then replaces blanks
        in correctly_guessed_letters with the correctly guessed letter.
        Accordingly increments correct_letters_count, a variable used to simplify
        win condition checks.
        :param guess: a correctly guessed single letter string.
        """
        matches = [m.start() for m in re.finditer(guess, self.word_to_find)]
        for index in matches:
            self.correctly_guessed_letters[index] = guess
            self.correct_letters_count += 1

    def display_correct_letters(self) -> None:
        """
        Method used to display nicely correctly_guessed_letters.
        """
        string_to_print =""
        for char in self.correctly_guessed_letters:
            string_to_print += char
            string_to_print += " "
        print(string_to_print)

    def display_wrong_letters(self) -> None:
        """
        Method displaying the list of already tried wrong letters.
        """
        print('You already tried these letters:')
        print(self.wrongly_guessed_letters)

    def full_display(self) -> None:
        """
        Method displaying useful information to the user, such as current
        state of the guessing, wrong letters already tried, lives left,
        number of mistakes and turn count.
        """
        self.display_correct_letters()
        self.display_wrong_letters()
        print(f'You have {self.lives} lives left. You have made {self.error_count} mistake(s) so far, and this is turn {self.turn_count}.')

    def start_game(self) -> None:
        """
        Method starting a game when called. Displays relevant informations and
        launches a turn, then keeps on doing that until player is out of lives
        or found the word.
        """
        print('Welcome to Hangman by Grégoire Hupin')
        while self.lives > 0:
            self.full_display()
            self.play()
            if self.correct_letters_count == len(self.word_to_find):
                self.well_played()
                return

        self.game_over()
        return
        

    def well_played(self):
        """
        Method called when the player won. Displays a summary of the game,
        including the word, turn count, and mistakes.
        """
        print(f'You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!')

    def game_over(self):
        """
        Method called when the game is over. Display a game over message.
        """
        print('game over...')





