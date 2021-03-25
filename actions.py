from patient import Patient

## -------- Actions -------- ##
    
    ## -- Exercises -- ##
def swimming(state):#action 0
    #step cost: 3
    bps = state.trestbps
    c = state.chol
    if (bps > 100):
        bps -= 4
    if (c > 180):
        c *= 0.9

    return Patient(bps, c, state.fbs)

def jogging(state):#action 1
    #step cost: 2.5
    bps = state.trestbps
    c = state.chol

    if (bps > 100):
        bps -= 3
    if (c > 180):
        c *= 0.98

    return Patient(bps, c, state.fbs)
    

def briskWalking(state):#action 2
    #step cost: 1
    bps = state.trestbps
    c = state.chol

    if (bps > 100):
        bps -= 1
    if (c > 180):
        c *= 0.98

    return Patient(bps, c, state.fbs)

## -- Diets -- ##
    # Ideally, these would directly affect blood sugar levels. 
    # But since fbs is represented as a boolean value that 
    # dictates if it is greater than 120mg/dl (1 = true), 
    # the change from true to false will be based on how deep 
    # in the search true we are (how long the patient has been on the diet).
def DASHdiet(state):#action 3
    #step cost: 2
    bps = state.trestbps
    c = state.chol

    if (bps > 100):
        bps -= 2
    if (c > 180):
        c *= 0.9

    return Patient(bps, c, state.fbs)

def meditarraneanDiet(state):#action 4
    #step cost: 1.5
    bps = state.trestbps
    c = state.chol

    if (bps > 100):
        bps -= 2
    if (c > 180):
        c *= 0.9

    return Patient(bps, c, state.fbs)