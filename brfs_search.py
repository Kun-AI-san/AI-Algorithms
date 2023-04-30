"""
    Enter your details below:

    Name: Karthik Reddy Vemireddy
    Student ID: u7348473
    Email: u7348473@anu.edu.au
"""

from typing import List
from frontiers import Queue
q = Queue()  # We can now use Queue

from game_engine.util import raise_not_defined
from search_problems import SearchProblem, PositionSearchProblem


def solve(problem: SearchProblem) -> List[str]:
    """See 2_implementation_notes.md for more details.

    Your search algorithms needs to return a list of actions that reaches the
    goal from the start state in the given problem. The elements of this list
    need to be one or more references to the attributes NORTH, SOUTH, EAST and
    WEST of the class Directions.
    """
    #raise_not_defined()  # Remove this line when you have implemented BrFS
    # *** YOUR CODE HERE ***
    ls = []
    ls1 = set()
    prev = {}
    current_state = problem.get_initial_state()
    q.push(current_state)
    ls1.add(current_state)
    while not problem.goal_test(current_state): # check for goal state
        for i,j,k in problem.get_successors(current_state):
            if i not in q.contents and i not in ls1:# check if state exists in queue or explored list
                q.push(i)
                prev[str(i)]=(current_state,j)
                ls1.add(i)
            else:
                continue
        v = q.pop()#pop off the queue
        current_state = q.peek()
    x = current_state
    while str(x) in prev:
        ls.append(prev[str(x)][1])
        x = prev[str(x)][0]
    ls.reverse()       
    return ls
