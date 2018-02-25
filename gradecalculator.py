#!/usr/bin/env python3.5
 
print ("now using Python 3.5\n")
#on 17th October 2017
#by Benjamin ********
 
 
#This program first takes in the values from the CSV file from memory, then places the values in RAM to await the next time the values will be used.
#The computer will then either deem the data replacable or read the data in RAM and send it to the CPU
#Next, computer will then get the next instruction add 1 to the program counter
import csv
 
 
def importData(file):
 
    "This function will read in a CSV file and split each row into separate Lists"
 
    #Create empty Lists(with sensible names) to match the columns/fields in the CSV source file
 
    listOne = []
 
    listTwo =[]
 
    listThree = []
 
    #Open the file using the path provided and assign to a variable for reference
 
    with open(file,"r") as filename:
 
        #Set reader up to parse a CSV file
 
        reader = csv.reader(filename)
 
        for row in reader:
 
            listOne.append(row[0])
 
            listTwo.append(row[1])
 
            listThree.append(row[2])
 
    return (listOne, listTwo, listThree)
 
 
def calcPercentage (courseMark, examMark):
 
    percentList=[]
 
    for index in range (0, 11):
 
        sum = int(courseMark[index]) + int(examMark[index]) #calculate percentage
 
        percentage = sum/150
 
        percentage = round(percentage*100,2)
 
        percentList.append(percentage)
 
    return percentList #return the percentage to the main program
 
def findGrade (percentage):
 
    #use the percentage to then find what grade the pupil had achieved
 
    if percentage>= 70 :
 
            grade = "A"
 
    elif percentage >= 60:
 
            grade = "B"
 
    elif percentage >=50:
 
            grade = "C"
 
    elif percentage >= 45:
 
            grade = "D"
 
    else:
 
        grade = "No Grade"
 
    return grade
 
def display (percentage, grade, name):
 
    print ("{0} got {1} with {2}%!".format(name, grade, percentage))#display the grade and percentage
 
def writeCSVFile(fp,lst1,lst2,lst3,lst4,lst5):
 
    "This procedure opens a disc file from its full filepath and writes all list contents to it"
 
    with open(fp, "w") as myFile:
 
        for index in range(0, 11):
 
            myFile.write("{0},{1},{2},{3},{4}\n".format(lst1[index],lst2[index],lst3[index],lst4[index], lst5[index])) # Write each record to file on a new line
 
def findMax (list):
 
    "search list for maximum value, report and return to a variable"
 
    max = list[0]  # set max to item in pos 0
 
    for i in range(0,len(list)-1):   # for each item in list
 
        if list[i]>max:  # if the item at i > found max
 
            max = list[i]   # set max to the item at i
 
    return max

def input_grade(prompt): # prompt is the prompt you want to show to the user

    # returns the grade in uppercase or "Error" if an incorrect grade is entered. Modify the grades list as desired

    grades = ["A", "B", "C", "D", "E", "F"] # valid grades

    uppercase = input (prompt).upper() # get the input and make it uppercase

    if uppercase not in grades: # if the entered grade is invalid

        return "Error"

    else: # if the entered grade is valid

        return uppercase
 
def countOccurrence (li):
 
    total = 0

    _desired_grade = "" # temporary variable to loop until the user provides a valid input

    _grade_found = False # temporary variable to loop until the user provides a valid input

    while _grade_found == False: # exit when _grade_found is True and _desired_grade is an actual grade

        _desired_grade = input_grade("Enter the grade you're looking for ") # user input

        if (_desired_grade != "Error"): # valid input, no error

            _grade_found = True # set to True and exit the loop
            
    search = _desired_grade # the grade the user wants to find
 
    for i in range(0,len(li)):
 
        if li[i] == search : #check if the item in the list is the grade that the user wants
 
            total = total + 1 #add 1 to the total when the item is the grade the user wants
 
    print ("The program found {0} {1}s".format(total, search)) #display how many of the grade there is
 
    return total
#Main program

while True:
 
    Name =[]
 
    examMark = []
 
    courseMark = []
 
    percentageList = []
 
    gradeList = []
 
    name, examMark, courseMark = importData("/home/bdavidson106/Assessment/AssessmentNames.csv")
 
    percentageList = calcPercentage(courseMark, examMark)
 
    for index in range(0, 11):
 
        grade = findGrade(percentageList[index])
 
        gradeList.append(grade)
 
        display(percentageList[index], gradeList[index], name[index])
 
    writeCSVFile("/home/bdavidson106/Assessment/AssessmentNames.csv", name, courseMark, examMark ,percentageList, gradeList)
 
    maxCourse = findMax (courseMark)
 
    maxExam = findMax (examMark)
 
    maxPercent = findMax (percentageList)
 
    print("Highest coursework mark was ", maxCourse,"\n Largest exam mark was ", maxExam, "\n Largest overall percentage was ", maxPercent)
 
    ocurrences = countOccurrence (gradeList)
