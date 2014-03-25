teams = ["Yankees", "Mets", "Giants", "Jets" , "Rangers" , "Knicks" , "Nets"]

print teams[0]    #Yankees
print teams[0:3]   #Yankees, Mets, Giants

teams[6] = "Islanders"  #Add Islanders to list in index 6, which replaces Nets
print teams
del teams[3]  #Delete element at third index
print teams[3]

print len(teams)  #Length of the list-- 6 Because one member was deletd

print "########################################"

teamLen = len(teams)
i = 0
while i < teamLen:
	print teams[i]
	i = i +1

print "#######################################"

for x in teams:
	print "Team: " , x



