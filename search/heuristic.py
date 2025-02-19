class Heuristic:
    @staticmethod
    def heuristic_function_v0(node : any) -> 'int':
        '''
            - Calculate the h(n) based on the node
            - h(n) would be the negative number of the
              number of wet pipes in the current state
        '''
        state = node.get_state()
        return -state.pump_water()
    

    @staticmethod
    def heuristic_function_v1(node : any) -> 'int':
        '''
            - Calculate the connection factor of a node
            - h(n) would return the sum of all connection factors
            - of all the pipes in the state of that node
        '''
        state = node.get_state()
        return -state.get_connection_factor()