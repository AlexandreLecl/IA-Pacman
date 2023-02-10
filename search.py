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
    openList=util.Stack()
    start=problem.getStartState()
    evaluatedState=(start,'Stop',0)
    closedList=[(evaluatedState,None)]  #Open and closed list contains tuples of form (Node,Ancestor)

    while(not problem.isGoalState(evaluatedState[0])):
        #Do the research while we haven't found the goal
        
        #Develop the node :
        listSuccesors=problem.getSuccessors(evaluatedState[0])
        for succesor in listSuccesors:
            # Check if the node isn't in the closed list to prevent infinite loops
            alreadyVisited=False
            for element in closedList :
                if(succesor[0]==element[0][0]):
                    alreadyVisited=True
            if(not alreadyVisited):
                openList.push((succesor,evaluatedState))
                
        if openList.isEmpty():
            print("No goal found")
            return []
        else :
            # Visit the next node in the open list
            temporaryTuple=openList.pop()
            closedList.append(temporaryTuple)
            evaluatedState=temporaryTuple[0]

    # Create list of actions
    listAction=[]
    while(evaluatedState[0]!=start):
        for element in closedList:
            if(element[0][0]==evaluatedState[0]):
                ancestor=element[1]
                listAction.insert(0,evaluatedState[1])
                evaluatedState=ancestor
    return listAction

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    #To compare with depthFirstSearch, we replaced the Stack by a Queue for the open list 
    #Initialization
    openList=util.Queue()
    start=problem.getStartState()
    evaluatedState=(start,'Stop',0)
    closedList=[(evaluatedState,None)]  #Open and closed list contains tuples of form (Node,Ancestor)

    while(not problem.isGoalState(evaluatedState[0])):
        #Do the research while we haven't found the goal
        
        #Develop the node :
        listSuccesors=problem.getSuccessors(evaluatedState[0])
        for succesor in listSuccesors:
            # Check if the node isn't in the closed list to prevent infinite loops
            alreadyVisited=False
            for element in closedList :
                if(succesor[0]==element[0][0]):
                    alreadyVisited=True
            if(not alreadyVisited):
                openList.push((succesor,evaluatedState))
                
        if openList.isEmpty():
            print("No goal found")
            return []
        else :
            # Visit the next node in the open list
            temporaryTuple=openList.pop()
            closedList.append(temporaryTuple)
            evaluatedState=temporaryTuple[0]

    # Create list of actions
    listAction=[]
    while(evaluatedState[0]!=start):
        for element in closedList:
            if(element[0][0]==evaluatedState[0]):
                ancestor=element[1]
                listAction.insert(0,evaluatedState[1])
                evaluatedState=ancestor
    return listAction

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    
    #Initialization
    openList=util.PriorityQueue()
    start=problem.getStartState()
    evaluatedState=(start,'Stop',0)
    closedList=[(evaluatedState,None,0)]  #Open and closed list contains tuples of form (Node,Ancestor,Cost)
    toDevelop=True
    while(not problem.isGoalState(evaluatedState[0])):
        #Do the research while we haven't found the goal
        
        
        if(toDevelop):
            #Develop the node :
            listSuccesors=problem.getSuccessors(evaluatedState[0])
            for succesor in listSuccesors:
                # Find the cost to this Node
                actions=[]  #List of actions from the start to this node
                thisNode= succesor
                while(thisNode[0]!=start):
                    for element in closedList:
                        if(element[0][0]==thisNode[0]):
                            ancestor=element[1]
                            actions.insert(0,thisNode[1])
                            thisNode=ancestor
                cost=start.getCostOfActions(actions)
                print("cost calculated\n")

                openList.push((succesor,evaluatedState,cost))
                
        if openList.isEmpty():
            print("No goal found")
            return []
        else :
            toDevelop=True
            # Visit the next node in the open list
            temporaryTuple=openList.pop()
            bestway=True
            for element in closedList:
                if(temporaryTuple[0]==element[0]):
                    #There is the same node visited
                    if(temporaryTuple[2]>=element[2]):
                        #with a lower cost
                        bestway=False
                    else:
                        #with a higher cost
                        element[2]=temporaryTuple[2] # cost
                        element[1]=temporaryTuple[1] # ancestor


            if(bestway):         
                closedList.append(temporaryTuple)
                evaluatedState=temporaryTuple[0] # risque inf loop
            else:
                toDevelop=False
           

    # Create list of actions
    listAction=[]
    while(evaluatedState[0]!=start):
        for element in closedList:
            if(element[0][0]==evaluatedState[0]):
                ancestor=element[1]
                listAction.insert(0,evaluatedState[1])
                evaluatedState=ancestor
    return listAction

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
