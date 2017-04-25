from game_check import game_check
from tictactoe import tictactoe

wins_one = 0
wins_two = 0
draws = 0

while True:

    winner = tictactoe() #play the game
    if winner == 'X':
        wins_one += 1
    elif winner == 'O':
        wins_two += 1
    else:
        draws += 1

    again = input('Would you like to play again?[y/n]\n')

    if again != 'y':
        break





print('\nPlayer 1 won ', wins_one, ' games\nPlayer 2 won ', wins_two, ' games\nThere were ', draws, ' draws')
