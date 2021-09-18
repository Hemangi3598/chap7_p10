# wapp to read tuple of names and print 
# the names in reverse , alpha order

names = ()
res = input(" do u want enter names y/n ")
while res == "y":
	n = input(" enter name ")
	names = names + (n,) # , is used so that names is converted to tuples
	res = input("do you want to enter moye y/n ")
print(names)

#s1 : convert tuple to list
d1 = list(names)

# s2 : sort the list in rev alpha
d1.sort(reverse=True)

#s3 : convert list to tuple
names = tuple(d1)

print(names)
