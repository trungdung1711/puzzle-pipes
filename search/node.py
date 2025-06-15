class Node:
    def __init__(self, state: 'any', parent: 'Node', action: 'any', path_cost: int):
        self.__state = state
        self.__parent = parent
        self.__action = action
        self.__path_cost = path_cost


    def get_state(self) -> 'any':
        return self.__state
    

    def set_state(self, state: 'any'):
        self.__state = state
    

    def get_parent(self) -> 'Node':
        return self.__parent
    

    def set_parent(self, parent: 'Node'):
        self.__parent = parent
    

    def get_action(self) -> 'any':
        return self.__action
    

    def set_action(self, action: 'any'):
        self.__action = action
    

    def get_path_cost(self) -> 'int':
        return self.__path_cost
    

    def set_path_cost(self, path_cost: 'int'):
        self.__path_cost = path_cost
    

    def __lt__(self, other):
        return True