while 1:
	n,m=map(int, raw_input().split())
  a,b=n,m
	while m:
		n,m=m, n%m
	print "hcf = %d\nlcm = %d" %(n, a*b/n)
	print "Do you want to continue(yes/no): "
	s=raw_input()
	if s=="no":
		break
