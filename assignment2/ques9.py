import sys

n=int(sys.argv[1])
a,b=0,1
for i in range(0,n):
    c=a+b
    b,a=a,c
    print(a)

