numToChange = input()
binList = []
while numToChange > 0:
    binList.append(numToChange%2)
    numToChange/=2

length = len(binList)-1
ans=0
while length>=0:
    ans*=10
    ans+=binList[length]
    length-=1
print ans
