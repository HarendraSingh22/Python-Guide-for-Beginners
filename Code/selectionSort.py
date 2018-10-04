def selection_sort(lst):
  #Fucntion for inplace selection sort

   for i in range(len(lst)):
       minPosition = i
   
       for j in range(i+1, len(lst)):
           if lst[minPosition] > lst[j]:
               minPosition = j
              
       temp = lst[i]
       lst[i] = lst[minPosition]
       lst[minPosition] = temp

   return lst
