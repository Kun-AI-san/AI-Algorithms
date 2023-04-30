"""
    Enter your details below:

    Name: Karthik Reddy Vemireddy
    Student ID: u7348473
    Email: u7348473@anu.edu.au
"""

from typing import Callable, List

from game_engine.util import raise_not_defined
from search_problems import SearchProblem
from frontiers import PriorityQueue
from search_strategies import SearchNode


def solve(problem: SearchProblem, heuristic: Callable) -> List[str]:
    """See 2_implementation_notes.md for more details.

    Your search algorithms needs to return a list of actions that reaches the
    goal from the start state in the given problem. The elements of this list
    need to be one or more references to the attributes NORTH, SOUTH, EAST and
    WEST of the class Directions.
    """

    #raise_not_defined()  # Remove this line when your solution is implemented
    # *** YOUR CODE HERE ***
    current_state = problem.get_initial_state()
    q = PriorityQueue()
    start_node = SearchNode(current_state, None, 0, None, 0)
    q.push(start_node, heuristic(current_state, problem))
    ls = []
    visited = set()
    result = None
    while not q.is_empty():#check if queue is empty
        node = q.pop()
        if node.state not in visited:#check if current state is present in visited set
            if problem.goal_test(node.state):#goal state check
                result = node
                break
            visited.add(node.state)#add node into the visited list
            for state, direc, cost in problem.get_successors(node.state):
                new_node = SearchNode(state, direc, node.path_cost+1, node, node.depth+1)
                q.push(new_node, new_node.path_cost+heuristic(new_node.state, problem))#pushing new node into priority queue
            
    while result.parent:
        ls.append(result.action)
        result=result.parent
    ls.reverse()
    return ls      