from patient import Patient

## -------- Actions -------- ##
# There is a possiblity here to develop an 'action class' and use inheritance to define the different levels of intensity (and diets) as objects e.g.:
# action -> lowIntensityAction.yoga() or
# action -> highIntensityAction.boxing()
        
class LowIntensityAction():
    def __init__(self):
        self.actions = [0,1,2]#list of the low intensity actions

    def briskWalking(self, state):#action 0
        #step cost: 2
        bps = state.trestbps
        c = state.chol

        if (bps > 100):
            bps -= 1
        if (c > 180):
            c *= 0.95

        return Patient(state.age, bps, c, state.fbs)

    def yoga(self, state):# action 1
        #step cost: 1
        bps = state.trestbps
        c = state.chol

        if (bps > 100):
            bps -= 2
        if (c > 180):
            c *= 0.98
        
        return Patient(state.age, bps, c, state.fbs)

    def pilates(self, state):# action 2
        #step cost: 1
        bps = state.trestbps
        c = state.chol

        if (bps > 100):
            bps -= 1.5
        if (c > 180):
            c *= 0.95
        return Patient(state.age, bps, c, state.fbs)

class MediumIntensityAction():
    def __init__(self):
        self.actions = [3, 4]#list of the medium intensity actions

    def swimming(self, state):#action 3
        #step cost: 3
        bps = state.trestbps
        c = state.chol
        if (bps > 100):
            bps -= 3
        if (c > 180):
            c *= 0.9

        return Patient(state.age, bps, c, state.fbs)

    def jogging(self, state):#action 4
        #step cost: 3
        bps = state.trestbps
        c = state.chol

        if (bps > 100):
            bps -= 4
        if (c > 180):
            c *= 0.98

        return Patient(state.age, bps, c, state.fbs)

class HighIntensityAction():
    def __init__(self):
        self.actions = [5,6]#list of the high intensity actions

    def boxing(self, state):#action 5
        #step cost: 4
        bps = state.trestbps
        c = state.chol

        if (bps > 100):
            bps -= 5
        if (c > 180):
            c *= 0.93

        return Patient(state.age, bps, c, state.fbs)
    
    def hiit(self, state):#action 6
        #step cost: 4
        bps = state.trestbps
        c = state.chol

        if (bps > 100):
            bps -= 6
        if (c > 180):
            c *= 0.95

        return Patient(state.age, bps, c, state.fbs)

class Diet():
    # Ideally, these would be able to directly affect blood sugar levels. 
    # But since fbs is represented as a boolean value that 
    # dictates if it is greater than 120mg/dl (1 = true), 
    # the change from true to false will be based on how deep 
    # in the search true we are (how long the patient has been on the diet).
    # 
    # Dieting will lower your cholesterol faster than blood pressure
    def __init__(self):
        self.actions = [7, 8]#list of the medium intensity actions
    
    def DASHdiet(self, state):#action 7
        #step cost: 2
        bps = state.trestbps
        c = state.chol

        if (bps > 100):
            bps -= 0.4
        if (c > 180):
            c *= 0.9

        return Patient(state.age, bps, c, state.fbs)

    def meditarraneanDiet(self, state):#action 8
        #step cost: 2
        bps = state.trestbps
        c = state.chol

        if (bps > 100):
            bps -= 0.3
        if (c > 180):
            c *= 0.87

        return Patient(state.age, bps, c, state.fbs)
