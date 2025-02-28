from typing import Dict
from state.grid import Grid
from typing import Tuple


LOCATION = [
    (0, 0),
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 0),
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 0),
    (2, 1),
    (2, 2),
    (2, 3),
    (3, 0),
    (3, 1),
    (3, 2),
    (3, 3)
]


# state
class PipeTouch:
    def __init__(self, grid : Grid):
        self.__touch : Dict[Tuple[int, int], int] = {
            (0, 0) : 0,
            (0, 1) : 0,
            (0, 2) : 0,
            (0, 3) : 0,
            (1, 0) : 0,
            (1, 1) : 0,
            (1, 2) : 0,
            (1, 3) : 0,
            (2, 0) : 0,
            (2, 1) : 0,
            (2, 2) : 0,
            (2, 3) : 0,
            (3, 0) : 0,
            (3, 1) : 0,
            (3, 2) : 0,
            (3, 3) : 0
        }
        self.__grid : Grid = grid


    def getTouch(self) -> Dict[int, int]:
        return self.__touch
    

    def getGrid(self) -> Grid:
        return self.__grid
    

    def is_goal_state(self) -> bool:
        return self.getGrid().is_goal_state()
    

    def touch(self, location : Tuple[int, int]):
        self.getTouch()[location] = (self.getTouch()[location] + 1) % 4
        self.getGrid().get_pipe(location).right_rotate()


    def to_tuple(self) -> Tuple:
        return tuple(self.__touch.values())