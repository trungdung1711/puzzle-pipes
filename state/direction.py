from enum import Enum


class Direction(Enum):
	U	= 1
	R	= 2
	D	= 3
	L	= 4


	@staticmethod
	def opposite(direction: 'Direction') -> 'Direction':
		if direction == Direction.U:
			return Direction.D
		elif direction == Direction.D:
			return Direction.U
		elif direction == Direction.R:
			return Direction.L
		elif direction == Direction.L:
			return Direction.R
		

	@staticmethod
	def get_next_location(location: tuple, direction: 'Direction'):
		row, col = location
		if direction == Direction.U:
			return (row - 1, col)
		elif direction == Direction.D:
			return (row + 1, col)
		elif direction == Direction.L:
			return (row, col - 1)
		else:
			return (row, col + 1)