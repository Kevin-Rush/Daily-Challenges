# How do you find the duplicate number on a given integer array? 

def remDuplicates(list):

    cleanList = []

    previous = list[0]

    for i in list:
        if i == previous:
            cleanList.append(i)
        previouis = i
    return cleanList

list = {1, 1, 2, 2, 3, 4, 5}
print("Duplicates: ")
print(remDuplicates(list))

# How do you find the largest and smallest number in an unsorted integer array?

def findHL(list):
    high = list[0]
    low = list[0]

    for i in list:
        if i > high:
            high = i
        elif i < low:
            low = 1

    return high, low



list = [1,4,23,6,78,9,4,3,6,8]
print("Find High, Low: ")
print(findHL(list))

# How do you find all pairs of an integer array whose sum is equal to a given number?

def findPairs(list, num):

    pairs = []

    for i in range(len(list)):
        start = list[i]
        for k in range(i+1, len(list)):
            next = list[k]
            if (start + next) == num:
                pairs.append([start,next])


    return pairs


list = [2,4,3,5,2,8,9,6,7,0]
num = 6
print("Find Pairs: ")
print(findPairs(list, num))