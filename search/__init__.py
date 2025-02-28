from .search import Search
from .heuristic import EvaluationFunction
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
    1 : EvaluationFunction.heuristic_function_1_v0, # negative
    2 : EvaluationFunction.heuristic_function_1_v1, # 1 / number

    # Using the number of connection factor
    3 : EvaluationFunction.heuristic_function_2_v0, # negative
    4 : EvaluationFunction.heuristic_function_2_v1, # 1 / number

    # main and the most effective h(n)
    5 : EvaluationFunction.heuristic_function_2_v2, # goal - current
        # Using the connection factor
    6 : EvaluationFunction.A_star_evaluation_function_1_v0, # positive + negative
    7 : EvaluationFunction.A_star_evaluation_function_2_v0, # positive + 1 / number

    # problem of heuristic drift
    8 : EvaluationFunction.A_star_evaluation_function_2_v1, # postitive + goal - current

    9 : EvaluationFunction.A_star_evaluation_function_2_v2
}