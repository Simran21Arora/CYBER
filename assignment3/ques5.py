def next(li,n):
    for i in range(0,n):
        if i==n-1:
            break
        elif li[i]==3 and li[i+1]==3:
            return True
    return False

li=[]
n=int(input('enter the number of elements you want in list:'))
for i in range(0,n):
    x=int(input('enter element'))
    li.append(x)
print(next(li,n))