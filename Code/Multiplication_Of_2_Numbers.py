
while True:
  
  print("(enter 'q' to quit anytime.)")
  
  a = input("Enter a number -->")
  if a == 'q':
    break
  else:
    a = int(a)
    
  b=input("Enter a number -->")
  if b == 'q':
    break
  else:
    b = int(b)
    
  print("The product is --> {}".format(a*b))
