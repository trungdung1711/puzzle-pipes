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

from search.problem import *
from search.node import *
from search.search import *
from game.game import display
from search.heuristic import Heuristic

                    #      Uninformed                      Informed    
                    # BFS           DLS             GBFS_v1         GBFS_v2
grid1 = data1()     # no check                      OK                  OK
grid2 = data2()     # OK                            OK                  OK
grid3 = data3()     # OK            OK              OK                  OK
grid4 = data4()     # OK                            OK                  OK
grid5 = data5()     # OK            OK              OK                  OK
grid6 = data6()     # no check                                          OK
grid7 = data7()     # no check                                          OK
grid8 = data8()     # OK            OK              OK                  OK
grid9 = data9()     # OK                            OK                  OK
grid10 = data10()   #               OK              OK                  OK
grid11 = data11()   #                                                   
grid12 = data12()   #                               OK                  OK
grid13 = data13()   #                               OK                  OK [ better solution ]
# real pipe from https://www.puzzle-pipes.com/
grid14 = data14()   #                               OK                  OK [ faster ]
grid15 = data15()   #                               OK [ long time]     OK [ faster and better solution]
grid16 = data16()   #                               OK                  OK [ faster ]


if __name__ == '__main__':

    pipe_puzzle_problem = PipePuzzleProblem(grid16)

    # solution_node = Search.breadth_first_search(pipe_puzzle_problem)
    # solution_node = Search.depth_first_search(pipe_puzzle_problem)
    # solution_node = Search.iterative_deepening_search(pipe_puzzle_problem, limit=30)
    # solution_node = Search.depth_limit_search(pipe_puzzle_problem, l = 7)
    solution_node = Search.greedy_best_first_search(pipe_puzzle_problem, Heuristic.heuristic_function_v0)
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