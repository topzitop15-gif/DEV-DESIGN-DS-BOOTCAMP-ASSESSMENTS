#Student Grades Tracker
#Ask the teacher how many students they want to enter grades for
#For each student: ask for student's name
#For each student: ask for test score
#Check if each score is valid (between 0 and 100)
#Calculate average of all scores
#Who passed(score >= 60)
#Who failed (score < 60)
# The class average
#The highest and lowest score


print("\n" + "="* 50)
print( """" 
      STUDENT GRADES TRACKER
      AUTHOR : TEMITOPE OLUGBAMILA
      DESCRIPTION : A PYTHON PROGRAM THAT TRACKS STUDENT GRADES, CALCULATING THE CLASS AVERAGE, WHO PASSED AND FAILED, AND THE HIGHEST AND LOWEST SCORE
""" )
print("="* 50)
print("="* 50)

#Initialize the variable
total_score = 0
passed_students = []
failed_students = []
all_score = []

#number of student
num_students = int(input("How many students would you like to grade?"))
for num in range (num_students):
    print (f"---Student {num+1} ---")
    

    #Student_name
    student_name = input ("Enter Student's name:")

    #Student_score
    student_score = float(input(f"Enter score for {student_name}:"))
    
    while student_score <0 or student_score >100:
        print("Invalid score! Enter a score between 0 and 100")
        

    #total score    
    total_score = total_score + student_score
    print("The total Student score is:", total_score)

    all_score.append(student_score)

    #Students that passed
    if student_score >= 60 :
        passed_students.append((student_name,student_score))
    else:
        failed_students.append((student_name,student_score))
        

#Class_average
class_average= total_score/num_students

#Highest score
highest_score= max(all_score)

#Lowest_score
lowest_score= min(all_score)

print("\n" + "="* 50)
print("\n STUDENTS WHO PASSED")
for student in passed_students:  
    print(f" {student[0]}:{student[1]}")
print("="* 50) 

print("\n STUDENTS WHO FAILED")
for student in failed_students:  
    print(f" {student[0]}:{student[1]}")
print("="* 50) 
     
print(f"THE CLASS AVERAGE IS: {class_average:.1f}") 
print("="* 50)

print (f"THE HIGHEST SCORE IS: {highest_score:.1f}")
print("="* 50)

print(f"THE LOWEST SCORE IS: {lowest_score:.1f}")
print("="* 50)
        

   



