class EvaluationFunction:
    
    @staticmethod
    def s1_hn_minus_number_of_wet_pipe(node : any) -> 'float':
        '''
            - Calculate the h(n) based on the node
            - h(n) would be the negative number of the
              number of wet pipes in the current state
        '''
        return - node.get_state().pump_water()
    

    @staticmethod
    def s1_hn_minus_number_of_connection_factor(node : any) -> 'float':
        '''
            - Calculate the connection factor of a node
            - h(n) would return the sum of all connection factors
            - of all the pipes in the state of that node
        '''
        return - node.get_state().get_connection_factor()
    

    @staticmethod
    def s1_hn_one_over_number_wet_pipe(node : any) -> 'float':
        '''
            - Calculate the h(n) based on the node
            - h(n) would not be the negative number of the
              number of wet pipes in the current state
            - Use 1 / number of wet pipes
            - More wet water -> estimate cost to be near the goal state
        '''
        return 1 / node.get_state().pump_water()


    @staticmethod
    def s1_hn_one_over_connection_factor(node : any) -> 'float':
        '''
            - Calculate the connection factor of a node
            - h(n) would return the sum of all connection factors
            - of all the pipes in the state of that node
            - Prevent negative heuristic function, thus using the fact 1 / h(n)
        '''
        return 1 / (1 + node.get_state().get_connection_factor())
    

    @staticmethod
    def s1_hn_remain_cost_based_on_connection_factor(node : any) -> 'int':
        '''
            - inadmissible heuristic 
            (overestimate the value, goal state does not mean all pipes are connected)
            - Calculate the substraction of the connection factor of goal state and
              connection factor of the current node
        '''
        return node.get_state().get_connection_factor_full() - node.get_state().get_connection_factor()


    @staticmethod
    def s1_fn_path_cost_and_minus_number_of_connection_factor(node : any) -> 'float':
        '''
            - The evaluation f(n) for A* search which is
            f(n) = g(n) + h(n)
            - g(n): path cost from initial state to node n
            - h(n): estimated cost of the shortest path from n to 
            goal state (no overestimate)
            - f(n): estimated cost of the best path (g(n))that continues from n to a goal (h(n))
        '''
        return node.get_path_cost() + EvaluationFunction.s1_hn_minus_number_of_connection_factor(node)
    

    @staticmethod
    def s1_fn_path_cost_and_one_over_connection_factor(node : any) -> 'float':
        '''
            - The evaluation f(n) for A* search which is
            f(n) = g(n) + h(n)
            - g(n): path cost from initial state to node n
            - h(n): estimated cost of the shortest path from n to 
            goal state (no overestimate) - using heuristic function 2 version 1
            - f(n): estimated cost of the best path (g(n))that continues from n to a goal (h(n))
        '''
        return node.get_path_cost() + EvaluationFunction.s1_hn_one_over_connection_factor(node)
    

    @staticmethod
    def s1_fn_path_cost_and_remain_cost_based_on_connection_factor(node : any) -> 'int':
        '''
            - The evaluation f(n) for A* search which is
            f(n) = g(n) + h(n)
            - g(n): path cost from initial state to node n
            - h(n): estimated cost of the shortest path from n to 
            goal state (no overestimate) - using heuristic function 2 version 2
            - f(n): estimated cost of the best path (g(n))that continues from n to a goal (h(n))
        '''
        return node.get_path_cost() + EvaluationFunction.s1_hn_remain_cost_based_on_connection_factor(node)
    

    @staticmethod
    def s1_fn_path_cost_and_w_remain_cost_based_on_connection_factor(node : any) -> 'int':
        '''
            - Weighted A*
        '''
        W = 3
        return node.get_path_cost() + W * EvaluationFunction.s1_hn_remain_cost_based_on_connection_factor(node)
    

    @staticmethod
    def s2_hn_remain_cost_based_on_connection_factor(node : any) -> 'int':
        '''
            - inadmissible heuristic 
            (overestimate the value, goal state does not mean all pipes are connected)
            - Calculate the substraction of the connection factor of goal state and
              connection factor of the current node

            - Used for state 2
        '''
        return node.get_state().getGrid().get_connection_factor_full() - node.get_state().getGrid().get_connection_factor()
    

    @staticmethod
    def s2_fn_path_cost_and_w_remain_cost_based_on_connection_factor(node : any) -> 'int':
        '''
            - Weighted A*
            - state 2
        '''
        W = 3
        return node.get_path_cost() + W * EvaluationFunction.s2_hn_remain_cost_based_on_connection_factor(node)