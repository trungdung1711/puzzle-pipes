from .search import Search
from .evalfunction import EvaluationFunction
from .ppproblem import PipePuzzleProblem
from .search import Result
from .ppproblem import PPP


search_algorithm = {
    1 : Search.breadth_first_search,
    2 : Search.depth_first_search_s1,
    3 : Search.depth_limit_search_s1,
    4 : Search.iterative_deepening_search,
    5 : Search.best_first_search,

    6 : Search.depth_first_search_s2,
    7 : Search.depth_limit_search_s2
}


evaluation_function = {
    1 : EvaluationFunction.s1_hn_minus_number_of_wet_pipe, # negative
    2 : EvaluationFunction.s1_hn_one_over_number_wet_pipe, # 1 / number

    3 : EvaluationFunction.s1_hn_minus_number_of_connection_factor, # negative
    4 : EvaluationFunction.s1_hn_one_over_connection_factor, # 1 / number

    5 : EvaluationFunction.s1_hn_remain_cost_based_on_connection_factor, # goal - current

    6 : EvaluationFunction.s1_fn_path_cost_and_minus_number_of_connection_factor, # positive + negative
    7 : EvaluationFunction.s1_fn_path_cost_and_one_over_connection_factor, # positive + 1 / number

    8 : EvaluationFunction.s1_fn_path_cost_and_remain_cost_based_on_connection_factor, # postitive + goal - current
    9 : EvaluationFunction.s1_fn_path_cost_and_w_remain_cost_based_on_connection_factor, # positive + w * (goal - current)

    # pure heuristic
    10: EvaluationFunction.s2_hn_remain_cost_based_on_connection_factor,
    # A*
    11: EvaluationFunction.s2_fn_path_cost_and_w_remain_cost_based_on_connection_factor
}