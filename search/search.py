from search.problem import Problem
from search.node import Node
from util import Stack
from util import FIFOQueue
from enum import Enum
import heapq


frontier_size = 0


class Result(Enum):
    CUTOFF = 0
    FAILURE = 1


class Search:
    def __init__(self):
        pass


    @staticmethod
    def expand(problem: Problem, node: Node) -> list:
        state = node.get_state()
        nodes = []
        for action in problem.actions(state):
            new_state = problem.result(state, action)
            path_cost = node.get_path_cost() + problem.action_cost(state, action, new_state)
            new_node = Node(new_state, node, action, path_cost)
            nodes.append(new_node)
        return nodes
    

    @staticmethod
    def depth(node : 'Node'):
        return node.get_path_cost()


    @staticmethod
    def breadth_first_search(problem : Problem) -> 'Node':
        global frontier_size

        node = Node(problem.get_initial(), None, None, 0)

        if problem.is_goal(node.get_state()):
            return node
        frontier = FIFOQueue()
        frontier.push(node)
        reached = set()
        reached.add(node.get_state().to_tuple())

        while not frontier.is_empty():
            print(f'Number of nodes in frontier: {frontier.size()}')

            node = frontier.pop()
            for child in Search.expand(problem, node):
                child_raw_state = child.get_state().to_tuple()
                if problem.is_goal(child.get_state()):
                    frontier_size = frontier.size()
                    return child
                if child_raw_state not in reached:
                    reached.add(child_raw_state)
                    frontier.push(child)
        return None
    

    @staticmethod
    def depth_first_search(problem : Problem) -> 'Node':
        global frontier_size

        node = Node(problem.get_initial(), None, None, 0)

        if problem.is_goal(node.get_state()):
            return node
        frontier = Stack()
        frontier.push(node)
        reached = set()
        reached.add(node.get_state().to_tuple())

        while not frontier.is_empty():
            print(f'Number of nodes in frontier: {frontier.size()}')

            node = frontier.pop()
            for child in reversed(Search.expand(problem, node)):
                if problem.is_goal(child.get_state()):
                    frontier_size = frontier.size()
                    return child
                if child.get_state().to_tuple() not in reached:
                    reached.add(child.get_state().to_tuple())
                    frontier.push(child)
        return None
    

    @staticmethod
    def is_cycle(node : Node) -> 'bool':
        current_state = node.get_state().to_tuple()
        traverse = node.get_parent()
        while traverse is not None:
            if traverse.get_state().to_tuple() == current_state:
                return True
            traverse = traverse.get_parent()
        return False
    

    @staticmethod
    def depth_limit_search(problem: Problem, l : int):
        global frontier_size

        node = Node(problem.get_initial(), None, None, 0)
        frontier = Stack()
        frontier.push(node)
        result = Result.FAILURE

        while not frontier.is_empty():
            print(f'Number of nodes in frontier: {frontier.size()}')
            node = frontier.pop()
            if problem.is_goal(node.get_state()):
                frontier_size = frontier.size()
                return node
            if Search.depth(node) > l:
                # there can be solution at deeper depth
                # doesn't add any child node
                result = Result.CUTOFF
            elif not Search.is_cycle(node):
                for child in reversed(Search.expand(problem, node)):
                    frontier.push(child)
        return result
    

    @staticmethod
    def iterative_deepening_search(problem : Problem, limit : int):
        for depth in range(limit):
            print(f'At depth {depth}')
            result = Search.depth_limit_search(problem, depth)
            if result != Result.CUTOFF:
                return result
        # search to limit but can't be able to find, limit -> infinity
        return Result.FAILURE
    

    # late goal test for optimality?
    @staticmethod
    def best_first_search(problem : 'Problem', evaluation_function : 'function'):
        global frontier_size

        node = Node(problem.get_initial(), None, None, 0)
        frontier = []
        heapq.heappush(frontier, (evaluation_function(node), node))
        reached = {}
        reached[node.get_state().to_tuple()] = node

        while not (len(frontier) == 0):
            print(f'Number of nodes in frontier: {len(frontier)}')
            _, node = heapq.heappop(frontier)
            if problem.is_goal(node.get_state()):
                frontier_size = len(frontier)
                return node
            
            for child in Search.expand(problem, node):
                child_state = child.get_state().to_tuple()
                if child_state not in reached:
                    reached[child_state] = child
                    heapq.heappush(frontier, (evaluation_function(child), child))
                else:
                    if child.get_path_cost() < reached[child_state].get_path_cost():
                        reached[child_state] = child
                        heapq.heappush(frontier, (evaluation_function(child), child))
                    else:
                        continue
        return None