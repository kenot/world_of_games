from abc import ABC, abstractmethod

class Game(ABC):
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def validate_input(self, prompt, valid_range=None):
        while True:
            try:
                user_input = int(input(prompt))
                # If valid_range is provided, ensure the input falls within the range
                if valid_range and user_input not in valid_range:
                    print(f"Please enter a number between {valid_range.start} and {valid_range.stop - 1}.")
                else:
                    return user_input
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def welcome_message(self):
        print(f'Welcome to the {self.__class__.__name__}!')

    def play(self):
        pass

    def start(self):
        self.welcome_message()
        print(f'Starting the game with difficulty level: {self.difficulty}')
        result = self.play()
        self.end_game(result)

    def end_game(self, result):
        if result:
            print(f'Congratulations, you won the {self.__class__.__name__}!')
        else:
            print(f'Sorry, you lost the {self.__class__.__name__}. Better luck next time!')