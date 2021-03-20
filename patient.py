
## ------------------------------- ##
## -------- Patient Class -------- ##
## ------------------------------- ##
# a class to represent a single patient, this class will also be used to represent a 'state'
# for a search problem
class Patient:
    #constructor
    def __init__(self, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, target):
        self.age = int(age)#age of the patient
        self.sex = int(sex)#sex of the patient (1 = male; 0 = female)
        self.cp = int(cp)#chest pain type (0,1,2,3)
        self.trestbps = int(trestbps)#resting blood pressure
        self.chol = int(chol)#serum cholesterol
        self.fbs = int(fbs)#fasting blood sugar (is it greater than 120mg/dl? 1 = true; 0 = false)
        self.restecg = int(restecg)#resting ECG (0,1,2)
        self.thalach = int(thalach)#maximum heart rate achieved
        self.exang = int(exang)#exercise enduce angina (1 = yes; 0 = no)
        self.oldpeak = float(oldpeak)#ST depression induced by exercise relative to rest
        self.slope = int(slope)#slope of the peak exercise ST segment (1 = upsloping; 2 = flat; 3 = downsloping)
        self.ca = int(ca)#the number of major vessels(0,1,2,3)
        self.thal = int(thal)#a blood disorder known as 'thalassemia' (3 = normal; 6 = fixed defect; 7 = reversable defect)
        self.target = int(target)#pressence of heart disease (0 = no; 1 = yes)

    #prints the information
    def printPatient(self):
        print("Age: ", self.age, "Sex: ", self.sex, "Chest Pain: ", self.cp, "Blood Pressure: ", self.trestbps, "Cholestorol: ", self.chol, "FBS: ", self.fbs, "Resting ECG: ", self.restecg, "Max heart rate: ", self.thalach, "Exercise enduced angina: ", self.exang, "Oldpeak: ", self.oldpeak, "Slope: ", self.slope, "Major blood vessels: ", self.ca, "Thalassemia: ", self.thal, "Target: ", self.target)
        print('\n')

    ## -------- Actions -------- ##
    #at the moment, these are still 'placeholder actions' that don't adhere to any real science

    #each will lower patient's corresponding attribute by an arbitrary amount

    #action 1
    def lowerBloodPressure(self):
        print("Lowering Blood Pressure...")
        self.trestbps -= 20

    #action 2
    def lowerCholestorol(self):
        print("Lowering Cholestorol...")
        self.chol -= 10

    #action 3
    def lowerMaxHeartRate(self):
        print("Lowering Max Heart Rate...")
        self.thalach -= 50

    #action 4
    def lowerChestPainLevel(self):
        #only lower cp if it is > 0
        if(self.cp > 0):
            self.cp -= 1