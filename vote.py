age = input("How old are you: ")
citizen = raw_input("Are you a citizen (Y/N): ")

#and is the bitwise operator that joins the conditions
#or is another possible operator that can join conditions

if age >= 18 and citizen == "Y":
   print "Congratulations!"
   print "You are old enough to vote and elgiible"
else:
   print "You are inelgiible to vote"
   print "Sorry, Charlie"
print "EOE"

