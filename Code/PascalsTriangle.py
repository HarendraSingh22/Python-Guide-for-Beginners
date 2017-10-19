# Program to print Pascal's triangle

def PascalsTriangle(n): # (n + 1) rows to be printed. [0th - 5th]
	
	print (1)

	if n > 0:
		a = [1]
		i = 0
		while (i < n):
			x = []
			x.append(a[0])
			for j in range(len(a) - 1):
				x.append(a[j] + a[j + 1])
			x.append(a[-1])

			for element in x:
				print (element, end = ' ')

			print ()
			a = x

			i += 1


PascalsTriangle(10)