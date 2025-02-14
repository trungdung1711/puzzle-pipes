from state.grid import Grid
from copy import *


class Problem:
    def __init__(self, initial: 'any'):
        self.__initial = initial


    def is_goal(self, state: 'any') -> 'bool':
        pass


    def actions(self, state: 'any') -> 'list':
        pass


    def result(self, state: 'any', action: 'any') -> 'any':
        pass


    def action_cost(self, state: 'any', action: 'any', new_state : 'any') -> 'int':
        pass


    def get_initial(self) -> 'any':
        return self.__initial


# state is Grid object
class PipePuzzleProblem(Problem):
    def __init__(self, initial):
        super().__init__(initial)


    def is_goal(self, state) -> 'bool':
        return state.is_goal_state()
    

    def actions(self, state):
        actions = []
        for i in range(4):
            for j in range(4):
                actions.append((i, j))
        return actions
    

    def result(self, state, action):
        new_state = deepcopy(state)
        new_state.get_pipe(action).change_direction()
        return new_state
    

    def action_cost(self, state, action, new_state):
        return 1