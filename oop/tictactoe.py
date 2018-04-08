class TicTacToe(object):
	def __init__(self):
		self._board = [[' '] * 3 for j in range(3)]
		self._player = 'X'

	def mark(self, i, j):
		# make sure move is a valid board position
		if not (0 <= i <=2 and 0 <= j <= 2):
			raise ValueError('Invalid board position')

		# make sure move is not in an already occupied position
		if self._board[i][j] != ' ':
			raise ValueError('Board position occupied')

		# make sure there isn't already a game winner
		if self.winner() is not None:
			raise ValueError('Game is already complete')

		# assign board position to current player token X or O
		self._board[i][j] = self._player

		# swap players
		if self._player == 'X':
			self._player = 'O'
		else:
			self._player = 'X'

	def _is_win(self, mark):
		board = self._board
		return (mark == board[0][0] == board[0][1] == board[0][2] or # winner in top row of game board
				mark == board[1][0] == board[1][1] == board[1][2] or # winner in middle row of game board
				mark == board[2][0] == board[2][1] == board[2][2] or # winner in bottom row of game board
				mark == board[0][0] == board[1][0] == board[2][0] or # winner in first column of game board
				mark == board[0][1] == board[1][1] == board[2][1] or # winner in second column of game board
				mark == board[0][2] == board[1][2] == board[2][2] or # winner in third column of game board
				mark == board[0][0] == board[1][1] == board[2][2] or # winner in diagonal
				mark == board[2][0] == board[1][1] == board[0][2]) # winner in diagonal

	def winner(self):
		for mark in 'XO':
			if self._is_win(mark):
				return mark
		return None

	def __str__(self):
		rows = ['|'.join(self._board[r]) for r in range(3)]
		return '\n-----\n'.join(rows)
