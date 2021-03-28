
## ------------------------------- ##
## -------- Patient Class -------- ##
## ------------------------------- ##
# a class to represent a single patient, this class will also be used to represent a 'state'
# for a search problem
class Patient:
    #constructor
    #def __init__(self, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, target):
    def __init__(self, age, trestbps, chol, fbs):
        self.age = int(age)#age of the patient
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
        #self.thal = int(thal)#a blood disorder known as 'thalassemia' (3 = normal; 6 = fixed defect; 7 = reversable defect)
        #self.target = int(target)#pressence of heart disease (0 = no; 1 = yes)


    #prints the information
    def printPatient(self):
        print("[Age: ", self.age, "]    [Blood Pressure (mm/Hg):", self.trestbps, "]    [Serum Cholesterol (mg/dl):", self.chol, "]    [Is Fasting Blood Sugar above 120mg/dl? (1=true, 0=false):", self.fbs, "]")
        print("Risk Level (0-2 is low, 3-5 is medium and 6+ is high):", self.getRiskLevel())

    ## ---- Checks ----##
    # each will return an integer corresponding to the patient's risk level in the given category
    # these values will be combined to given an overall risk level for the patient
    def ageCheck(self):
        #returns an integer corresponding to the patient's age
        #Sources:
        #https://www.cdc.gov/physicalactivity/basics/age-chart.html
        # https://www.thehealthy.com/exercise/best-workout-every-age/
        # the cdc provides recommendations for both children and adolescents,
        # but there are no people in the dataset under the age of 29, so these age groups don't need to be considered

        if (self.age < 50):
            return 0
        elif ((self.age >=50) and (self.age < 65)):
            return 1
        else:
            return 2

    def bloodPressureCheck(self):
        #returns an integer value corresponding to one of
        #low, normal, high, very high (0,1,2,3)
        #Sources:
        #https://www.cdc.gov/bloodpressure/about.htm
        #https://www.nhs.uk/conditions/low-blood-pressure-hypotension/
        if (self.trestbps < 90):
            #low blood pressure
            return 1
        elif ((self.trestbps >= 90) and (self.trestbps < 120)):
            #normal blood pressure
            return 0
        elif ((self.trestbps >= 120) and (self.trestbps < 140)):
            #high blood pressure
            return 2
        else:
            #Very high blood pressure
            return 3

    def cholesterolCheck(self):
        #returns an integer value corresponding to one of
        #normal, high, very high (1,2,3)
        #Sources:
        #https://www.medicalnewstoday.com/articles/315900#recommended-levels
        if (self.chol < 200):
            #normal cholesterol
            return 0
        elif ((self.chol >= 200) and (self.chol < 240)):
            #high cholesterol
            return 1
        else:
            #very high cholesterol
            return 2

    def sugarCheck(self):
        if (self.fbs == 0):
            return 0
        if (self.fbs == 1):
            return 1

    def getRiskLevel(self):
        return (self.ageCheck() + self.bloodPressureCheck() + self.cholesterolCheck() + self.sugarCheck())