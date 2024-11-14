gradelist = []
systemloop = True
grade_number = 0

while systemloop == True:
    grade = input ("Enter the student grade and Type 'Done' if finished:")
    if (grade.isdigit()):
        grade = int(grade)
        
        if (grade >= 40 and grade <= 100):
            grade_number = grade_number + 1
            gradelist.append(grade)
        
        else:
            print("The input number is too low or too high.")
    
    elif (grade == str("done").lower()):
            systemloop = False
    
    else:
        print("Invalid Input, please try again.")

else:
    sum = sum(gradelist)
    final = sum/grade_number
    passing = 0
    
    print("Average Grade:", final)
    
    for grade in gradelist:
        if grade >= 75:
            passing = passing + 1
            
    print ("Passed the Subject:", passing)
    print ("Passing Percentage:", (passing/len(gradelist))*100,"%")
    print("Grade:", gradelist)

            