average = input("Enter the student's average: ")
grade = "F"

if average >= 90:
	grade = "A"
elif average >= 80:
	grade = "B"
elif average >= 70:
	grade = "C"
elif average >= 60:
	grade = "D"

print "The grade is " , grade

