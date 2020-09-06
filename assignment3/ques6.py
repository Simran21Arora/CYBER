def blackjack(a,b,c):
    sum=a+b+c
    if sum<=21:
        return sum
    else:
        if a==11 or b==11 or c==11:
            sum=sum-10
            if sum<=21:
                return sum
            else:
                return 'BUST'
        else:
            return 'BUST'
print('enter three integers between 1 & 11')
a=int(input('enter number'))
b=int(input('enter number'))
c=int(input('enter number'))
print(blackjack(a,b,c))