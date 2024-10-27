import os


POINTS_OF_WINNING = lambda difficulty: (difficulty * 3) + 5


from utils import SCORES_FILE_NAME, BAD_RETURN_CODE


def add_score(difficulty):
    try:
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, "r") as file:
                current_score = int(file.read().strip() or 0)
        else:
            current_score = 0

        points_to_add = POINTS_OF_WINNING(difficulty)
        new_score = current_score + points_to_add

        with open(SCORES_FILE_NAME, "w") as file:
            file.write(str(new_score))

        print(f'Score updated! Current total score is now: {new_score}')
    except (IOError, ValueError) as e:
        print('Error managing the score file: ', e)
        return BAD_RETURN_CODE
    return new_score
