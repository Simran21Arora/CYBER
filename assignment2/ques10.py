n=int(input('enter limit :'))
li=[[0 for i in range(n+1)] for j in range(n+1)]
for i in range(1,n+1):
    print('\n')
    for j in range(1,i):
        if j==i-1 or j==1:
            li[i][j]=1
        else:
            li[i][j]=li[i-1][j-1]+li[i-1][j]
        print(li[i][j], end=' ')