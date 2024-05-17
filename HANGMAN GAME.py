import random

class Hangman:
    def __init__(self, word_list):
        self.word_list = word_list
        self.secret_word = ""
        self.guesses_left = 6
        self.guessed_letters = []
        self.display_word = []
        self.hangman_stages = [
            """
                -------
               |       |
                       |
                       |
                       |
                       |
               ---------
            """,
            """
                -------
               |       |
               O       |
                       |
                       |
                       |
               ---------
            """,
            """
                -------
               |       |
               O       |
               |       |
                       |
                       |
               ---------
            """,
            """
                -------
               |       |
               O       |
              /|       |
                       |
                       |
               ---------
            """,
            """
                -------
               |       |
               O       |
              /|\\      |
                       |
                       |
               ---------
            """,
            """
                -------
               |       |
               O       |
              /|\\      |
              /        |
                       |
               ---------
            """,
            """
                -------
               |       |
               O       |
              /|\\      |
              / \\      |
                       |
               ---------
            """
        ]

    def select_random_word(self):
        self.secret_word = random.choice(self.word_list)
        self.display_word = ['_'] * len(self.secret_word)

    def display_hangman(self):
        print(self.hangman_stages[6 - self.guesses_left])

    def display_word_state(self):
        print(" ".join(self.display_word))

    def get_guess(self):
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            return self.get_guess()
        return guess

    def update_word_state(self, guess):
        for i, letter in enumerate(self.secret_word):
            if letter == guess:
                self.display_word[i] = letter

    def check_guess(self, guess):
        if guess in self.guessed_letters:
            print("You've already guessed that letter.")
            return False
        self.guessed_letters.append(guess)
        if guess in self.secret_word:
            self.update_word_state(guess)
            return True
        else:
            self.guesses_left -= 1
            return False

    def check_win(self):
        return '_' not in self.display_word

    def check_loss(self):
        return self.guesses_left == 0

    def play_again(self):
        play_again = input("Do you want to play again? (yes/no): ").lower()
        return play_again == 'yes'

    def play(self):
        print("Welcome to Hangman!")
        while True:
            self.select_random_word()
            while not self.check_win() and not self.check_loss():
                print("\n")
                self.display_hangman()
                self.display_word_state()
                guess = self.get_guess()
                if not self.check_guess(guess):
                    print("Incorrect guess. {} guesses left.".format(self.guesses_left))
            if self.check_win():
                print("Congratulations! You guessed the word: {}".format(self.secret_word))
            else:
                print("Sorry, you ran out of guesses. The word was: {}".format(self.secret_word))
            if not self.play_again():
                break

# Example usage
word_list = ["apple", "banana", "orange", "grape", "pineapple"]
hangman_game = Hangman(word_list)
hangman_game.play()
