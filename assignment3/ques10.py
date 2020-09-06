board={ '1':' ','2':' ','3':' ',
        '4':' ','5':' ','6':' ',
        '7':' ','8':' ','9':' ',
      }
moves=0
player=1
end_check=0
def check(plyr1,plyr2):
    #to check if player one has won
    if board['1'] == board['2'] == board['3'] == plyr1:
        print('player one won!')
        return 1
    if board['4'] == board['5'] == board['6'] == plyr1:
        print('player one won!')
        return 1
    if board['7'] == board['8'] == board['9'] == plyr1:
        print('player one won!')
        return 1
    if board['1'] == board['5'] == board['9'] == plyr1:
        print('player one won!')
        return 1
    if board['3'] == board['5'] == board['7'] == plyr1:
        print('player one won!')
        return 1
    if board['1'] == board['4'] == board['7'] == plyr1:
        print('player one won!')
        return 1
    if board['2'] == board['5'] == board['8'] == plyr1:
        print('player one won!')
        return 1
    if board['3'] == board['6'] == board['9'] == plyr1:
        print('player one won!')
        return 1

    #to check if player two has won
    if board['1'] == board['2'] == board['3'] == plyr2:
        print('player two won!')
        return 1
    if board['4'] == board['5'] == board['6'] == plyr2:
        print('player two won!')
        return 1
    if board['7'] == board['8'] == board['9'] == plyr2:
        print('player two won!')
        return 1
    if board['1'] == board['5'] == board['9'] == plyr2:
        print('player two won!')
        return 1
    if board['3'] == board['5'] == board['7'] == plyr2:
        print('player two won!')
        return 1
    if board['1'] == board['4'] == board['7'] == plyr2:
        print('player two won!')
        return 1
    if board['2'] == board['5'] == board['8'] == plyr2:
        print('player two won!')
        return 1
    if board['3'] == board['6'] == board['9'] == plyr2:
        print('player two won!')
        return 1
    return 0

print(' 1 | 2 | 3 ')
print('___|___|___')
print(' 4 | 5 | 6 ')
print('___|___|___')
print(' 7 | 8 | 9 ')
print('   |   |   ')
print('**********************')
plyr1 = input('player one enter your choice "X" or "O" ')
if plyr1 == 'x':
    plyr2 = 'o'
elif plyr1 == 'o':
    plyr2 = 'x'
else:
    print('wrong input enter again')
while True:
    print(" "+board["1"]+" | "+" "+board["2"]+"| "+" "+board["3"]+" ")
    print('___|___|___')
    print(" "+board["4"]+" | "+" "+board["5"]+"| "+" "+board["6"]+" ")
    print('___|___|___')
    print(" "+board["7"]+" | "+" "+board["8"]+"| "+" "+board["9"]+" ")
    print('   |   |   ')
    print('**********************')
    end_check=check(plyr1,plyr2)
    if moves==9 or end_check==1:
        break
    while True:
        if player==1:
          p1=input("player one's turn")
          if p1 in board and board[p1]==' ':
             board[p1]=plyr1
             player=2
             break
          else:
              print('wrong input!, enter value again')
              continue
        else:
            p2 = input("player two's turn")
            if p2 in board and board[p2] == ' ':
                board[p2] = plyr2
                player = 1
                break
            else:
              print('wrong input!, enter value again')
        moves+=1
        print("**********************")


