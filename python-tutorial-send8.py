#python8
#x



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
