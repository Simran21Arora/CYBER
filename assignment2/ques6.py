def palindrome(st):
    if st==st[::-1]:
        print(st ,'is a palindrome string')
    else:
        print(st ,'is not a palindrome string')

st=input('enter a string :')
palindrome(st)
