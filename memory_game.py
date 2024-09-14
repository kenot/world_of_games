import random
import time


class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.sequence = []

    def generate_sequence(self):
        self.sequence = [random.randint(1, 101) for _ in range(self.difficulty)]
        return self.sequence

    def get_list_from_user(self):
        print(f'Please enter {self.difficulty} numbers separated by spaces: ')
        user_input = input()
        user_sequence = list(map(int, user_input.split()))
        return user_sequence

    def is_list_equal(self, user_sequence):
        return user_sequence == self.sequence

    def play(self):
        sequence = self.generate_sequence()

        print(f'Try to memorize this sequence: {sequence}')
        time.sleep(0.7)
        print('\n' * 50)

        user_sequence = self.get_list_from_user()

        if self.is_list_equal(user_sequence):
            print('Congratulations! You remembered the sequence correctly!')
            return True
        else:
            print(f'Sorry, the correct sequence was {sequence}. Better luck next time!')
            return False
