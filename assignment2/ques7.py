n=int(input('enter limit :'))
li=[]
t=()
for i in range(1,n+1):
    c=0
    if i==1:
        t=(i,'Non Prime')
    elif i==2:
        t=(i,'Prime')
    else:
        for j in range(2,n+1):
            if i%j==0:
                c=c+1
        if c==1:
            t=(i,'Prime')
        else:
            t=(i,'Non Prime')
    li.append(t)
print(li)