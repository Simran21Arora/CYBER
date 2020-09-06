def spy_game(li,n):
    for i in range(0,n):
        if li[i]==0:
            x=i+1
            for i in range(x,n):
                if li[i]==0:
                    y=i+1
                    for i in range(y,n):
                        if li[i]==7:
                            return True
    return False

li=[]
n=int(input('enter the number of elements you want in list:'))
for i in range(0,n):
    x=int(input('enter element'))
    li.append(x)
print(spy_game(li,n))