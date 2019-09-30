#Program to find maximum of 2 numbers
while 1:
	n,m=map(int, raw_input())
	k = max(m,n)
	print k
	print "Do you want to continue(yes/no): "
	s=raw_input()
	if s=="no":
		break
