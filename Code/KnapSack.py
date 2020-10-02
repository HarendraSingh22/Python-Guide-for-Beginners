#W->Weight of the bag
#n->No. of items
#w->List of available weights
#v->Values of items
W=int(input('Enter the weight of the bag: '))
n=int(input('Enter the number of items: '))
w=[]
v=[]
table=[]
use=[]
for i in range(n+1):
    for j in range(W+1):
        use.append(0)
    table.append(use)
    use=[]
print(table)
print('Enter the weights and values: ')
for i in range(n+1):
    x,y=[int(k) for k in input().split()]
    w.append(x)
    v.append(y)
for i in range(1,n+1):
    for j in range(1,W+1):
        if(j<w[i]):
            table[i][j]=table[i-1][j]
        elif(j>=w[i]):
            table[i][j]=max(v[i]+table[i-1][j-w[i]],table[i-1][j])
print(table)
i=n
j=W
tw=0
tp=0
while(table[i][j]!=0):
    if(table[i][j]==table[i-1][j]):
        i=i-1
    else:
        if(j<w[i]):
            tw=tw+w[i]
            tp=tp+v[i]
            print(table[i][j])
            i=i-1
        else:
            tw=tw+w[i]
            tp=tp+v[i]
            print(table[i][j])
            i=i-1
            j=j-w[i]
print("Total Weight: ",tw)
print("Total Profit: ",tp)
