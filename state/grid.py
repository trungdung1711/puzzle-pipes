from state.pipe import Pipe


class Grid:
    def __init__(self):
        self.__grid = [[None for _ in range(4)] for _ in range(4)]


    def set_pipe(self, row: int, col: int, pipe: Pipe):
        if 0 <= row < 4 and 0 <= col < 4:
            self.__grid[row][col] = pipe
        else:
            raise IndexError("Grid position out of range")
        


    def get_pipe(self, row: int, col: int) -> Pipe:
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