# Contributed by @Hinal-Srivastava 
def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    elif n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
  
# Driver Program 
n = int(input("Enter Number: "))  
print(Fibonacci(n)) 