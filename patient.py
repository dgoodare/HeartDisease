
## ------------------------------- ##
## -------- Patient Class -------- ##
## ------------------------------- ##
# a class to represent a single patient, this class will also be used to represent a 'state'
# for a search problem
class Patient:
    #constructor
    def __init__(self, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, target):
        #self.age = int(age)#age of the patient
        #self.sex = int(sex)#sex of the patient (1 = male; 0 = female)
        #self.cp = int(cp)#chest pain type (0,1,2,3)
        self.trestbps = int(trestbps)#resting blood pressure
        self.chol = int(chol)#serum cholesterol
        self.fbs = int(fbs)#fasting blood sugar (is it greater than 120mg/dl? 1 = true; 0 = false)
        #self.restecg = int(restecg)#resting ECG (0,1,2)
        #self.thalach = int(thalach)#maximum heart rate achieved
        #self.exang = int(exang)#exercise enduce angina (1 = yes; 0 = no)
        #self.oldpeak = float(oldpeak)#ST depression induced by exercise relative to rest
        #self.slope = int(slope)#slope of the peak exercise ST segment (1 = upsloping; 2 = flat; 3 = downsloping)
        #self.ca = int(ca)#the number of major vessels(0,1,2,3)
        self.thal = int(thal)#a blood disorder known as 'thalassemia' (3 = normal; 6 = fixed defect; 7 = reversable defect)
        #self.target = int(target)#pressence of heart disease (0 = no; 1 = yes)

        self.onDiet = False#can't be on several diets at once
        self.onExercise = False#can't do multiple exercise programs at the same time

        self.timePassed = 0#measures the time elapsed in months

    #prints the information
    def printPatient(self):
        #print("Age: ", self.age, "Sex: ", self.sex, "Chest Pain: ", self.cp, "Blood Pressure: ", self.trestbps, "Cholestorol: ", self.chol, "FBS: ", self.fbs, "Resting ECG: ", self.restecg, "Max heart rate: ", self.thalach, "Exercise enduced angina: ", self.exang, "Oldpeak: ", self.oldpeak, "Slope: ", self.slope, "Major blood vessels: ", self.ca, "Thalassemia: ", self.thal, "Target: ", self.target)
        print("[Blood Pressure (mm/Hg):", self.trestbps, "]    [Serum Cholesterol (mg/dl):", self.chol, "]    [Is Fasting Blood Sugar above 120mg/dl? (1=true, 0=false):", self.fbs, "]    [Thalassemia (1=Normal, 2=Fixed Defect, 3=Reversable Defect)", self.thal , ']')
        print('\n')

    ## -------- Actions -------- ##
    
    ## -- Exercises -- ##
    def swimming(self):#action 0
        self.trestbps -= 4
        self.chol *= 0.9

    def jogging(self):#action 1
        self.trestbps -= 3
        self.chol *= 0.8

    def briskWalking(self):#action 2
        self.trestbps -= 1
        self.chol *= 0.95

    ## -- Diets -- ##
    # Ideally, these would directly affect blood sugar levels. 
    # But since fbs is represented as a boolean value that 
    # dictates if it is greater than 120mg/dl (1 = true), 
    # the change from true to false will be based on how deep 
    # in the search true we are (how long the patient has been on the diet).
    def DASHdiet(self):#action 3
        self.trestbps -= 6
        self.chol *= 0.85

    def Meditarranean(self):#action 4
        self.trestbps -= 5
        self.chol *= 0.8

    ## ---- Checks ----##
    def bloodPressureCheck(self):
        #returns an integer value corresponding to one of
        #low, normal, high, very high (1,2,3,4)
        #Sources:
        #https://www.cdc.gov/bloodpressure/about.htm
        #https://www.nhs.uk/conditions/low-blood-pressure-hypotension/
        if (self.trestbps < 90):
            #low blood pressure
            return 1
        elif ((self.trestbps >= 90) and (self.trestbps < 120)):
            #normal blood pressure
            return 2
        elif ((self.trestbps >= 120) and (self.trestbps < 140)):
            #high blood pressure
            return 3
        else:
            #Very high blood pressure
            return 4

    def cholesterolCheck(self):
        #returns an integer value corresponding to one of
        #normal, high, very high (1,2,3)
        #Sources:
        #https://www.medicalnewstoday.com/articles/315900#recommended-levels
        if (self.chol > 200):
            #normal cholesterol
            return 1
        elif ((self.chol >= 200) and (self.chol < 240)):
            #high cholesterol
            return 2
        else:
            #very high cholesterol
            return 3

