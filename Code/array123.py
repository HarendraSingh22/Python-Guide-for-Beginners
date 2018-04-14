
'''
Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.


array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True  '''

def array123(nums):
  
  for index in range (0,len(nums)-2):
    
      if(nums[index] == 1 and nums[index+1] == 2 and nums[index+2] == 3):
        return True
        break
      
  return False

num_list = [1, 1, 2, 1, 2, 3]  
print(array123(num_list))