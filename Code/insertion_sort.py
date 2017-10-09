# Insertion sort
elem_num = input('Enter the number of elements: ')
a_list = list()
print "Enter the elements:"
for item in range(elem_num):
    elem = input()
    a_list.append(elem)
print a_list, 'Before sort!'
for j in range(1, elem_num):
    key = a_list[j]
    i = j - 1
    while i > -1 and a_list[i] > key:
        a_list[i + 1] = a_list[i]
        i = i - 1
    a_list[i + 1] = key

print a_list, 'After sort!'
