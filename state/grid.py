from state.type import PipeType
from state.stack import Stack
from state.pipe import Pipe


class Grid:
    def __init__(self):
        self.__grid = [[None for _ in range(4)] for _ in range(4)]


    def set_pipe(self, row: int, col: int, pipe: 'Pipe'):
        if 0 <= row < 4 and 0 <= col < 4:
            self.__grid[row][col] = pipe
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
        destination_list = []
        for row in self.__grid:
            for pipe in row:
                if pipe.get_type() == PipeType.STRAIGHT_DESTINATION:
                    destination_list.append(pipe)
        return destination_list


    def get_source(self) -> 'Pipe':
        return self.__grid[2][2]


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
                    # loop
                    print('Loop detection')
                    return False
                elif neighbour in reached and parent[current_pipe] == neighbour:
                    # just passing
                    continue
                else:
                    # normal
                    stack.push(neighbour)
                    reached.add(neighbour)
                    parent[neighbour] = current_pipe


        for pipe in self.get_destinations():
            if pipe not in reached:
                return False
        return True