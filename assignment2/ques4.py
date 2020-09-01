def unique(l1,n):
    l2=[]
    for i in l1:
        if i not in l2:
            l2.append(i)
    print(l2)

n=int(input('enter total number of elements to be inserted in list:'))
l=[]
for i in range(n):
    x=input()
    l.append(x)
unique(l,n)
