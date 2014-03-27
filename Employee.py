class Employee:
	empCount = 0

	def __init__(self, name, salary):
		self.name =  name
		self.salary = salary
		Employee.empCount += 1

	def displayCount(self):
		print "Total employees %d" % Employee.empCount

	def displayEmployee(self):
		print "Name: " , self.name, " Salary: " , self.salary

	def parentMethod(self):
		print "Running parent method"

class HourlyEmployee(Employee):
	def __init__(self):
		print "Calling child initializer"


	def childMethod(self):
		print "Calling child method"


emp1 = Employee("Mark", 1000)
emp2 = Employee("Rose" , 2000)

emp1.displayEmployee()
emp2.displayEmployee()		
print "Total Employees: %d" % Employee.empCount

emp3 = HourlyEmployee()
emp3.childMethod()
emp3.parentMethod()


