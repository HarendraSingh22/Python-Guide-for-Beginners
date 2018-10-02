

memo={}
def fibo(n):
	if n in memo:
		return memo[n]
	if n<=2:
		f=1
	else:
		f=fibo(n-1)+fibo(n-2)
	memo[n]=f
	return f

# print(fibo(1000))


fib={}
def fibos(n):
	for i in range(1,n+1):
		if i<=2:
			f=1
		else:
			f=fib[i-1]+fib[i-2]
		fib[i]=f
	return fib[n]


print(fibo(6))
