# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #Initialization
    openList=util.Stack() # contains (position,listActions)
    start=problem.getStartState()
    closedList=[start]  #Open and closed list contains visited emplacement

    #Develop the first node
    listSuccesors=problem.getSuccessors(start)
    for succesor in listSuccesors:
        openList.push((succesor[0],[succesor[1]])) 

    evaluatedState=start
    while(not problem.isGoalState(evaluatedState)):
        #Do the research while we haven't found the goal

        # Check if the node isn't in the closed list to prevent infinite loops
        alreadyVisited=False
        for element in closedList :
            if(evaluatedState==element):
                alreadyVisited=True
        if(not alreadyVisited):
            #Develop the node :
            listSuccesors=problem.getSuccessors(evaluatedState)
            for succesor in listSuccesors:
                position=succesor[0]
                action=succesor[1]
                openList.push((position,listAction+[action]))
            closedList.append(evaluatedState)
        
        if openList.isEmpty():
            print("No goal found")
            return []
        else :
            # Visit the next node in the open list
            temporaryTuple=openList.pop()
            evaluatedState=temporaryTuple[0]
            listAction=temporaryTuple[1]

    return listAction

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    #To compare with depthFirstSearch, we replaced the Stack by a Queue for the open list 
    #Initialization
    openList=util.Queue() # contains (position,listActions)
    start=problem.getStartState()
    closedList=[start]  # contains visited emplacement

    #Develop the first node
    listSuccesors=problem.getSuccessors(start)
    for succesor in listSuccesors:
        openList.push((succesor[0],[succesor[1]])) 

    evaluatedState=start
    while(not problem.isGoalState(evaluatedState)):
        #Do the research while we haven't found the goal

        # Check if the node isn't in the closed list to prevent infinite loops
        alreadyVisited=False
        for element in closedList :
            if(evaluatedState==element):
                alreadyVisited=True
        if(not alreadyVisited):
            #Develop the node :
            listSuccesors=problem.getSuccessors(evaluatedState)
            for succesor in listSuccesors:
                position=succesor[0]
                action=succesor[1]
                openList.push((position,listAction+[action]))
            closedList.append(evaluatedState)
        
        if openList.isEmpty():
            print("No goal found")
            return []
        else :
            # Visit the next node in the open list
            temporaryTuple=openList.pop()
            evaluatedState=temporaryTuple[0]
            listAction=temporaryTuple[1]

    return listAction

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    #Initialization
    openList=util.PriorityQueue() # contains (position,listActions,cumulatedCost)
    start=problem.getStartState()
    closedList=[start]  # contains visited emplacement

    #Develop the first node
    listSuccesors=problem.getSuccessors(start)
    for succesor in listSuccesors:
        cumulatedCost=succesor[2]
        openList.push((succesor[0],[succesor[1]],cumulatedCost),cumulatedCost)

    evaluatedState=start
    while(not problem.isGoalState(evaluatedState)):
        #Do the research while we haven't found the goal

        # Check if the node isn't in the closed list to prevent infinite loops
        alreadyVisited=False
        for element in closedList :
            if(evaluatedState==element):
                alreadyVisited=True
        if(not alreadyVisited):
            #Develop the node :
            listSuccesors=problem.getSuccessors(evaluatedState)
            for succesor in listSuccesors:
                position=succesor[0]
                action=succesor[1]
                cost=succesor[2]
                openList.update((position,listAction + [action],cost+cumulatedCost),cost+cumulatedCost)
            closedList.append(evaluatedState)
        
        if openList.isEmpty():
            print("No goal found")
            return []
        else :
            # Visit the next node in the open list
            temporaryTuple=openList.pop()
            evaluatedState=temporaryTuple[0]
            listAction=temporaryTuple[1]
            cumulatedCost=temporaryTuple[2]
                
    return listAction

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

    #Initialization
    openList=util.PriorityQueue() # contains (position,listActions,cumulatedCost)
    start=problem.getStartState()
    closedList=[start]  # contains visited emplacement

    #Develop the first node
    listSuccesors=problem.getSuccessors(start)
    for succesor in listSuccesors:
        cumulatedCost=succesor[2]
        fn=cumulatedCost+heuristic(succesor[0],problem)
        openList.push((succesor[0],[succesor[1]],cumulatedCost),fn)

    evaluatedState=start
    while(not problem.isGoalState(evaluatedState)):
        #Do the research while we haven't found the goal

        # Check if the node isn't in the closed list to prevent infinite loops
        alreadyVisited=False
        for element in closedList :
            if(evaluatedState==element):
                alreadyVisited=True
        if(not alreadyVisited):
            #Develop the node :
            listSuccesors=problem.getSuccessors(evaluatedState)
            for succesor in listSuccesors:
                position=succesor[0]
                action=succesor[1]
                cost=succesor[2]
                fn=cost+cumulatedCost+heuristic(position,problem)
                openList.update((position,listAction + [action],cost+cumulatedCost),fn)
            closedList.append(evaluatedState)
        
        if openList.isEmpty():
            print("No goal found")
            return []
        else :
            # Visit the next node in the open list
            temporaryTuple=openList.pop()
            evaluatedState=temporaryTuple[0]
            listAction=temporaryTuple[1]
            cumulatedCost=temporaryTuple[2]  
    return listAction

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
