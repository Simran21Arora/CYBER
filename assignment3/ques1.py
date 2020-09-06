def pangram(st):
    l="abcdefghijklmnopqrstuvwxyz"
    for char in l:
        if char not in st.lower():
            return("non pangram")
    else:
        return("pangram")
str=input("enter the string")
print(pangram(str))