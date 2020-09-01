def mult(l,n):
    m=1
    for i in range(n):
        m=m*l[i]
    return m

n=int(input('enter total number of elements to be inserted in list:'))
l=[]
print('enter numbers in list :')
for i in range(n):
    x=int(input())
    l.append(x)
print(mult(l,n))