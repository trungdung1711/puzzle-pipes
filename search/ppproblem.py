from .problem import Problem
from copy import *
from state.grid import Grid
from state import PipeTouch
from state import LOCATION
from typing import List
from typing import Dict
from typing import Tuple


# state is Grid object
class PipePuzzleProblem(Problem):
    def __init__(self, initial : 'Grid'):
        super().__init__(initial)


    def is_goal(self, state : 'Grid') -> 'bool':
        return state.is_goal_state()
    

    def actions(self, state : 'Grid'):
        return LOCATION
    

    def result(self, state : 'Grid', action : 'tuple'):
        new_state = deepcopy(state)
        new_state.get_pipe(action).right_rotate()
        return new_state
    

    def action_cost(self, state : 'Grid', action : 'tuple', new_state : 'Grid'):
        return 1
    

# state is 
class PPP(Problem):
    def __init__(self, initial : PipeTouch):
        super().__init__(initial)


    def is_goal(self, state : PipeTouch) -> 'bool':
        return state.is_goal_state()
    

    # different from Grid state
    def actions(self, state : PipeTouch) -> List[Tuple[int, int]]:
        return LOCATION


    def result(self, state : PipeTouch, action : Tuple[int, int]):
        new_state = deepcopy(state)
        new_state.touch(action)
        return new_state
    

    def action_cost(self, state : PipeTouch, action : Tuple[int, int], new_state : PipeTouch):
        return 1