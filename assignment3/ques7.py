def summer_69(li,n):
    sum=0
    if li==[]:
        return 0
    else:
     for i in range(n):
        if li[i]!=6 and li[i]!=7 and li[i]!=8 and li[i]!=9:
         sum=sum+li[i]
     return sum

li=[]
n=int(input('enter the number of elements you want in list:'))
for i in range(0,n):
    x=int(input('enter element'))
    li.append(x)
print(summer_69(li,n))