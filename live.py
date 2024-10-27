from guess_game import GuessGame
from memory_game import MemoryGame
from currency_roulette_game import CurrencyRouletteGame
from score import add_score
from utils import screen_cleaner

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
                print(f'Please enter a valid number from: {valid_values}.')
        except ValueError:
            print('Invalid input. Please enter a valid integer.')

def load_game():
    # Mapping game choices to the respective game class constructors
    games = {
        1: MemoryGame,
        2: GuessGame,
        3: CurrencyRouletteGame
    }

    # Display the game options
    game_descriptions = {
        1: 'Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back',
        2: 'Guess Game - guess a number and see if you chose like the computer',
        3: 'Currency Roulette - try and guess the value of a random amount of USD in ILS'
    }

    print(f'Please choose a game to play: \n')
    for key, description in game_descriptions.items():
        print(f'    {key}. {description}')

    # Get user's game choice
    game_choice = get_valid_input('\nPlease make your choice: ', list(games.keys()))

    print(f'\nWelcome to {game_descriptions[game_choice].split(" - ")[0]}!')

    # Display difficulty options
    difficulties = ['Beginner', 'Easy', 'Normal', 'Hard', 'Insane']
    print('\nPlease choose game difficulty from 1 to 5: \n')
    for idx, difficulty in enumerate(difficulties, 1):
        print(f'    {idx}. {difficulty}')

    # Get user's difficulty choice
    difficulty_choice = get_valid_input('\nPlease select your preferred difficulty level: ', range(1, 6))
    print(f'\nYour preference is to play as {difficulties[difficulty_choice - 1]}\n')

    # Dynamically instantiate the game class based on user choice and start the game
    selected_game_class = games[game_choice]  # Fetches the game class
    game_instance = selected_game_class(difficulty_choice)  # Creates an instance with the chosen difficulty

    game_won = game_instance.start()

    if game_won:
        print('\nCongratulations, you won!')
        add_score(difficulty_choice)
    else:
        print('\nGood try! Better luck next time.')

    screen_cleaner()
