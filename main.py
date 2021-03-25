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
        newPatient = Patient(row[3], row[4], row[5])
        #print data on a patient
        #newPatient.printPatient()
        #append the newly created patient to the end of the list
        patientList.append(newPatient)

    return patientList

def breadthFirstSearch(problem):
    #Find solution using breadth-first search
    solutionNode = BFS(problem)
    solutionNode.state.printPatient()

    print(problem.goalsMet)

    print("Path to recovery:")
    path = solutionNode.actionSequence()
    print(path)

def depthFirstSearch(problem):
    #Find solution using breadth-first search
    solutionNode = DFS(problem)
    solutionNode.state.printPatient()

    print(problem.goalsMet)

    print("Path to recovery:")
    path = solutionNode.actionSequence()
    print(path)


def uniformCostSearch(problem):
    #Find a solution using uniform-cost search
    solutionNode = UCS(problem)
    solutionNode.state.printPatient()

    print(problem.goalsMet)

    print("Path to recovery:")
    path = solutionNode.actionSequence()
    print(path)

def aStarSearch(problem):
    #Find a solution using uniform-cost search
    solutionNode = UCS(problem)
    solutionNode.state.printPatient()

    print(problem.goalsMet)

    print("Path to recovery:")
    path = solutionNode.actionSequence()
    print(path)

#create the list of Patients
patientList = initialisePatientList(openCSV())
#get the first patient from the list
#p = patientList[0]
r = random.randint(0, len(patientList))
p = patientList[r]

print("Patient number: ", r)
#define the starting state as a list of the relevant values (only using 4 of them right now: trestbps, chol, thalach & cp)
initialState = p
print("Initial State: ")
p.printPatient()

#initialise problem
problem = Problem(initialState)

#uncomment whichever algorithm you want to use:
#breadthFirstSearch(problem)
#depthFirstSearch(problem)
#uniformCostSearch(problem)
#aStarSearch(problem)


