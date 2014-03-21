#raw_input() reads every input as a string
#It's up to you, the developer to process the string

name = raw_input("Enter Your First Name: ")
print "Your Name is " , name

#input() that uses raw_input() and then tries to covert the input data to a number using eval()
#will give an error if the input is non-numeric

x = input ("Enter a number: ")
print "You entered :" , x


