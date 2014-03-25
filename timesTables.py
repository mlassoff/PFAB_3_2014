import random

values = [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8, 9 , 10, 11 , 12]
values.append(13)

for x in values:
	print x * 2

sports = ["Tennis" , "Baseball" , "Football" , "Football" , "Wrestling" ]

print sports.count("Football")   #Returns the number of instances of Football
print sports.index("Wrestling")  #Returns the index of wrestling

names = ["Judy", "Tom" , "Eve" , "Kristin" , "Blair" , "Tootie", "Jo" , "Edna" ]

names.sort()   #Returns nothing-- Sorts the list in the names variable

print names

randomName = random.randint(0,8)
print names[randomName]

