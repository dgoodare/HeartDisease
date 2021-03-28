import sys
from collections import deque

from actions import LowIntensityAction, MediumIntensityAction, HighIntensityAction, Diet
from filterActions import filterPressure, filterCholesterol#functions that filter out useless actions

## ------------------------------- ##
## -------- Problem Class -------- ##
## ------------------------------- ##
#A class to represent an abstract problem
class Problem:
    """
    There are 9 possible actions a patient can take with 3 levels of intesity; low intesity exercises are recommended to people at medium-high risk;
    medium intensity exercises are recommended to people low-medium risk; and high intensity exercises are recommended to people at high risk.
    Diets are recommended to all patients
    When an action is referenced in the code, it will be an integer that corresponds to one of the following actions:
    = Low Intensity =
    0. Brisk Walking
    1. Yoga
    2. Pilates

    = Medium Intensity =
    3. Swimming
    4. Jogging

    = High Intensity = 
    5. Boxing
    6. High-Intensity Interval Training (HIIT)

    = Diets =
    7. DASH diet
    8. Meditarranean diet
    """

    def __init__(self, initialState): #, goal=None):
        self.initial = initialState
        self.goalsMet = [False, False, False]#list of boolean values that declares if a variable has met the target value: [trestbps, chol, fbs]
        #objects to store the different tiers/kinds of actions
        self.lowIntensity = LowIntensityAction()
        self.mediumIntensity = MediumIntensityAction()
        self.highIntensity = HighIntensityAction()
        self.diets = Diet()
    
    def goalTest(self, node):
        #Returns true if the state is a goal state
        #Check each variable to see if it is in the target range

        #Blood Pressure
        if ((node.state.trestbps >= 90) and (node.state.trestbps < 120)):
                self.goalsMet[0] = True

        #Cholestrerol
        if (node.state.chol < 200):
                self.goalsMet[1] = True

        #Blood sugar
        if (node.state.fbs == 0):
            self.goalsMet[2] = True

        if (self.goalsMet == [True, True, True]):
            return True
        else:
            return False

    def pathCost(self, totalCost, action):
        #return the cost of a solution path
        currentCost = 0
        if (action == 0):#Brisk Walking
            currentCost = 2
        elif (action == 1):#Yoga
            currentCost = 1           
        elif (action == 2):#Pilates
            currentCost = 1
        elif (action == 3):#Swimming
            currentCost = 3
        elif (action == 4):#Jogging
            currentCost = 3
        elif (action == 5):#Boxing
            currentCost = 4
        elif (action == 6):#HIIT
            currentCost = 4
        elif (action == 7):#DASH diet
            currentCost = 3
        elif (action == 8):#Meditarranean diet
            currentCost = 3
        return totalCost + currentCost

    def actions(self, node, action):
        #returns the list of all the possible actions
        #Checks each variable and determines which actions are best for the patient
        # it will then check to see which targets have already been met and remove
        # any unecessary actions from the list

        #dictates if an action is doable in the current state [swimming, jogging, brisk walking, DASH, meditarranean]
        #isDoable = [True, True, True, True, True]

        #age check
        ageLevel = node.state.ageCheck()
        #Blood Pressure Check
        pLevel = node.state.bloodPressureCheck()
        #Cholesterol Check
        cLevel = node.state.cholesterolCheck()
        #blood sugar check
        sLevel = node.state.sugarCheck()
        #give an overall risk level
        riskLevel = ageLevel + pLevel + cLevel + sLevel

        actionList = []

        if (riskLevel <= 2):
            #patient is at low risk, recommend medium - high intensity exercises
            actionList.append(self.mediumIntensity.actions[0])
            actionList.append(self.mediumIntensity.actions[1])

            actionList.append(self.highIntensity.actions[0])
            actionList.append(self.highIntensity.actions[1])
        elif ((riskLevel >= 3) and (riskLevel <= 5)):
            #patient is at medium risk, recommend low - medium intensity exercises
            actionList.append(self.lowIntensity.actions[0])
            actionList.append(self.lowIntensity.actions[1])
            actionList.append(self.lowIntensity.actions[2])

            actionList.append(self.mediumIntensity.actions[0])
            actionList.append(self.mediumIntensity.actions[1])
        elif ((riskLevel >= 6)):
            #patient is at high risk, recommend low intensity exercises
            actionList.append(self.lowIntensity.actions[0])
            actionList.append(self.lowIntensity.actions[1])
            actionList.append(self.lowIntensity.actions[2])

        #include diets, as well
        actionList.append(self.diets.actions[0])
        actionList.append(self.diets.actions[1])

        return actionList

    def resultingState(self, node, action, depth):
        #returns the state that results from executing the specified action in the specified state
        #At the moment the value that each variable is lowered by is entirely arbitrary
        if (action == 0):#Brisk Walking
            newState = self.lowIntensity.briskWalking(node.state)
        elif (action == 1):#Yoga
            newState = self.lowIntensity.yoga(node.state)               
        elif (action == 2):#Pilates
            newState = self.lowIntensity.pilates(node.state)
        elif (action == 3):#Swimming
            newState = self.mediumIntensity.swimming(node.state)
        elif (action == 4):#Jogging
            newState = self.mediumIntensity.jogging(node.state)
        elif (action == 5):#Boxing
            newState = self.highIntensity.boxing(node.state)
        elif (action == 6):#HIIT
            newState = self.highIntensity.hiit(node.state)
        elif (action == 7):#DASH diet
            newState = self.diets.DASHdiet(node.state)
        elif (action == 8):#Meditarranean diet
            newState = self.diets.meditarraneanDiet(node.state)

        # Since there isn't an exact value for blood sugar in the dataset, 
        # we're just estimating that after a year (equivalent to 4 3-month long actions)
        # the patient's blood sugar will have dropped below the threshold of 120 mg/dL
        if (depth >= 4):
            newState.fbs = 0
        
        # We must also consider the undenible fact of life that people age.
        # Since actions are all 3 months long, age will increase at every
        # 4th node deep in the tree
        if ((depth != 0) and (depth % 4 == 0)):
            newState.age += 1

        #newState.printPatient()
        return newState
            
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
        return [self.childNode(problem, action) for action in problem.actions(self, self.action)]
    

    def childNode(self, problem, action):
        #generates a child node 
        nextState = problem.resultingState(self, action, self.depth)
        nextNode = Node(nextState, self, action, problem.pathCost(self.pathCost, action))
        return nextNode

    def actionSequence(self):
        #returns the action sequence from the root node to the current node
        #return [self.action for node in self.path()[1:]]
        sequence = []
        path = self.path()[1:]

        for action in path:
            sequence.append(action)
        return sequence
        

    def path(self):
        #return the list of nodes that form a path from the root to the current node
        node = self
        pathHome = []
        while node:
            pathHome.append(node.action)
            node = node.parentNode
        #path goes from the current node to the root node
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
        if problem.goalTest(node):
            print("Goal FOUND!")
            #return the current node
            return node
        
        #if (node.depth > 8):
         #   print("No goal found")
         #   return node
        #add the child nodes of the current node to the frontier
        frontier.extend(node.expand(problem))

    print("No goal found")
    return node

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
        if problem.goalTest(node):
            #return the current node
            return node
        #otherwise, add it to the explored set
        explored.append(node)
        #add the nodes child nodes to the frontier
        frontier.extend(node.expand(problem))

    print("No goal state found")
    return None

## --------- Uniform-Cost Search --------- ##
def UCS(problem):
    #Uniform-Cost Search algorithm

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
        if problem.goalTest(node):
            #return the node if it is a goal node
            print("Goal FOUND!")
            return node
        #otherwise, add it to the explored set
        explored.append(node)
        #expand the node, placing its child nodes into the frontier
        frontier.extend(node.expand(problem))
        #sort the frontier, lowest path cost first
        sorted(frontier, key=lambda Node: node.pathCost)

    print("No goal found")
    return None

## --------- A* Search --------- ##    
#Heuristic Function
def h(node):
    cost = 0
    #check if the node is the root node
    #i.e it doesn't have an action
    if node.action is None:
        return cost

    #find the difference between the current and target values
    bpDifference = node.state.trestbps - 120
    cholDifference = node.state.chol - 200

    cost = bpDifference + cholDifference
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
        if problem.goalTest(node):
            #return the node if it is a goal node
            print("Goal FOUND!")
            return node

        #otherwise, add it to the explored set
        explored.append(node)
        #expand the node, placing its child nodes into the frontier
        frontier.extend(node.expand(problem))
        #sort the frontier, lowest path cost first
        sorted(frontier, key=lambda Node: node.pathCost + h(node))
