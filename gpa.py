def GPA():
    '''
get no of courses
get the unit load for each course 
get the grade for each course
grades have a point from 0.0 - 5.0
unit load * point 
get total unit load 
get the total (unit load * point) = total points 
total points / total unit load
this is the GPA

To get the cummulative
Add the old GPA to the new GPA
Divide by 2
    '''
    currentcumulativepoint = float(input("input current cumulative point: "))
    currenttotalcreditunit = int(input("input current total credit unit so far: "))
    oldgpa = (currentcumulativepoint / currenttotalcreditunit)
    print("your current gpa is " + str(oldgpa.__round__(2)))
    semestercreditload = int(input("how many credit load did you take this semester: "))
    semestercourses = int(input("how many courses did you take this semester: "))
    cgpa = 0
    a = 0
    b = ''
    total_points = 0
    for x in range(semestercourses):
        y = x + 1
        a = int(input("how many unit load is course " + str(y) + " - "))
        b = input("what was your grade in course " + str(y) + (" - "))

        if b == "a" or b == "A":
          b = 5.0
        elif b == "b" or b=="B":
          b = 4.0
        elif b == "c" or b == "C":
          b = 3.0
        elif b == "d" or b =="D":
          b = 2.0
        elif b == "e" or b == 'E':
          b = 1.0   
        elif b == "f" or b == "F":
          b = 0.0 
        
        total_points += a * b

    new_gpa = total_points / semestercreditload
    print("Your GPA for this semester is: {}".format(new_gpa.__round__(2)))
    cgpa = (oldgpa + new_gpa.__round__(2)) / 2
    print("Your cummulative GPS or CGPA is: {}".format(cgpa.__round__(2)))

GPA()  
