class Heuristic:
    @staticmethod
    def simple_heuristic_function(node : any) -> 'int':
        '''
            - Calculate the h(n) based on the node
            - h(n) would be the negative number of the
              number of wet pipes in the current state
        '''
        state = node.get_state()
        return -state.pump_water()