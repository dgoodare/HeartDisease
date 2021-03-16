import sys
from collections import deque

## ----------------------- ##
## ---- Problem Class ---- ##
## ----------------------- ##
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
    
    def goalTest(self, testState):
        #Returns true if the state is a goal state
        if ((testState[0] <= self.goal[0]) and (testState[1] <= self.goal[1]) and (testState[2] <= self.goal[2]) and (testState[3] <= self.goal[3])):
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
            return [2,3,4]
        elif (action == 2):
            return [1,3,4]
        elif (action == 3):
            return [1,2,4]
        else:
            return[1,2,3]

    def resultingState(self, state, action):
        #returns the state that results from executing the specified action in the specified state
        #At the moment the value that each variable is lowered by is entirely arbitrary
        if (action == 1):
            #lower blood pressure
            print("lowering bp")
            state[0] -= 2
        elif (action == 2):
            #lower cholesterol level
            print("lowering chol")
            state[1] -= 10
        elif (action == 3):
            #lower max heart rate
            print("lowering thalach")
            state[2] -= 5
        else:
            #lower chest pain level (only if it is > 0)
            if (state[3] > 0):
                print("lowering cp")
                state[3] -= 1

        return state
            
## -------------------- ##
## ---- Node Class ---- ##
## -------------------- ##
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
        if problem.goalTest(node.state):
            print("Goal FOUND!")
            #return the current node
            return node
        #add the child nodes of the current node to the frontier
        frontier.extend(node.expand(problem))

    print("No goal found")
    return None