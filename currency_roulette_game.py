import random
import requests
from game import Game


class CurrencyRouletteGame(Game):
    def __init__(self, difficulty):
        super().__init__(difficulty)

    def get_current_exchange_rate(self):
        url = 'https://api.exchangerate-api.com/v4/latest/USD'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return data['rates']['ILS']  # Get the ILS rate
        else:
            print("Error fetching exchange rate.")
            return None

    def get_money_interval(self, amount_usd):
        exchange_rate = self.get_current_exchange_rate()
        total_value = amount_usd * exchange_rate
        margin = 5 - self.difficulty
        return total_value - margin, total_value + margin

    def get_guess_from_user(self, amount_usd):
        while True:
            user_input = input(f'Guess the value of {amount_usd} USD in ILS: ')

            formatted_user_input = user_input.replace(',', '.')

            try:
                return float(formatted_user_input)
            except ValueError:
                print(f'Invalid input. Please enter a valid number.')

    def play(self):
        amount_usd = random.randint(1, 100)
        interval = self.get_money_interval(amount_usd)
        guess = self.get_guess_from_user(amount_usd)
        return interval[0] <= guess <= interval[1]
