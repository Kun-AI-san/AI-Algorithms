"""
    Enter your details below:

    Name: Karthik Reddy Vemireddy
    Student ID: u7348473
    Email: u7348473@anu.edu.au
"""

from typing import List

from game_engine.util import raise_not_defined
from search_problems import SearchProblem
from frontiers import Stack
from search_strategies import SearchNode

def solve(problem: SearchProblem) -> List[str]:
    """See 2_implementation_notes.md for more details.

    Your search algorithms needs to return a list of actions that reaches the
    goal from the start state in the given problem. The elements of this list
    need to be one or more references to the attributes NORTH, SOUTH, EAST and
    WEST of the class Directions.
    """
    
    # Remove this line when you have implemented Iterative Deepening Depth First Search
    #raise_not_defined()
    # *** YOUR CODE HERE ***
    ls = []
    path = {}
    current_state = problem.get_initial_state()
    node = SearchNode(current_state, None, None, None)
    i = 0
    while(True):#loop until goal state with increasing depth limit
        s = Stack()
        visited = []
        visited.append(current_state)
        result, cutoff, fail=IDS_search(node, problem, i, visited, s)
        print(visited)
        if cutoff != True and fail!=True:
            break
        elif fail == True:
            return []
        i+=1
    while result.parent:
        ls.append(result.action)
        result=result.parent
    ls.reverse()
    return ls


def IDS_search(node, problem, i, visited, s):
    if problem.goal_test(node.state):#goal state check
        return (node, False, False)
    elif i == node.depth:#cutoff
        return (None, True, False)
    else:
        cutoff_occured = False
        for state, direc, cost in problem.get_successors(node.state):
            new_node = SearchNode(state, direc, cost, node, node.depth+1)
            if new_node.state not in visited:#check if new node is present in the explored list
                visited.append(new_node.state)
                result, cutoff, fail = IDS_search(new_node, problem, i, visited, s)#recursive way to check for goal
                if cutoff == True:
                    cutoff_occured = True
                elif fail!=True:
                    return (result, False, False)
                visited.remove(new_node.state)
    return (None, True, False) if cutoff_occured else (None, False, True)
            
