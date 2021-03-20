#standard libraries
import csv

#local imports
from patient import Patient#Patient class
from problem import Problem#Problem class
from problem import BFS#Breadth-first search algorithm

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
        newPatient = Patient(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13])
        #print data on a patient
        #newPatient.printPatient()
        #append the newly created patient to the end of the list
        patientList.append(newPatient)

    return patientList

#create the list of Patients
patientList = initialisePatientList(openCSV())
#get the first patient from the list
p = patientList[0]

#define the starting state as a list of the relevant values (only using 4 of them right now: trestbps, chol, thalach & cp)
initialState = p
print("Initial State: ")
p.printPatient()

#define the goal state as a list of target values for each variable
#we could expand this definition by saying that only a certain number of contraints need to be satisfied?
#these values are just arbitrary values for now and as such, don't hold any medical relevance
#goalState = [trestbps=120, chol=200, thal=135, cp=0]
goalState = Patient(0, 0, 0, 120, 200, 0, 0, 0, 0, 0, 0, 0, 135, 0)
print("Goal State:")
goalState.printPatient()

#initialise problem
problem = Problem(initialState, goalState)

#Find solution using breadth-first search
solutionNode = BFS(problem)
solutionNode.state.printPatient()