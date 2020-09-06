def lesserOfTwo(a,b):
    if a%2==0 and b%2==0:
        if a<b:
            return a
        else:
            return b
    else:
        if a>b:
            return a
        else:
            return b
x=int(input('enter 1st number'))
y=int(input('enter 2nd number'))
print(lesserOfTwo(x,y))