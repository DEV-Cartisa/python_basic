#python

game = (0, 0, 0,
        0, 0, 0,
        0, 0, 0)
print(game)


game1 = [0, 0, 0,
         0, 0, 0,
         0, 0, 0]

print(game1)


game1 = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

print(game1)

for row in game1:
    print(row)


#--


print('    0 1 2')
count = 0
game1 = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

for row in game1:
    print(count, row)
    count = count+1 # count +=1

#enumerate 



game2 = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],]

print('   a  b  c')
for count, row in enumerate(game2):
    print(count,row)








