list=[6,9,19,34,21,43,89]
n=int(input('enter a number'))
for i in range(len(list)):
    if list[i]==n:
        print('found at pos',i+1)
        break
else:
        print('not found')
