print "To find : "
to_find = input()

print "How many elements are in the list?"
n = input()

print "List : "
List = []

for i in range (0,n):
    x = input()
    List.append(int(x))

begin = 0
end = len(List)-1
mid = int((begin+end)/2)

found = 1
while List[mid] != to_find:
    if List[mid] < to_find:
        begin = mid
        mid = int((begin + end)/2)
    else:
        end = mid
        mid = int((begin + end)/2)
    if end - begin == 1 and end != to_find and begin != to_find:
        print "Item not found!"
        found = 0;
        break

if found == 1:
    print 'Item found at position: ',mid
