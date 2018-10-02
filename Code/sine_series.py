#sine series generation 
import math
def fact(n):
    fact=1
    while n!=0:
	 fact*=n
	 n-=1
    return fact
x=input("Enter the value of x: ")
x=x*(math.pi/180)
n=input("Enter the limit: ")
sin=0
for i in range(n):
        sign=(-1)**i
	a=(i*2)+1
	sin+=(sign*(x**a))/(fact(a))
print "The sum of the sine series is: ",sin
