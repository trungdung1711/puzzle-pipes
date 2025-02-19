from data.data1 import data1
from data.data2 import data2
from data.data3 import data3
from data.data4 import data4
from data.data5 import data5
from data.data6 import data6
from data.data7 import data7
from data.data8 import data8
from data.data9 import data9
from data.data10 import data10
from data.data11 import data11
from data.data12 import data12
from data.data13 import data13
from data.data14 import data14
from data.data15 import data15
from data.data16 import data16
from data.data17 import data17

from search.problem import *
from search.node import *
from search.search import *
from game.game import display
from search.heuristic import Heuristic

                    # problem with negative h(n) https://stackoverflow.com/questions/30067813/are-heuristic-functions-that-produce-negative-values-inadmissible
                    #           Uninformed                                           Informed    
                    # BFS           DLS             GBFS1_v0(-)                GBFS1_v1 (1/)                       GBFS2_v0(-)                                 GBFS2_v1_v2(1/)              A* [ negative h(n) -> causing problem]          A* [ g(n) and possitive h(n) -> still causing problem ]
grid1 = data1()     #                               OK                                   [ out of memory ]             OK                                        OK [ faster ]                           [ out of memory ]                         [ out of memory ]
grid2 = data2()     # OK                            OK                                OK                               OK                                        OK                                   OK                                        OK
grid3 = data3()     # OK            OK              OK                                OK                               OK                                        OK                                   OK                                        OK
grid4 = data4()     # OK                            OK                                OK                               OK                                        OK                                   OK                                        OK
grid5 = data5()     # OK            OK              OK                                OK                               OK                                        OK                                   OK                                        OK
grid6 = data6()     #                                                                 OK                               OK                                        OK                                   OK                                        OK
grid7 = data7()     #                                                                                                  OK                                        OK                                   OK [ long time ]                          OK [ out of memory ]
grid8 = data8()     # OK            OK              OK                                OK                               OK                                        OK                                   OK                                           [ out of memory ]
grid9 = data9()     # OK                            OK                                OK                               OK                                        OK                                   OK                                        OK [ out of memory ]
grid10 = data10()   #               OK              OK                                OK                               OK                                        OK                                   OK                                        OK
grid12 = data12()   #                               OK                                OK                               OK                                        OK                                   OK                                        OK [ out of memory ]
grid13 = data13()   #                               OK                                OK [ long time]                  OK [ faster and better solution ]         OK [ faster and better solution ]    OK [ longer but better solution]          OK [ out of memory ]
# real puzzles       from https://www.puzzle-pipes.com/
grid11 = data11()   #                               OK []                             OK                               OK [ faster ]                             OK                                      [ out of memory ]                         [ out of memory ]
grid14 = data14()   #                               OK                                OK                               OK [ faster ]                             OK                                   OK [ out of memory ]                         [ out of memory ]
grid15 = data15()   #                               OK [ long time]                   OK [ faster time ]               OK [ faster and better solution ]         OK [ faster and better solution ]       [ out of memory ]                         [ out of memory ]
grid16 = data16()   #                               OK                                OK                               OK [ faster ]                             OK                                   OK                                           [ out of memory ]
grid17 = data17()   #                               OK [ better solution]             OK [ better solution]            OK                                        OK                                   OK                                           [ out of memory ]

if __name__ == '__main__':

    pipe_puzzle_problem = PipePuzzleProblem(grid17)

    # solution_node = Search.breadth_first_search(pipe_puzzle_problem)
    # solution_node = Search.depth_first_search(pipe_puzzle_problem)
    # solution_node = Search.iterative_deepening_search(pipe_puzzle_problem, limit=30)
    # solution_node = Search.depth_limit_search(pipe_puzzle_problem, l = 7)
    # solution_node = Search.best_first_search(pipe_puzzle_problem, evaluation_function=Heuristic.heuristic_function_v1)
    # solution_node = Search.best_first_search(pipe_puzzle_problem, evaluation_function=Heuristic.A_star_evaluation_function_1_v0)
    # solution_node = Search.best_first_search(pipe_puzzle_problem, evaluation_function=Heuristic.heuristic_function_1_v1)
    # solution_node = Search.best_first_search(pipe_puzzle_problem, evaluation_function=Heuristic.heuristic_function_2_v1)
    # solution_node = Search.best_first_search(pipe_puzzle_problem, evaluation_function=Heuristic.A_star_evaluation_function_2_v0)
    solution_node = Search.best_first_search(pipe_puzzle_problem, evaluation_function=Heuristic.heuristic_function_2_v2)


    # if isinstance(solution_node, Node):
    #     traverse = solution_node
    #     while traverse.get_parent() is not None:
    #         print(f"Action: {traverse.get_action()}")
    #         traverse = traverse.get_parent()
    # else:
    #     print (solution_node)


    traverse = solution_node
    while traverse.get_parent() is not None:
        print(f"Action: {traverse.get_action()}")
        traverse = traverse.get_parent()

    display(solution_node.get_state())