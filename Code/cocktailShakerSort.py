"""
Python implementation of cocktail-shaker sort.

This function sorts a given list of integers in ascending order.

The basic algorithm is almost identical to bubble sort, but with an extra step.
Instead of just sorting the largest unsorted number to the end each pass, this
algorithm moves the lowest unsorted number to the start each pass as well.
"""

def cocktailShakerSort(arr):
    swaps = True #Flag for early finish if there is nothing more to swap.
    for i in range(len(arr) - 1, -1, -1): #Loop as many times as there are items in the list
        if swaps == False: #If nothing was swapped last time
            return arr #Return the sorted list
        swaps = False #Reset the swaps flag
        for j in range(0, i): #for each unsorted item
            if arr[j] > arr[j + 1]: #compare the item to the next value along
                arr[j], arr[j + 1] = arr[j + 1], arr[j] #swap if the j value is higher
                swaps = True #Set the swaps flag
        for k in range(i-1, -1, -1): #loop back through the list
            if arr[j] < arr[j - 1]: #compare the item to the value preceding it
                arr[j], arr[j - 1] = arr[j - 1], arr[j] #swap if the j value is lower
                swaps = True #Set the swaps flag
    return arr #Return the sorted list


#Example sorts
print(cocktailShakerSort([1,2,3,4,5]))
print(cocktailShakerSort([5,4,3,2,1]))
print(cocktailShakerSort([11,12,-4,3.8,9999999999,0]))
print(cocktailShakerSort([8,4,78,127,8234,9,2,235,9,23549,23425,95678,123,66,479,345323,54]))
print(cocktailShakerSort([-70,-80,300,600,12,47,18,8.5,-1**1]))
