n=int(input('Enter the number of elements:'))
p=[]
w=[]
W=int(input('Enter the weight of the bag:'))
s=[]
print('Enter profit and weight: ')
for i in range(n):
    a,b=[int(j) for j in input().split()]
    p.append(a)
    w.append(b)
    s.append(0)
r=[]
q=[]
for i in range(n):
    a=p[i]/w[i]
    r.append(a)
    q.append(a)
q.sort()
q.reverse()
tp=0
for i in range(n):
    if(W>=w[r.index(q[i])]):
        W=W-w[r.index(q[i])]
        tp=tp+p[r.index(q[i])]
        print("Profit: ",p[r.index(q[i])],"Weight: ",w[r.index(q[i])])
        s[r.index(q[i])]=1
    elif(W!=0):
        tp=tp+(W*r[r.index(q[i])])
        print("Profit: ",(W*r[r.index(q[i])]),"Weight: ",W)
        s[r.index(q[i])]=W/w[r.index(q[i])]
        W=0
print(tp)
print(s)
