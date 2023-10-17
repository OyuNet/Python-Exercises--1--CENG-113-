homeworkGrade = float(input("Enter your homework grade: "))
midtermGrade = float(input("Enter your midterm grade: "))
finalGrade = float(input("Enter your final grade: "))

couseGrade = float((homeworkGrade/10) + (midtermGrade*3/10) + (finalGrade*6/10))

print("Your course grade is", couseGrade)