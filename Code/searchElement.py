
def search(a, element):
  for ech in a:
    if ech == element:
        print ("found")
        return
  print ("Not Found")
  return

lst  = [1,2,3,4,5,6,7,8]

element = input("Enter Element: ")

search(lst,int(element))
