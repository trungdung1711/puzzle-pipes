class EvaluationFunction:
    @staticmethod
    def heuristic_function_1_v0(node : any) -> 'float':
        '''
            - Calculate the h(n) based on the node
            - h(n) would be the negative number of the
              number of wet pipes in the current state
        '''
        return - node.get_state().pump_water()
    

    @staticmethod
    def heuristic_function_2_v0(node : any) -> 'float':
        '''
            - Calculate the connection factor of a node
            - h(n) would return the sum of all connection factors
            - of all the pipes in the state of that node
        '''
        return - node.get_state().get_connection_factor()
    

    @staticmethod
    def heuristic_function_1_v1(node : any) -> 'float':
        '''
            - Calculate the h(n) based on the node
            - h(n) would not be the negative number of the
              number of wet pipes in the current state
            - Use 1 / number of wet pipes
            - More wet water -> estimate cost to be near the goal state
        '''
        return 1 / node.get_state().pump_water()


    @staticmethod
    def heuristic_function_2_v1(node : any) -> 'float':
        '''
            - Calculate the connection factor of a node
            - h(n) would return the sum of all connection factors
            - of all the pipes in the state of that node
            - Prevent negative heuristic function, thus using the fact 1 / h(n)
        '''
        return 1 / (1 + node.get_state().get_connection_factor())
    

    @staticmethod
    def heuristic_function_2_v2(node : any) -> 'int':
        '''
            - inadmissible heuristic 
            (overestimate the value, goal state does not mean all pipes are connected)
            - Calculate the substraction of the connection factor of goal state and
              connection factor of the current node
        '''
        return node.get_state().get_connection_factor_full() - node.get_state().get_connection_factor()

    @staticmethod
    def A_star_evaluation_function_1_v0(node : any) -> 'float':
        '''
            - The evaluation f(n) for A* search which is
            f(n) = g(n) + h(n)
            - g(n): path cost from initial state to node n
            - h(n): estimated cost of the shortest path from n to 
            goal state (no overestimate)
            - f(n): estimated cost of the best path (g(n))that continues from n to a goal (h(n))
        '''
        return node.get_path_cost() + EvaluationFunction.heuristic_function_2_v0(node)
    

    @staticmethod
    def A_star_evaluation_function_2_v0(node : any) -> 'float':
        '''
            - The evaluation f(n) for A* search which is
            f(n) = g(n) + h(n)
            - g(n): path cost from initial state to node n
            - h(n): estimated cost of the shortest path from n to 
            goal state (no overestimate) - using heuristic function 2 version 1
            - f(n): estimated cost of the best path (g(n))that continues from n to a goal (h(n))
        '''
        return node.get_path_cost() + EvaluationFunction.heuristic_function_2_v1(node)
    

    @staticmethod
    def A_star_evaluation_function_2_v1(node : any) -> 'int':
        '''
            - The evaluation f(n) for A* search which is
            f(n) = g(n) + h(n)
            - g(n): path cost from initial state to node n
            - h(n): estimated cost of the shortest path from n to 
            goal state (no overestimate) - using heuristic function 2 version 2
            - f(n): estimated cost of the best path (g(n))that continues from n to a goal (h(n))
        '''
        return node.get_path_cost() + EvaluationFunction.heuristic_function_2_v2(node)
    

    @staticmethod
    def A_star_evaluation_function_2_v2(node : any) -> 'int':
        '''
            - Weighted A*
        '''
        W = 3
        return node.get_path_cost() + W * EvaluationFunction.heuristic_function_2_v2(node)