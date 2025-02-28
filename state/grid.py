from state.type import PipeType
from util.stack import Stack
from state.pipe import Pipe
from util import FIFOQueue


# state
class Grid:
    def __init__(self):
        self.__grid = [[None for _ in range(4)] for _ in range(4)]
        self.__destionation_list : list = []
        self.__connection_factor : int = 0


    def set_pipe(self, row: int, col: int, pipe: 'Pipe'):
        if 0 <= row < 4 and 0 <= col < 4:
            self.__grid[row][col] = pipe
            self.__connection_factor += pipe.get_number_of_flow_direction()
            if pipe.get_type() == PipeType.D:
                self.__destionation_list.append(pipe.get_location())
        else:
            raise IndexError("Grid position out of range")


    def get_pipe(self, location: tuple) -> Pipe:
        row, col = location
        if 0 <= row < 4 and 0 <= col < 4:
            return self.__grid[row][col]
        else:
            raise IndexError("Grid position out of range")
        

    def get_grid(self) -> list:
        return self.__grid
    

    def print(self):
        for row in self.__grid:
            for pipe in row:
                pipe.show()


    def get_destinations(self) -> 'list':
        return self.__destionation_list


    def get_source(self) -> 'Pipe':
        return self.__grid[2][2]
    

    def to_tuple(self):
        return tuple(tuple(pipe.to_tuple() for pipe in row ) for row in self.__grid)


    def is_goal_state(self) -> 'bool':
        stack = Stack()
        reached = set()
        parent = {}

        # initialisation
        stack.push(self.get_source())
        reached.add(self.get_source())
        parent[self.get_source()] = None

        while not stack.is_empty():
            current_pipe = stack.pop()
            connected_neighbours = current_pipe.get_connected_pipes(self)

            for neighbour in connected_neighbours:
                if neighbour in reached and parent[current_pipe] != neighbour:
                    return False
                elif neighbour in reached and parent[current_pipe] == neighbour:
                    continue
                else:
                    stack.push(neighbour)
                    reached.add(neighbour)

                    parent[neighbour] = current_pipe


        for location in self.get_destinations():
            if self.get_pipe(location) not in reached:
                return False
        return True
    

    def pump_water(self) -> 'int':
        number_wet_pipe = 0
        queue = FIFOQueue()
        reached = set()

        queue.push(self.get_source())
        reached.add(self.get_source())
        number_wet_pipe += 1

        while not queue.is_empty():
            pipe = queue.pop()
            connected_pipes = pipe.get_connected_pipes(self)

            for neighbour in connected_pipes:
                if neighbour in reached:
                    continue
                else:
                    # we never pump water to this pipe
                    queue.push(neighbour)
                    reached.add(neighbour)
                    number_wet_pipe += 1
        return number_wet_pipe
    

    def get_connection_factor(self) -> 'int':
        connection_factor = 0
        for row in self.get_grid():
            for pipe in row:
                connection_factor += pipe.get_connection_factor(self)
        return connection_factor
    

    def get_connection_factor_full(self) -> 'int':
        return self.__connection_factor