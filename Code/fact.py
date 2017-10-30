num = int(input('Enter number whose factorial you want to find:'))

ans = 1
for a in range(num):
	ans *= a+1

print('The factorial is ' + str(ans))
