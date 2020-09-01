def prime(i,n):
    c=0
    if i==1:
        value='Non Prime'
    elif i==2:
        value='Prime'
    else:
        for j in range(2,n+1):
            if i%j==0:
                c=c+1
        if c==1:
            value='Prime'
        else:
         value = 'Non Prime'
    return value

n=int(input('enter limit :'))
d={i:prime(i,n) for i in range(1,n+1)}
print(d)
count=0
for i in range(1,n+1):
    if prime(i,n)=='Non Prime':
        del d[i]
        count = count + 1
print('number of non prime key-value pairs are :',count)
print('Prime dictionary = ')
print(d)