from data1 import data1
from state.pipe import Pipe
from state.direction import Direction
from state.type import PipeType


grid = data1()

pipe1 = Pipe(PipeType.L_SHAPE, Direction.DOWN)
pipe2 = Pipe(PipeType.T_SHAPE, Direction.DOWN)
print(pipe1.is_connected_with_neighbour(pipe2, Direction.DOWN))

print(pipe2.get_can_flow_direction())