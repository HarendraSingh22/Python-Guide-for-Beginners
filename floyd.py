r=int(input("enter number of rows: "))
#t=(r*(r+1))//2
c=1
for i in range(r):
	for j in range(i+1):
		print(c, end=" ")
		c+=1
	print("")




