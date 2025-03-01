from state.direction import Direction
from state.type import PipeType


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
            - not heuristic
        '''
        W = 3
        return node.get_path_cost() + W * EvaluationFunction.s1_hn_remain_cost_based_on_connection_factor(node)
    

    @staticmethod
    def s2_hn_remain_cost_based_on_connection_factor(node : any) -> 'int':
        '''
            - not heuristic
        '''
        return node.get_state().get_grid().get_connection_factor_full() - node.get_state().get_grid().get_connection_factor()
    

    @staticmethod
    def s2_fn_path_cost_and_w_remain_cost_based_on_connection_factor(node : any) -> 'int':
        '''
            - not heuristic
        '''
        W = 3
        return node.get_path_cost() + W * EvaluationFunction.s2_hn_remain_cost_based_on_connection_factor(node)
    

    @staticmethod
    def s2_hn_number_of_unwet_pipe(node : any) -> 'float':
        '''
            - unusable
        '''
        return 16 - node.get_state().get_grid().pump_water()
    

    @staticmethod
    def s2_fn_path_cost_and_number_of_unwet_pipe(node : any) -> 'float':
        '''
            - unusable
        '''
        return node.get_path_cost() + 2 * EvaluationFunction.s2_hn_number_of_unwet_pipe(node)
    

    @staticmethod
    def s2_hn_estimated_remain_cost_state_to_goal(node : any) -> 'float':
        '''
            - may be inadmissible
        '''
        grid = node.get_state().get_grid()
        remain : int = 0

        for location in REMAIN_COST:
            pipe = grid.get_pipe(location)
            remain += REMAIN_COST[location][pipe.get_type()][pipe.get_direction()]

        for row in grid.get_grid():
            for pipe in row:
                if pipe.get_connection_factor(grid) < pipe.get_number_of_flow_direction():
                    remain += pipe.get_number_of_flow_direction()
        
        return remain
        

    @staticmethod
    def s2_fn_path_cost_and_estimated_remain_cost_state_to_goal(node : any) -> 'float':
        '''
            - A* with estimated remain cost to the goal
        '''
        return node.get_path_cost() + EvaluationFunction.s2_hn_estimated_remain_cost_state_to_goal(node)
    

    @staticmethod
    def s2_fn_path_cost_and_weighted_estimated_remain_cost_state_to_goal(node : any) -> 'float':
        '''
            - A* with weighed on heuristic
        '''
        W = 4
        return node.get_path_cost() + W * EvaluationFunction.s2_hn_estimated_remain_cost_state_to_goal(node)
    

REMAIN_COST = {
    (0, 0) : {
        PipeType.D : {
            Direction.U : 0,
            Direction.R : 2,
            Direction.D : 1,
            Direction.L : 0
        },
        PipeType.L : {
            Direction.U : 1,
            Direction.R : 0,
            Direction.D : 3,
            Direction.L : 2
        }
    },
    (0, 1) : {
        PipeType.D : {
            Direction.U : 0,
            Direction.R : 0,
            Direction.D : 1,
            Direction.L : 0
        },
        PipeType.L : {
            Direction.U : 1,
            Direction.R : 0,
            Direction.D : 0,
            Direction.L : 2
        },
        PipeType.T : {
            Direction.U : 0,
            Direction.R : 3,
            Direction.D : 2,
            Direction.L : 1
        },
        PipeType.S : {
            Direction.U : 1,
            Direction.R : 0,
            Direction.D : 1,
            Direction.L : 0
        }
    },
    (0, 2) : {
        PipeType.D : {
            Direction.U : 0,
            Direction.R : 0,
            Direction.D : 1,
            Direction.L : 0
        },
        PipeType.L : {
            Direction.U : 1,
            Direction.R : 0,
            Direction.D : 0,
            Direction.L : 2
        },
        PipeType.T : {
            Direction.U : 0,
            Direction.R : 3,
            Direction.D : 2,
            Direction.L : 1
        },
        PipeType.S : {
            Direction.U : 1,
            Direction.R : 0,
            Direction.D : 1,
            Direction.L : 0
        }
    },
    (1, 0) : {
        PipeType.D : {
            Direction.U : 0,
            Direction.R : 1,
            Direction.D : 0,
            Direction.L : 0
        },
        PipeType.L : {
            Direction.U : 0,
            Direction.R : 0,
            Direction.D : 2,
            Direction.L : 1
        },
        PipeType.T : {
            Direction.U : 3,
            Direction.R : 2,
            Direction.D : 1,
            Direction.L : 0
        },
        PipeType.S : {
            Direction.U : 0,
            Direction.R : 1,
            Direction.D : 0,
            Direction.L : 1
        }
    },
    (2, 0) : {
        PipeType.D : {
            Direction.U : 0,
            Direction.R : 1,
            Direction.D : 0,
            Direction.L : 0
        },
        PipeType.L : {
            Direction.U : 0,
            Direction.R : 0,
            Direction.D : 2,
            Direction.L : 1
        },
        PipeType.T : {
            Direction.U : 3,
            Direction.R : 2,
            Direction.D : 1,
            Direction.L : 0
        },
        PipeType.S : {
            Direction.U : 0,
            Direction.R : 1,
            Direction.D : 0,
            Direction.L : 1
        }
    },
    (1, 3) : {
        PipeType.D : {
            Direction.U : 0,
            Direction.R : 0,
            Direction.D : 0,
            Direction.L : 1
        },
        PipeType.L : {
            Direction.U : 2,
            Direction.R : 1,
            Direction.D : 0,
            Direction.L : 0
        },
        PipeType.T : {
            Direction.U : 1,
            Direction.R : 0,
            Direction.D : 3,
            Direction.L : 2
        },
        PipeType.S : {
            Direction.U : 0,
            Direction.R : 1,
            Direction.D : 0,
            Direction.L : 1
        }
    },
    (2, 3) : {
        PipeType.D : {
            Direction.U : 0,
            Direction.R : 0,
            Direction.D : 0,
            Direction.L : 1
        },
        PipeType.L : {
            Direction.U : 2,
            Direction.R : 1,
            Direction.D : 0,
            Direction.L : 0
        },
        PipeType.T : {
            Direction.U : 1,
            Direction.R : 0,
            Direction.D : 3,
            Direction.L : 2
        },
        PipeType.S : {
            Direction.U : 0,
            Direction.R : 1,
            Direction.D : 0,
            Direction.L : 1
        }
    },
    (3, 1) : {
        PipeType.D : {
            Direction.U : 1,
            Direction.R : 0,
            Direction.D : 0,
            Direction.L : 0
        },
        PipeType.L : {
            Direction.U : 0,
            Direction.R : 2,
            Direction.D : 1,
            Direction.L : 0
        },
        PipeType.T : {
            Direction.U : 2,
            Direction.R : 1,
            Direction.D : 0,
            Direction.L : 3
        },
        PipeType.S : {
            Direction.U : 1,
            Direction.R : 0,
            Direction.D : 1,
            Direction.L : 0
        }
    },
    (3, 2) : {
        PipeType.D : {
            Direction.U : 1,
            Direction.R : 0,
            Direction.D : 0,
            Direction.L : 0
        },
        PipeType.L : {
            Direction.U : 0,
            Direction.R : 2,
            Direction.D : 1,
            Direction.L : 0
        },
        PipeType.T : {
            Direction.U : 2,
            Direction.R : 1,
            Direction.D : 0,
            Direction.L : 3
        },
        PipeType.S : {
            Direction.U : 1,
            Direction.R : 0,
            Direction.D : 1,
            Direction.L : 0
        }
    },
    (3, 3) : {
        PipeType.D : {
            Direction.U : 1,
            Direction.R : 0,
            Direction.D : 0,
            Direction.L : 2
        },
        PipeType.L : {
            Direction.U : 3,
            Direction.R : 2,
            Direction.D : 1,
            Direction.L : 0
        }
    },
    (0, 3) : {
        PipeType.D : {
            Direction.U : 0,
            Direction.R : 0,
            Direction.D : 2,
            Direction.L : 1
        },
        PipeType.L : {
            Direction.U : 2,
            Direction.R : 1,
            Direction.D : 0,
            Direction.L : 3
        }
    },
    (3, 0) : {
        PipeType.D : {
            Direction.U : 2,
            Direction.R : 1,
            Direction.D : 0,
            Direction.L : 3
        },
        PipeType.L : {
            Direction.U : 0,
            Direction.R : 3,
            Direction.D : 2,
            Direction.L : 1
        }
    }
}