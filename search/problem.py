from abc import ABC


class Problem(ABC):
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