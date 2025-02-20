from .problem import Problem
from copy import *
from state.grid import Grid


# state is Grid object
class PipePuzzleProblem(Problem):
    def __init__(self, initial : 'Grid'):
        super().__init__(initial)


    def is_goal(self, state : 'Grid') -> 'bool':
        return state.is_goal_state()
    

    def actions(self, state : 'Grid'):
        actions = []
        for i in range(4):
            for j in range(4):
                actions.append((i, j))
        return actions
    

    def result(self, state : 'Grid', action : 'tuple'):
        new_state = deepcopy(state)
        new_state.get_pipe(action).right_rotate()
        return new_state
    

    def action_cost(self, state : 'Grid', action : 'tuple', new_state : 'Grid'):
        return 1