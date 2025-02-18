from state.direction import Direction
from state.type import PipeType


# make up a state
class Pipe:
    PIPE_DICT = {
        PipeType.D : {
            Direction.U : [Direction.D],
            Direction.R : [Direction.L],
            Direction.D : [Direction.U],
            Direction.L : [Direction.R]
        },
        PipeType.S : {
            Direction.U : [Direction.U, Direction.D],
            Direction.R : [Direction.L, Direction.R],
            Direction.D : [Direction.U, Direction.D],
            Direction.L : [Direction.L, Direction.R]
        },
        PipeType.L : {
            Direction.U: [Direction.R, Direction.U],
            Direction.R: [Direction.D, Direction.R],
            Direction.D: [Direction.L, Direction.D],
            Direction.L: [Direction.U, Direction.L]
        },
        PipeType.T : {
            Direction.U: [Direction.D, Direction.L, Direction.R],
            Direction.R: [Direction.L, Direction.U, Direction.D],
            Direction.D: [Direction.U, Direction.L, Direction.R],
            Direction.L: [Direction.R, Direction.U, Direction.D]
        }
    }


    def __init__(self, type: 'PipeType', direction: 'Direction', location: tuple):
        self.__type = type
        self.__direction = direction
        self.__location = location


    def get_type(self) -> 'PipeType':
        return self.__type
    
    
    def set_type(self, type: 'PipeType'):
        self.__type = type
    

    def get_direction(self) -> 'Direction':
        return self.__direction
    

    def set_direction(self, direction: 'Direction'):
        self.__direction = direction


    def get_location(self) -> 'tuple':
        return self.__location


    def show(self):
        print(f'[{self.__type.name},{self.__direction.name}]')


    def to_tuple(self) -> 'tuple':
        return (self.__type.value, self.__direction.value)


    def change_direction(self):
        if self.__direction == Direction.U:
            self.__direction = Direction.R
        elif self.__direction == Direction.R:
            self.__direction = Direction.D
        elif self.__direction == Direction.D:
            self.__direction = Direction.L
        elif self.__direction == Direction.L:
            self.__direction = Direction.U


    def get_can_flow_direction(self) -> 'list':
        return self.PIPE_DICT[self.__type][self.__direction]


    def is_connected_with_neighbour(self, neighbour: 'Pipe', move_direction: 'Direction') -> 'bool':
        if Direction.opposite(move_direction) in neighbour.get_can_flow_direction():
            return True
        return False
    

    def get_connected_pipes(self, grid) -> 'list':
        neighbours = []
        possible_directions = self.get_can_flow_direction()
        for direction in possible_directions:
            next_location = Direction.get_next_location(self.__location, direction)
            next_row, next_col = next_location
            if (next_row < 0 or next_row > 3 or next_col < 0 or next_col > 3):
                continue
            # valid next_location
            neighbour = grid.get_pipe(next_location)
            if self.is_connected_with_neighbour(neighbour, direction):
                neighbours.append(neighbour)
        return neighbours
    

    # def __eq__(self, value):
    #     if isinstance(value, 'Pipe'):
    #         return self.get_type() == value.get_type() and self.get_direction() == value.get_direction()
        

if __name__ == '__main__':
    pipe = Pipe(PipeType.L, Direction.U, (0,0))
    print(pipe.to_tuple())