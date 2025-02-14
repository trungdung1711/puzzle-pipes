from enum import Enum


class Direction(Enum):
	UP 		= 1
	RIGHT	= 2
	DOWN 	= 3
	LEFT	= 4


	@staticmethod
	def opposite(direction: 'Direction') -> 'Direction':
		if direction == Direction.UP:
			return Direction.DOWN
		elif direction == Direction.DOWN:
			return Direction.UP
		elif direction == Direction.RIGHT:
			return Direction.LEFT
		elif direction == Direction.LEFT:
			return Direction.RIGHT
		

	@staticmethod
	def get_next_location(location: tuple, direction: 'Direction'):
		row, col = location
		if direction == Direction.UP:
			return (row - 1, col)
		elif direction == Direction.DOWN:
			return (row + 1, col)
		elif direction == Direction.LEFT:
			return (row, col - 1)
		else:
			return (row, col + 1)