def BinarySearch(array, low, high, find):

	while low <= high:

		mid = low + (high - low)//2;
		
		
		if array[mid] == find:
			return mid

		
		elif array[mid] < find:
			low = mid + 1

		
		else:
			high = mid - 1
	
	# If the element is not present it returns -1
	return -1


# Sample array
arr = [ 2, 3, 4, 10, 40 ]
find = 2


found = BinarySearch(arr, 0, len(arr)-1, find)

if found != -1:
	print ("Given element %d is found at index %d" %(find, found))
else:
	print ("Given element is not present in the given array")

