
#mean - medium - mode

#Mean
list = [ 3, 5, 6, 2, 22, 12, 24, 33, 26]
mean = sum(list)/len(list)
print(mean)

# Median
list = [ 3, 5, 6, 2, 22, 12, 24, 33, 26]
list.sort()

if len(list) % 2 == 0:
    x1 = list[len(list)//2]
    x2 = list[len(list)//2 -1]
    median = (x1 + x2)/2
else:
    median = list[len(list)//2]
print(median)

#mode

list = [ 3, 5, 6, 2, 22, 12, 24, 33, 26] 
frequency = {}
for i in list:
    frequency.setdefault(i,0)
    frequency[i]+=1
frequent = max(frequency.values())
for i,j in frequency.items():
    if j == frequent:
        mode = i 
print(mode)




