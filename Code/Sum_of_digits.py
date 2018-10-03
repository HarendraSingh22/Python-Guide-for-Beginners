t = input("Enter the number of test cases\n") 
for i in range(t):
    tot = 0
    x = input("Enter the number\n")
    y = str(x) #converted x into a string y
    n = len(y) #calculated length of the string y
    for i in range(n):
        tot = tot + x%10
        x = x/10
    print tot
