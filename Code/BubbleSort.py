def BubbleSort(array):
	n = len(array)

	
	for i in range(n):

		
		for j in range(0, n-i-1):

			if array[j] > array[j+1] :
				array[j], array[j+1] = array[j+1], array[j]

#Test code
arr = [75, 44, 35, 22, 32, 11, 96]

BubbleSort(arr)

print ("The sorted array is:")
for i in range(len(arr)):
	print ("%d" %arr[i]), 

