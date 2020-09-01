def inRange(a,b,i):
    if i in range(a,b):
        return True
    elif i==b:
        return True
    else:
        return False

x=int(input('enter the lower range :'))
y=int(input('enter the higher range :'))
n=int(input('enter the number to be checked :'))
print("output will be TRUE if number exists in the range and will be FALSE if not")
print(inRange(x,y,n))



