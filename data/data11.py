from state.pipe import Pipe
from state.grid import Grid
from state.direction import Direction
from state.type import PipeType


def data11() -> Grid:
    grid = Grid()
    
    pipe00 = Pipe(PipeType.D, Direction.D, (0, 0))
    pipe01 = Pipe(PipeType.L, Direction.R, (0, 1))
    pipe02 = Pipe(PipeType.D, Direction.L, (0, 2))
    pipe03 = Pipe(PipeType.D, Direction.L, (0, 3))

    pipe10 = Pipe(PipeType.L, Direction.U, (1, 0))
    pipe11 = Pipe(PipeType.T, Direction.U, (1, 1))
    pipe12 = Pipe(PipeType.T, Direction.D, (1, 2))
    pipe13 = Pipe(PipeType.T, Direction.U, (1, 3))

    pipe20 = Pipe(PipeType.D, Direction.R, (2, 0))
    pipe21 = Pipe(PipeType.T, Direction.D, (2, 1))
    pipe22 = Pipe(PipeType.T, Direction.U, (2, 2))
    pipe23 = Pipe(PipeType.D, Direction.R, (2, 3))

    pipe30 = Pipe(PipeType.D, Direction.R, (3, 0))
    pipe31 = Pipe(PipeType.D, Direction.R, (3, 1))
    pipe32 = Pipe(PipeType.L, Direction.L, (3, 2))
    pipe33 = Pipe(PipeType.D, Direction.U, (3, 3))

    grid.set_pipe(0, 0, pipe00)
    grid.set_pipe(0, 1, pipe01)
    grid.set_pipe(0, 2, pipe02)
    grid.set_pipe(0, 3, pipe03)

    grid.set_pipe(1, 0, pipe10)
    grid.set_pipe(1, 1, pipe11)
    grid.set_pipe(1, 2, pipe12)
    grid.set_pipe(1, 3, pipe13)

    grid.set_pipe(2, 0, pipe20)
    grid.set_pipe(2, 1, pipe21)
    grid.set_pipe(2, 2, pipe22)
    grid.set_pipe(2, 3, pipe23)

    grid.set_pipe(3, 0, pipe30)
    grid.set_pipe(3, 1, pipe31)
    grid.set_pipe(3, 2, pipe32)
    grid.set_pipe(3, 3, pipe33)
    return grid