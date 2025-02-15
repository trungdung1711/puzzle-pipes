from data1 import data1
from data2 import data2
from data3 import data3
from data4 import data4
from data5 import data5
from data6 import data6
from data7 import data7
from data8 import data8
from data9 import data9

from search.problem import *
from search.node import *
from search.search import *

grid1 = data1() # no check
grid2 = data2() # OK
grid3 = data3() # OK
grid4 = data4() # OK
grid5 = data5() # OK
grid6 = data6() # no check
grid7 = data7() # no check
grid8 = data8() # OK
grid9 = data9() # OK


if __name__ == '__main__':
    pipe_puzzle_problem = PipePuzzleProblem(grid9)
    solution_node = Search.breadth_first_search(pipe_puzzle_problem)

    state = solution_node.get_state()

    traverse = solution_node
    while traverse.get_parent() is not None:
        print(f"Action: {traverse.get_action()}")
        traverse = traverse.get_parent()