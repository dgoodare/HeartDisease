#standard libraries
import csv
import random

#local imports
from patient import Patient#Patient class
from problem import Problem#Problem class
from problem import BFS#Breadth-first search algorithm
from problem import DFS#depth-first search algorithm
from problem import UCS#Uniform-cost search algorithm
from problem import AStar#A* search algorithm

#generate a random number to pick a patient
r = 96#random.randint(0, 302)

def initialiseProblem():
    #create the list of Patients
    patientList = initialisePatientList(openCSV())
    #get the first patient from the list
    #p = patientList[0]
    
    p = patientList[r]
    
    print("Patient number: ", r)
    #define the starting state as a list of the relevant values (only using 4 of them right now: trestbps, chol, thalach & cp)
    initialState = p
    print("Initial State: ")
    p.printPatient()
    print("")
    #initialise problem
    return Problem(initialState)

def openCSV():
    #create list of patients' data
    patientData = []

    #open csv file and copy contents into patientData
    with open('heart.csv') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            patientData.append(row)

    return patientData

#initialises a list of patients
def initialisePatientList(data):
    #need to delete the first row in the file, since it contains the labels for the fields
    del data[0]
    #create a list to store the patients
    patientList = []
    for row in data:     
        #create a new patient storing the information in the current row
        #currently stores every variable in the database
        newPatient = Patient(row[0], row[3], row[4], row[5])
        #print data on a patient
        #newPatient.printPatient()
        #append the newly created patient to the end of the list
        patientList.append(newPatient)

    return patientList

def breadthFirstSearch():
    #Find solution using breadth-first search
    print('==========================================================================================================================================')
    print("Searching with breadth-first search...")
    print("")
    problem = initialiseProblem()
    breadthSln = BFS(problem)
    breadthSln.state.printPatient()

    #print(problem.goalsMet)

    generatePlan(breadthSln.actionSequence())
    print('==========================================================================================================================================')

def depthFirstSearch():
    #Find solution using breadth-first search
    print('==========================================================================================================================================')
    print("Searching with depth-first search...")
    print("")
    problem = initialiseProblem()
    depthSln = DFS(problem)
    depthSln.state.printPatient()

    #print(problem.goalsMet)

    generatePlan(depthSln.actionSequence())
    print('==========================================================================================================================================')

def uniformCostSearch():
    #Find a solution using uniform-cost search
    print('==========================================================================================================================================')
    print("Searching with uniform-cost search...")
    print("")

    problem = initialiseProblem()
    uniformSln = UCS(problem)
    uniformSln.state.printPatient()

    #print(problem.goalsMet)


    generatePlan(uniformSln.actionSequence())
    print('==========================================================================================================================================')

def aStarSearch():
    #Find a solution using uniform-cost search
    print('==========================================================================================================================================')
    print("Searching with A* search...")
    print("")

    problem = initialiseProblem()
    aStarSln = AStar(problem)
    aStarSln.state.printPatient()

    #print(problem.goalsMet)

    generatePlan(aStarSln.actionSequence())
    print('==========================================================================================================================================')    

def generatePlan(path):
    w = y = p = s = j = b = h = d = m = 0
    for action in path:
        if (action == 0):
            w += 3
        elif (action == 1):
            y += 3
        elif (action == 2):
            p += 3
        elif (action == 3):
            s += 3
        elif (action == 4):
            j += 3
        elif (action == 5):
            b += 3
        elif (action == 6):
            h += 3
        elif (action == 7):
            d += 3
        elif (action == 8):
            m += 3
    
    print("You should try: ")
    if (s > 0):
        print("- Swimming regularly for", s, "months")
    if (j > 0):
        print("- Jogging regularly for", j, "months")
    if (w > 0):
        print("- Going for a brisk walk regularly for", w, "months")
    if (d > 0):
        print("- The DASH diet for", d, "months")
    if (m > 0):
        print("- The meditarranean diet for", m, "months")

breadthFirstSearch()
depthFirstSearch()
uniformCostSearch()
aStarSearch()




