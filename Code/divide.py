
#Creating two numbers. The input function will allow the user to enter their own numbers.
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')


#The denominator cannot be 0, so we need to avoid that situation
if num2==0:
	print 'Denominator cannot be 0' 

else:
	Division=float(num1)/float(num2)
	print Division



