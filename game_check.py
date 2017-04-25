"""
Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.
"""
def game_check( game_board):
	winner = '-'

	#diagnols
	if game_board[0][0] == game_board[1][1] and game_board[1][1] == game_board[2][2] and game_board[0][0] != '-':
		winner = game_board[0][0]
	elif game_board[2][0] == game_board[1][1] and game_board[1][1] == game_board[0][2] and game_board[2][0] != '-':

		winner = game_board[0][2]



	for i in range(0,3):
		#rows, if all three columns have the same value, winner is assigned
		if game_board[i][0] == game_board[i][1] and game_board[i][1] == game_board[i][2] and game_board[i][0] != '-':

			winner = game_board[i][0]
		#columns, if all three rows have the same value, winner is assigned
		elif  game_board[0][i] == game_board[1][i] and game_board[1][i] == game_board[2][i] and game_board[0][i] != '-':

			winner = game_board[0][i]

	return winner
