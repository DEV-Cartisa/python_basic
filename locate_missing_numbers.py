# locate missing numbers 

def FindingMissingNumbers(n):
    numbers = set(n)
    length = len(n)
    output = []
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
    return output

ListOfNumbers = [1, 2, 3, 5, 6, 8, 8, 10, 11, 12, 14, 15, 17, 18, 19, 20]





print(FindingMissingNumbers(ListOfNumbers))





