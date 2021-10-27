import numpy as np
x = int(input())  
x=x*3.14159/180
t=x
sum=0 
# Loop to calculate the value of Sine */
for i in np.arange(x) :
    t=(t*(-1)*x*x)/(2*i*(2*i+1)) 
    sum += sum
    print(" The value of Sin",x,sum)
