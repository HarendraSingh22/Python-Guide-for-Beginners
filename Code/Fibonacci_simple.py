#fibonacci series using recursion

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    

n=input('Fibonacci series total terms? ')
a=[]
for i in range(n):
    a.append(fib(i))

print a
