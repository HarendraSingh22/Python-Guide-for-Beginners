
# Code to find if a number is palindrome
import sys

if __name__ == '__main__':
	num = str(input('Enter the number to find if it is a palindrome: '))

	try:
		num = int(num)
	except Exception as e:
		print("Not a number.")
		sys.exit(-1)

	num = str(num)
	if num == num[::-1]:
		print("It is a palindrome.")
	else:
		print("It is not a palindrome.")

