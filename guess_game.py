import random
from game import Game

class GuessGame(Game):
    def __init__(self, difficulty):
        super().__init__(difficulty)

    def generate_number(self):
        return random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        return int(input(f'Guess a number between 1 and {self.difficulty}: '))

    def compare_results(self, secret_number, user_guess):
        return secret_number == user_guess

    def play(self):
        secret_number = self.generate_number()
        user_guess = self.get_guess_from_user()
        return self.compare_results(secret_number, user_guess)
