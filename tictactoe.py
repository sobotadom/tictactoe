from game_check import game_check


def tictactoe():
    nummoves = 0
    MAXMOVES = 9
    game = [['-','-','-'],['-','-','-'],['-','-','-']]
    player = 1
    winner = '-'

    print('',game[0],'\n',game[1],'\n',game[2])
    while nummoves != MAXMOVES and winner == '-':
        row = 0
        column = 0
        marker = ''
        if player == 1:   #Player 1 turn
            while True:

                row,column = input('Player one, enter your coordinates (row, column)').split(',')
                row = int(row)
                column = int(column)
                if row < 1 or column < 1 or row > 3 or column > 3:
                    print('Try again')
                else:
                    break

            marker = 'X'
        else: # Player 2 turn
            while True:

                row,column = input('Player two, enter your coordinates (row, column)').split(',')
                row = int(row)
                column = int(column)
                if row < 1 or column < 1 or row > 3 or column > 3:
                    print('Try again')
                else:
                    break

            marker = 'O'

        if game[row - 1][column - 1] == '-': #empty position
            game[row-1][column-1] = marker
            if marker == 'X':
                player = 2   #let player two take their turn
            elif marker == 'O':
                player = 1  #let player one take their turn

            nummoves += 1

            winner = game_check(game) #check if after the move is made, there is a winner

            print('Move ', nummoves, ' Winner ', winner)
        else:
            print('\nSpot taken, try again!\n')


        print('',game[0],'\n',game[1],'\n',game[2])

    if nummoves == MAXMOVES:
        print('\nGame ran out of moves!\nThe game is a draw :(')
    elif winner == 'X':
        print('\nPlayer 1 has won the game!\n')
    elif winner == 'O':
        print('\nPlayer 2 has won the game!\n')

    return winner
