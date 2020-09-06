li=[]
n=int(input('enter the number of words in sentence :'))

for i in range(n):
    x=input()
    li.append(x)

s=' '
s=s.join(li[::-1])
print(s)