from state.pipe import Pipe
from state.grid import Grid
from state.direction import Direction
from state.type import PipeType


def data1() -> Grid:
    pipe00 = Pipe(PipeType.STRAIGHT_DESTINATION, Direction.UP)
    pipe01 = Pipe(PipeType.T_SHAPE, Direction.RIGHT)
    pipe02 = Pipe(PipeType.T_SHAPE, Direction.LEFT)
    pipe03 = Pipe(PipeType.L_SHAPE, Direction.UP)

    pipe10 = Pipe(PipeType.STRAIGHT_DESTINATION, Direction.DOWN)
    pipe11 = Pipe(PipeType.L_SHAPE, Direction.LEFT)
    pipe12 = Pipe(PipeType.STRAIGHT, Direction.RIGHT)
    pipe13 = Pipe(PipeType.STRAIGHT_DESTINATION, Direction.DOWN)

    pipe20 = Pipe(PipeType.STRAIGHT_DESTINATION, Direction.UP)
    pipe21 = Pipe(PipeType.T_SHAPE, Direction.UP)
    pipe22 = Pipe(PipeType.T_SHAPE, Direction.LEFT)
    pipe23 = Pipe(PipeType.L_SHAPE, Direction.UP)

    pipe30 = Pipe(PipeType.STRAIGHT_DESTINATION, Direction.DOWN)
    pipe31 = Pipe(PipeType.T_SHAPE, Direction.RIGHT)
    pipe32 = Pipe(PipeType.STRAIGHT_DESTINATION, Direction.UP)
    pipe33 = Pipe(PipeType.STRAIGHT_DESTINATION, Direction.RIGHT)

    grid = Grid()
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