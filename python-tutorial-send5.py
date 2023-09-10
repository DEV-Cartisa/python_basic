#python5


game2 = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],]

print('   a  b  c')
for count, row in enumerate(game2):
    print(count,row)



l = [1,2,3,4,5]

print(l[1])
print(l[-1])
print(l[1:3])

l[1] = 99 
print(l)


game3 = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],]

game3[0][1] = 1 # row column

print('   a  b  c')
for count, row in enumerate(game3):
    print(count,row)

# using functions or have m to repeat code again n again , mess
# functions , when repition 




game6 = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],]


def game_board():
    print('   a  b  c')
    for count, row in enumerate(game6):
        print(count,row)


game_board()
# functiion , just prints it out 

game6[0][1] = 1

game_board()


#---7

def addition(x, y):
    return x+y

z = addition(1,4)

print(z)


game7 = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],]


def game_board(player=0, row=0, column=0):
    print('   0  1  2')
    if player !=0: # if no input
        game7[row][column] = player #?? didnt work without this [ belongs to player?]
    for count, row in enumerate(game7):
        print(count,row)


game_board()
game_board(player=1, row=2, column=1)


game7 = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],]


def game_board(player=0, row=0, column=0, just_display=False):
    print('   0  1  2')
    if not just_display: # if no input
        game7[row][column] = player #?? didnt work without this [ belongs to player?]
    for count, row in enumerate(game7):
        print(count,row)


game_board()
game_board(player=1, row=2, column=1)







