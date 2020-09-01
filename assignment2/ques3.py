def calculate(st):
    u,l=0,0
    for i in st:
        if i.islower()==True:
            l=l+1
        elif i.isupper()==True:
            u=u+1
    print('Number of lower case letters in string are :', l)
    print('Number of upper case letters in string are :', u)


st=input('enter a string')
calculate(st)
