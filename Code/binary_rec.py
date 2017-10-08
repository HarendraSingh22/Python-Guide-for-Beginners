def convertToBinary(n):
   """Function to print binary number
   for the input decimal using recursion"""
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

# decimal number
#Taking user input
num = input('Enter number: ')

#Diplay the output
convertToBinary(int(num))