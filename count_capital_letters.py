
with open('textfile.txt') as x1:
    count = 0 
    text = x1.read()
    for i in text:
        if i.isupper():
            count +=1
        print(count)

#lower case

with open('textfile.txt') as x1:
    count = 0
    text = file.read()
    for i in text:
        if i.islower():
            count +=1
    print(count)
    


