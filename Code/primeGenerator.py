prime=[]
#Implementing Sieve of Erathotenes Algorithm
for i in range(10000):
	prime.append(True)
for i in range(10000):
	#0 and 1 arent prime numbers
	if(i <= 1):
		prime[i]=False
	else:
		#If it's prime number
		if(prime[i]):
			#Apply false value for any multiples of current prime number
			for j in range(i*i,10000,+i):
				prime[j]=False
n=int(input('Insert range value = '))
#Print prime numbers 0..n
for i in range(n+1):
	if(prime[i]):
		print(i) 







