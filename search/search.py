from search.problem import Problem
from search.node import Node
from search.queue import FIFOQueue


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
    def breadth_first_search(problem : Problem) -> 'Node':
        node = Node(problem.get_initial(), None, None, 0)

        if problem.is_goal(node.get_state()):
            return node
        frontier = FIFOQueue()
        frontier.add(node)
        reached = set()
        reached.add(node.get_state().to_tuple())

        while not frontier.is_empty():
            print(f'Number of nodes in frontier: {frontier.size()}')
            node = frontier.pop()
            for child in Search.expand(problem, node):
                child_state = child.get_state()
                if problem.is_goal(child_state):
                    return child
                child_state_tuple = child_state.to_tuple()
                if child_state_tuple not in reached:
                    reached.add(child_state_tuple)
                    frontier.add(child)
        
        return None