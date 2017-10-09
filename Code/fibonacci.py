a,b = 0,1
n= int(input("Enter number of terms : "))
print(a)
for i in range(n):
    a , b = b , a+b;
    print (a)


