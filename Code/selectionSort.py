def selection_sort(lst):
    #Fucntion for inplace selection sort, takes in a list lst.
    #Select smallest element form list and add it one position after the previous smallest element.

    for i in range(len(lst)):
    #get position for smallest element to be inserted
        minPosition = i
   
        for j in range(i+1, len(lst)):
        #find next smallest element
            if lst[minPosition] > lst[j]:
                minPosition = j
              
        temp = lst[i]
        #insert smallest element after previous smallest element
        lst[i] = lst[minPosition]
        #get new position for smallest element 
        lst[minPosition] = temp
    return lst
