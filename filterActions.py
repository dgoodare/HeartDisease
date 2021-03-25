def filterPressure(doableActions, level):
    #removes any actions that would be made dangerous by having high/low blood pressure
        if (level == 1):
            # the patient has low blood pressure 
            # and should not do any intense exercise in case they pass out.
            # Remove: swimming, jogging
            doableActions[0] = doableActions[1] = False
        elif (level == 2):
            # the patient has normal blood pressure
            # so all actions are available 
            # remove: nothing
            pass
        elif (level == 3):
            # the patient has high blood pressure
            # and should not do any intense exercise without consulting a doctor
            # remove: swimming, jogging
            doableActions[0] = doableActions[1] = False
        else:
            # the patient has VERY high blood pressure
            # and should not start ANY new exercises, should focus on their diet instead
            # remove: swimming, jogging, brisk walking
            doableActions[0] = doableActions[1] = doableActions[2] = False
        
        return doableActions

def filterCholesterol(doableActions, level):
#Having high cholesterol won't prevent someone from doing a particular exercise,
# but it is better to consider dieting to lower high cholesterol levels
    if (level == 1):
        #the patient has normal cholesterol
        #remove: nothing
        pass
    elif (level == 2):
        #the patient has high cholesterol
        #remove: nothing
        pass
    else:
        #the patient has VERY high cholesterol
        # should focus on diet and light exercise until cholesterol has lowered more
        #remove: swimming, jogging
        doableActions[0] = doableActions[1] = False

    return doableActions

def filterBloodSugar(doableActions, depth):
    return doableActions