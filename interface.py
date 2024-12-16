from utils import *
from student import Student
from employee import Employee
from menu import Menu
import pandas as pd
 
def printMenu():
    idx = 1
    for option in Menu:
        print(str(idx) + ". " + option.name.replace("_", " ").capitalize())
        idx += 1

def saveNewEntry(dict_by_id, list_of_person):
    types_of_person = [Employee, Student]
    try:
        id = checkParamIsNumber("ID")
        if id in dict_by_id:
            print("Error: ID already exists: ", end="")
            print(dict_by_id[id].getName() + " - " + str(dict_by_id[id].getAge()))
            return 0

        name = input("Please enter the name: ")

        age = checkParamIsNumber("age")
    except ValueError as e:
        return 0
    
    for idx, person in enumerate(types_of_person):
        str_to_print = str(person).replace("<class '", "").replace("'>", "").split(".")[0]
        if isvowel(str_to_print[0]):
            articule = "an"
        else:
            articule = "a"
        print("If you are " + articule + " " + str_to_print + " - press " + str(idx))

    type_to_create = None
    while type_to_create not in range(len(types_of_person)):
        type_to_create = input()

    type_to_create = int(type_to_create)
    person = types_of_person[type_to_create](id, name, age)
    
    dict_by_id[id] = person
    list_of_person.append(person)     
    print("ID [" + str(id) + "] saved successfully")
    return int(age)
    

def searchById(dict_by_id):
    try:
        id = checkParamIsNumber("ID")
    except ValueError as e:
        return
    
    if id in dict_by_id:
        dict_by_id[id].printMySelf()
    else:
        print("Error: ID " + str(id) + " is not saved")


def printAgesAverage(sum_of_ages, list_of_person):
    if len(list_of_person) == 0:
        print("0")
        return
    res = sum_of_ages / len(list_of_person)
    print(str(res))



def printAllNames(list_of_person):
    for idx, person in enumerate(list_of_person):
        print(str(idx) + ". " + person.getName())



def printAllIds(list_of_person):
    [print(str(idx) + ". " + str(person.getId())) for idx, person in enumerate(list_of_person)]


def printAllEntries(list_of_person):
    [person.printMySelf(idx)  for idx, person in enumerate(list_of_person)]



def printEntryByIndex(list_of_person):
    try:
        idx = checkParamIsNumber("Index")
    except ValueError:
        return

    if idx >= len(list_of_person) or idx < 0:
        printIndexErrorOutOfRange(idx, len(list_of_person))
    else:
        list_of_person[idx].printPerson()


def saveAllData(list_of_person):
    output_filename = input("What is your output file name? ")

    peolpe_list = []
    for person in list_of_person:
        peolpe_list.append(person.mySelfAsDict())

    people_df = pd.DataFrame(peolpe_list)
    people_df.to_csv(output_filename, index = False)


def exitSystem():
    flag = None
    while flag != "y" and flag != "n":
        flag = input("Are you sure you want to exit? (y/n) ")
    if flag == "y":
        print("Goodbye!")
        exit()