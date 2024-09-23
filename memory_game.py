import random
import time
from game import Game


class MemoryGame(Game):
    def __init__(self, difficulty):
        super().__init__(difficulty)

    def generate_sequence(self):
        return [random.randint(1, 101) for _ in range(self.difficulty)]

    def get_list_from_user(self):
        user_sequence = []
        print(f"Enter the {self.difficulty} numbers you remember, one at a time.")
        for i in range(self.difficulty):
            user_input = self.validate_input(f'Enter number {i + 1}: ')
            user_sequence.append(user_input)
        return user_sequence

    def is_list_equal(self, list1, list2):
        return list1 == list2

    def play(self):
        sequence = self.generate_sequence()
        print(f"Memorize this sequence: {sequence}")
        time.sleep(1)
        print("\n" * 50)  # Clears the screen (simulate hiding the sequence)

        user_sequence = self.get_list_from_user()
        return self.is_list_equal(sequence, user_sequence)
