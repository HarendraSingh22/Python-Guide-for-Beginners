
firstnum = int(input("First number: "))
secondnum = int(input("Second number: "))

if secondnum == 0:
	print("Division by zero illegal.")
else:
	print("The result is " + str(firstnum/secondnum))