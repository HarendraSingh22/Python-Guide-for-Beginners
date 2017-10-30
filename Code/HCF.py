# Program to find HCF in python

def hcf(x, y): # x and y are two integers you can input
  # smaller will be used to store the variable for running the shorter loop
  #comment
  ans = 1
  if (x < y):
    smaller = x
  else:
    smaller = y
  for i in range(2, smaller+1):
    if ((x%i == 0) and (y%i == 0)):
      ans = i
  return ans

print(hcf(27, 6))
    
