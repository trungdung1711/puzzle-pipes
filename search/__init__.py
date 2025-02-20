from .search import Search
from .heuristic import Heuristic
from .ppproblem import PipePuzzleProblem
from .search import Result


search_algorithm = {
    1 : Search.breadth_first_search,
    2 : Search.depth_first_search,
    3 : Search.depth_limit_search,
    4 : Search.iterative_deepening_search,
    5 : Search.best_first_search
}


evaluation_function = {
    # Using the number of wet pipes
    1 : Heuristic.heuristic_function_1_v0, # negative
    2 : Heuristic.heuristic_function_1_v1, # 1 / number

    # Using the number of connection factor
    3 : Heuristic.heuristic_function_2_v0, # negative
    4 : Heuristic.heuristic_function_2_v1, # 1 / number

    5 : Heuristic.heuristic_function_2_v2, # goal - current
        # Using the connection factor
    6 : Heuristic.A_star_evaluation_function_1_v0, # positive + negative
    7 : Heuristic.A_star_evaluation_function_2_v0, # positive + 1 / number
    8 : Heuristic.A_start_evaluation_function_2_v1 # postitive + goal - current
}