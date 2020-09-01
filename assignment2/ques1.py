def volume(r):
    a=4/3*3.14*r*r*r
    return a

n=int(input('enter the radius of sphere :'))
print('The volume of given sphere is : ' , volume(n))