def almost_there(n):
    if abs(100-n)<=10 or abs(200-n)<=10:
        return True
    else:
        return False

n=int(input('enter number'))
print(almost_there(n))
