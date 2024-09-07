def welcome(name):
    print(f'Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n')


def load_game():
    print(f'Please choose a game to play:\n'
          '     1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n'
          '     2. Guess Game - guess a number and see if you chose like the computer\n'
          '     3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n')

    while True:
        try:
            choice = int(input('Please make your choice: '))
            if choice == 1:
                print('\nWelcome to Memory Game!')
                break
            elif choice == 2:
                print('\nWelcome to Guess Game!')
                break
            elif choice == 3:
                print('\nWelcome to Currency Roulette!')
                break
            else:
                print('Please enter a number from 1 to 3!')
        except ValueError:
            print('Invalid input. Please enter a valid integer.')

    print('\nPlease choose game difficulty from 1 to 5: \n'
          '     1. Beginner\n'
          '     2. Easy\n'
          '     3. Normal\n'
          '     4. Hard\n'
          '     5. Insane\n')

    while True:
        try:
            difficulty = int(input('Please select your preferred difficulty level: '))
            if difficulty == 1:
                print('\nYour preference is to play as Beginner\n')
                break
            elif difficulty == 2:
                print('\nYour preference is to play as Easy\n')
                break
            elif difficulty == 3:
                print('\nYour preference is to play as Normal\n')
                break
            elif difficulty == 4:
                print('\nYour preference is to play as Hard\n')
                break
            elif difficulty == 5:
                print('\nYour preference is to play as Insane\n')
                break
            else:
                print('\nPlease select a number from 1 to 5\n')
        except ValueError:
            print('Invalid input. Please enter a valid integer.')
