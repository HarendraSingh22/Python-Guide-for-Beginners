#!/usr/bin/python


def convertToBinary( num ):
	"function to convert integer to equivalent binary string"
	if (num > 1):
		convertToBinary(num/2)
	print(int(num%2), end="")
	return;

# Getting inpts from user
num = input('Enter the integer: ')

# passing the input to convertToBinary method
print('The binary equivalent of {0} is '.format(num), end=''	)
convertToBinary(int(num))