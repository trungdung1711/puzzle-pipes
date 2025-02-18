from enum import Enum


class Direction(Enum):
	U	= 0
	R	= 1
	D	= 2
	L	= 3


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