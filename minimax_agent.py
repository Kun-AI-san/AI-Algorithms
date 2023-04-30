# minimax_agent.py
# --------------
# COMP3620/6320 Artificial Intelligence
# The Australian National University
# For full attributions, see attributions.txt on Wattle at the end of the course

"""
    Enter your details below:

    Name: Karthik Reddy Vemireddy
    Student ID: u7348473
    Email: u7348473@anu.edu.au
"""

from typing import Tuple

from agents import Agent
from game_engine.actions import Directions
from search_problems import AdversarialSearchProblem

Position = Tuple[int, int]
Positions = Tuple[Position]
State = Tuple[int, Position, Position, Positions, float, float]


class MinimaxAgent(Agent):
    """ The agent you will implement to compete with the black bird to try and
        save as many yellow birds as possible. """

    def __init__(self, max_player, depth="2"):
        """ Make a new Adversarial agent with the optional depth argument.
        """
        self.max_player = max_player
        self.depth = int(depth)

    def evaluation(self, problem: AdversarialSearchProblem, state: State) -> float:
        """
            (MinimaxAgent, AdversarialSearchProblem,
                (int, (int, int), (int, int), ((int, int)), number, number))
                    -> number
        """
        player, red_pos, black_pos, yellow_birds, score, yb_score = state

        # *** YOUR CODE GOES HERE ***
        min_dist1=99999
        min_dist2=99999
        #finding out the closest bird distances from red bird and black bird
        for bird in yellow_birds:
            x=problem.maze_distance(red_pos,bird)
            y=problem.maze_distance(black_pos,bird)
            if x<min_dist1:
                min_dist1=x
            if y<min_dist2:
                min_dist2=y
        #we want distance between yellow bird to red to reduce hence a negative weight for creating an incentive to increase score
        #we want the red to avoid black to some degree, hence a positive weight
        #we want the number of birds to reduce to increase the score hence the negative weight
        #we want the distance between nearest yellow bird to increase from black, hence a positive weight
        f = score-2*min_dist1+0.5*problem.maze_distance(red_pos, black_pos)-6*len(yellow_birds)+2*min_dist2 
        return f

    def maximize(self, problem: AdversarialSearchProblem, state: State,
                 current_depth: int, alpha=float('-inf'), beta=float('inf')) -> Tuple[float, str]:
        """ This method should return a pair (max_utility, max_action).
            The alpha and beta parameters can be ignored if you are
            implementing minimax without alpha-beta pruning.
        """
        # *** YOUR CODE GOES HERE ***
        if current_depth==self.depth: return (self.evaluation(problem, state), Directions.STOP)
        if problem.terminal_test(state): return (self.evaluation(problem, state), Directions.STOP)
        v = float('-inf')
        action1 = Directions.STOP
        for successor,  action, cost in problem.get_successors(state):
            if successor[0]==state[0]: continue
            x=self.minimize(problem, successor, current_depth+1, alpha, beta)
            v = max(v, x)
            #if x is greater than v then x's action is updated as the new action
            if v==x:
                action1=action
            #do pruning for invalid limits
            if v>=beta:
                return (v,Directions.STOP)
            alpha = max(alpha, v)
        #no pruning occurs
        return (v, action1)
            

    def minimize(self, problem: AdversarialSearchProblem, state: State,
                 current_depth: int, alpha=float('-inf'), beta=float('inf')) -> float:
        """ This function should just return the minimum utility.
            The alpha and beta parameters can be ignored if you are
            implementing minimax without alpha-beta pruning.
        """
        # *** YOUR CODE GOES HERE ***
        if current_depth==self.depth: return self.evaluation(problem, state)
        if problem.terminal_test(state): return self.evaluation(problem, state)
        v = float('inf')
        for successor, action, cost in problem.get_successors(state):
            if successor[0]==state[0]: continue
            x, y = self.maximize(problem, successor, current_depth+1, alpha, beta)
            v = min(v, x)
            #do pruning for invalid limits
            if v<=alpha:
                return v
            beta = min(beta, v)
        #no pruning occurs
        return v

    def get_action(self, game_state):
        """ This method is called by the system to solicit an action from
            MinimaxAgent. It is passed in a State object.

            Like with all of the other search problems, we have abstracted
            away the details of the game state by producing a SearchProblem.
            You will use the states of this AdversarialSearchProblem to
            implement your minimax procedure. The details you need to know
            are explained at the top of this file.
        """
        # We tell the search problem what the current state is and which player
        # is the maximizing player (i.e. who's turn it is now).
        problem = AdversarialSearchProblem(game_state, self.max_player)
        state = problem.get_initial_state()
        utility, max_action = self.maximize(problem, state, 0)
        print("At Root: Utility:", utility, "Action:",
              max_action, "Expanded:", problem._expanded)
        return max_action
