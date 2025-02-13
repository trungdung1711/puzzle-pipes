from state.direction import Direction
from state.type import PipeType


class Pipe:
    PIPE_DICT = {
        PipeType.STRAIGHT_DESTINATION : {
            Direction.UP : [Direction.DOWN],
            Direction.RIGHT : [Direction.LEFT],
            Direction.DOWN : [Direction.UP],
            Direction.LEFT : [Direction.RIGHT]
        },
        PipeType.STRAIGHT : {
            Direction.UP : [Direction.UP, Direction.DOWN],
            Direction.RIGHT : [Direction.LEFT, Direction.RIGHT],
            Direction.DOWN : [Direction.UP, Direction.DOWN],
            Direction.LEFT : [Direction.LEFT, Direction.RIGHT]
        },
        PipeType.L_SHAPE : {
            Direction.UP: [Direction.RIGHT, Direction.UP],
            Direction.RIGHT: [Direction.DOWN, Direction.RIGHT],
            Direction.DOWN: [Direction.LEFT, Direction.DOWN],
            Direction.LEFT: [Direction.UP, Direction.LEFT]
        },
                PipeType.T_SHAPE : {
            Direction.UP: [Direction.DOWN, Direction.LEFT, Direction.RIGHT],
            Direction.RIGHT: [Direction.LEFT, Direction.UP, Direction.DOWN],
            Direction.DOWN: [Direction.UP, Direction.LEFT, Direction.RIGHT],
            Direction.LEFT: [Direction.RIGHT, Direction.UP, Direction.DOWN]
        }
    }


    def __init__(self, type: 'PipeType', direction: 'Direction'):
        self.__type = type
        self.__direction = direction


    def get_type(self) -> 'PipeType':
        return self.__type
    
    
    def set_type(self, type: 'PipeType'):
        self.__type = type
    

    def get_direction(self) -> 'Direction':
        return self.__direction
    

    def set_direction(self, direction: 'Direction'):
        self.__direction = direction


    def show(self):
        print(f'[{self.__type.name},{self.__direction.name}]')


    def change_direction(self):
        if self.__direction == Direction.UP:
            self.__direction = Direction.RIGHT
        elif self.__direction == Direction.RIGHT:
            self.__direction = Direction.DOWN
        elif self.__direction == Direction.DOWN:
            self.__direction = Direction.LEFT
        elif self.__direction == Direction.LEFT:
            self.__direction = Direction.UP


    def get_can_flow_direction(self) -> 'list':
        return self.PIPE_DICT[self.__type][self.__direction]


    def is_connected_with_neighbour(self, neighbour: 'Pipe', move_direction: 'Direction'):
        if Direction.opposite(move_direction) in neighbour.get_can_flow_direction():
            return True
        return False