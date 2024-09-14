from guess_game import GuessGame
from memory_game import MemoryGame
from currency_roulette_game import CurrencyRouletteGame


def welcome(name):
    print(f'Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n')


def get_valid_input(prompt, valid_range):
    valid_range_list = list(valid_range)
    while True:
        try:
            choice = int(input(prompt))
            if choice in valid_range_list:
                return choice
            else:
                valid_values = ', '.join(map(str, valid_range_list))
                print(f"Please enter a valid number from: {valid_values}.")
        except ValueError:
            print('Invalid input. Please enter a valid integer.')


def load_game():
    games = {
        1: 'Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back',
        2: 'Guess Game - guess a number and see if you chose like the computer',
        3: 'Currency Roulette - try and guess the value of a random amount of USD in ILS'
    }
    print(f'Please choose a game to play: \n')
    for key, description in games.items():
        print(f'    {key}. {description}')

    game_choice = get_valid_input('\nPlease make your choice: ', list(games.keys()))

    print(f'\nWelcome to {games[game_choice].split(" - ")[0]}!')

    difficulties = ['Beginner', 'Easy', 'Normal', 'Hard', 'Insane']
    print('\nPlease choose game difficulty from 1 to 5: \n')
    for idx, difficulty in enumerate(difficulties, 1):
        print(f'    {idx}. {difficulty}')

    difficulty_choice = get_valid_input('\nPlease select your preferred difficulty level: ', range(1, 6))
    print(f'\nYour preference is to play as {difficulties[difficulty_choice - 1]}\n')

    if game_choice == 1:
        print("\nStarting Memory Game...\n")
        memory_game = MemoryGame(difficulty_choice)
        memory_game.play()
    elif game_choice == 2:
        print("\nStarting Guess Game...\n")
        guess_game = GuessGame(difficulty_choice)
        guess_game.play()
    elif game_choice == 3:
        print("\nStarting Currency Roulette...\n")
        currency_roulette = CurrencyRouletteGame(difficulty_choice)
        currency_roulette.play()
