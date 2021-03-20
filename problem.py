import sys
from collections import deque

## ------------------------------- ##
## -------- Problem Class -------- ##
## ------------------------------- ##
#A class to represent an abstract problem
class Problem:
    """
    While we get the general infrastructure of the problem in place, I'm going to work 
    with simplified versions of the actions that don't necessarily correspond to a real
    'action' a person can take. Instead the available actions will directly affect one 
    of the variables:
    1. Lowers resting blood pressure (trestbps)
    2. Lowers cholestorol level (chol)
    3. Lowers max heart rate achieved (thal)
    4. Lowers chest pain level (cp)
    For now, whenever an action is referred to in the code, it will be as an integer
    value that corresponds to one of the 4 actions listed above
    """

    def __init__(self, initialState, goal=None):
        self.initial = initialState
        self.goal = goal
        self.goalsMet = [False, False, False, False]#list of boolean values that declares if a variable has met the target value: [trestbps, chol, thal, cp]
    
    def goalTest(self):
        #Returns true if the state is a goal state
        if (self.goalsMet == [True, True, True, True]):
            return True
        else:
            return False

    def pathCost(self, c, s1, action, s2):
        #return the cost of a solution path
        #at the moment all actions cost the same (1), meaning that the resulting cost
        #for a solution will be equivalent to its depth in the search tree
        return c + 1

    def actions(self, state, action):
        #returns the list of all the possible actions
        #for now we'll just say that no action can be repeated consecutively
        #so each action will return a list containing only the other actions
        if (action == 1):
            return self.actionCheck([2,3,4])
        elif (action == 2):
            return self.actionCheck([1,3,4])
        elif (action == 3):
            return self.actionCheck([1,2,4])
        else:
            return self.actionCheck([1,2,3])

    def actionCheck(self, actionList):
        #checks each action in the list and will remove any actions
        #where the corrresponding goal has already been met
        availableActions = []
        for x in actionList:
            #if the corresponding goal hasn't been met, 
            #add it to the list of available actions
            if (self.goalsMet[x-1] == False):
                availableActions.append(x)
        print(availableActions)
        return availableActions

    def resultingState(self, state, action):
        #returns the state that results from executing the specified action in the specified state
        #At the moment the value that each variable is lowered by is entirely arbitrary
        if (action == 1):
            #lower blood pressure
            state.lowerBloodPressure()
            #check if the target value has been met
            if (state.trestbps <= self.goal.trestbps):
                self.goalsMet[0] = True
        elif (action == 2):
            #lower cholesterol level
            state.lowerCholestorol()
            #check if the target value has been met
            if (state.chol <= self.goal.chol):
                self.goalsMet[1] = True            
        elif (action == 3):
            #lower max heart rate
            state.lowerMaxHeartRate()
            #check if the target value has been met
            if (state.thalach <= self.goal.thalach):
                self.goalsMet[2] = True
        else:
            #lower chest pain level (only if it is > 0)
            state.lowerChestPainLevel()
            #check if the target value has been met
            if (state.cp <= self.goal.cp):
                self.goalsMet[3] = True
            
        return state
            
## ---------------------------- ##
## -------- Node Class -------- ##
## ---------------------------- ##
#A class to represent a node within a search tree
class Node:
    def __init__(self, state, parentNode=None, action=None, pathCost=0):
        self.state = state
        self.parentNode = parentNode
        self.action = action
        self.pathCost = pathCost
        #set the depth of the node to parent's +1
        if parentNode:
            #if the node has a parent
            self.depth = parentNode.depth + 1
        else:
            #if does not (root node)
            self.depth = 0

    def expand(self, problem):
        #returns the list of nodes that can be reached from this node in only 1 step
        return [self.childNode(problem, action) for action in problem.actions(self.state, self.action)]
    

    def childNode(self, problem, action):
        #generates a child node 
        nextState = problem.resultingState(self.state, action)
        nextNode = Node(nextState, self, action, problem.pathCost(self.pathCost, self.state, action, nextState))
        return nextNode

    def actionSequence(self, problem, action):
        #returns the action sequence from the root node to the current node
        return [node.action for node in self.path()[1:]]

    def path(self):
        #return the list of nodes that form a path from the root to the current node
        node, pathHome = self, []
        while node:
            pathHome.append(node)
            node = node.parentNode
        #at the moment the path goes from the current node to the root node
        #so it needs to be inverted:
        return list(reversed(pathHome))

    def printNode(self):
        print("State: ", self.state, "Parent: ", self.parentNode.state, "Action: ", self.action,)


## ----------------------------------- ##
## -------- Search Algorithms -------- ##
## ----------------------------------- ##

## --------- Breadth-First Search --------- ##
def BFS(problem):
    #Breadth-first Search algorithm, we should try a few different search algorithms
    #and compare the results from each of them. 
    #But for simplicity's sake, I'm just using one for now

    #double-ended queue to represent the frontier
    #initialise the frontier with the starting state of the problem
    frontier = deque([Node(problem.initial)])

    #while there are items in the frontier
    while frontier:
        #get the next item in the frontier
        node = frontier.popleft()

        #if the state in the current node matches a goal node:
        if problem.goalTest():
            print("Goal FOUND!")
            #return the current node
            return node
        #add the child nodes of the current node to the frontier
        frontier.extend(node.expand(problem))

    print("No goal found")
    return None


## --------- Depth-First Search --------- ##
def DFS(problem):
    #depth-first search algorithm

    #list to represent the frontier
    #initialise the frontier with the starting state of the problem
    frontier = list([Node(problem.initial)])

    #create an empty list to represent the explored set
    explored = []

    #while there are items in the frontier
    while frontier:
        #get the first item in the frontier
        node = frontier.pop(0)

        #check if the node is already in the explored set
        if node in explored:
            #if it is, skip to the next node in the frontier
            continue

        #if the state in the current node matches a goal node:
        if problem.goalTest():
            #return the current node
            return node
        #otherwise, add it to the explored set
        explored.append(node)
        #add the nodes child nodes to the frontier
        frontier.extend(node.expand(problem))

    print("No goal state found :(")
    return None


## --------- A* Search --------- ## 
def g(node):
    #returns the cost to reach a node
    return node.pathCost
    
#Heuristic Function
def h(node):
    cost = 0
    #check if the node is the root node
    #i.e it doesn't have an action

    if node.action is None:
        cost = 4
        return cost

    if (node.state % 2 == 0):
        cost += 1
    else:
        cost += 2
    
    if (node.action % 2 != 0):
        cost += 1
    return cost

def AStar(problem):
    #similar to GBFS, but incorporates the path cost of a given
    #node when sorting the values in the frontier.
    #in this case, g(node) is functionally the same as node.pathCost

    #list to represent the frontier
    #initialise the frontier with the starting state of the problem
    frontier = list([Node(problem.initial)])

    #create an empty list to represent the explored set
    explored = []

    #while there are items in the frontier
    while frontier:
        #get the first item in the frontier
        node = frontier.pop(0)

        #check if the node is already in the explored set
        if node in explored:
            #if it is, skip to the next node in the frontier
            continue

        #check if the current node is a goal state
        if problem.goalTest():
            #return the node if it is a goal node
            return node
        #otherwise, add it to the explored set
        explored.append(node)
        #expand the node, placing its child nodes into the frontier
        frontier.extend(node.expand(problem))
        #sort the frontier, lowest path cost first
        sorted(frontier, key=lambda Node: g(node) + h(node))