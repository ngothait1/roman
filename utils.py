def isvowel(char):
    return char.lower() in "aeiou"

def checkParamIsNumber(param_name, float_value = False):

    param = input("Please enter the " + param_name + ": ")
    try:
        if float_value:
            return float(param)
        else:
            return int(param)
    except ValueError as e:
        printParamErrorNotNumber(param, param_name)
        raise e
    
def printParamErrorNotNumber(param, param_name):
    print("Error, " + param_name + " must be a number. " + param + " is not a number")

def printIndexErrorNotNumber(idx):
    print("Error, index must be a number. " + idx + " is not a number")

def printIndexErrorOutOfRange(idx, num_people):
    if idx >= num_people:
        print("Error, Index out of range. The maximum index allowed is " + str(num_people - 1))
    elif idx < 0:
        print("Error, Index out of range. The minimum index allowed is 0")
