import random


class CurrencyRouletteGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.exchange_rate = self.get_usd_to_ils_rate()

    def get_usd_to_ils_rate(self):
        return 3.5

    def get_money_interval(self, usd_amount):
        total_value = usd_amount * self.exchange_rate
        margin_of_error = 5 - self.difficulty
        return total_value - margin_of_error, total_value + margin_of_error

    def get_guess_from_user(self, usd_amount):
        guess = float(input(f"How much do you think {usd_amount:.2f} USD is in ILS? "))
        return guess

    def play(self):
        usd_amount = random.uniform(1, 100)

        lower_bound, upper_bound = self.get_money_interval(usd_amount)

        user_guess = self.get_guess_from_user(usd_amount)

        if lower_bound <= user_guess <= upper_bound:
            print(f"Correct! {usd_amount:.2f} USD is approximately {usd_amount * self.exchange_rate:.2f} ILS.")
            return True
        else:
            print(f"Sorry, {usd_amount:.2f} USD is approximately {usd_amount * self.exchange_rate:.2f} ILS.")
            return False
