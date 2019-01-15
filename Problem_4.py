# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, 
# find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# approach to problem:
# sort the array,
# traverse it and compare one integer to the next "expected" int 
# if negative or duplicate, move to the next one
# if not = to expected then end and return numbers

def findLPI(list):
    list.sort()
    count = 1
    length = len(list)
    for i in list:
        if i > 0:
            if count < length and i != list[count]:
                diff = list[count] - i 
                # if the difference is = 1 it's the next int if not then theres a gap, if it's the first gap we 
                # find it is the lowest postive integer
                if diff != 1:
                    return i + 1

        count += 1

    if list[count-2] < 0:
        return 0
    else:
        return list[count-2] + 1

list = [3, 4, -1, 1, 6]
#print (findLPI(list))

# NOTE: for a better solution we can ignroe all values greater than the legnth because if it is greater than the length 
# then it cannot be increasing consecutively

def sortOfSort(arr) :
    for index in range(len(arr)) :
        print("index: " + str(index))
        checkValue = arr[index]
        print("init CV: " + str(checkValue))
        print("init arr: "+str(arr))

        while(checkValue > 0 and checkValue != index and checkValue < len(arr) and arr[checkValue] != checkValue) :
            arr[index] = arr[checkValue]
            arr[checkValue] = checkValue
            checkValue = arr[index]
            print("changed arr: "+str(arr))
            print("Changed checkValue: "+str(checkValue))

    print("arr[1:]: "+str(arr[1:]))
    print("[arr[0]]: "+str([arr[0]]))
    return arr[1:] + [arr[0]]

def findFirstMissingNumber(arr) :
    for x in range(len(arr)) :
        if (x+1 != arr[x]) :
            return x+1
    return len(arr) + 1

list = sortOfSort(list)
print("After Sort: "+str(list))
print(findFirstMissingNumber(list))

# def sortOfSort(list):
#     for i in ragne(len(list)):
#         checkV = list[i]

#         while(checkV > 0 and checkV != i and checkV < len(list) and checkV != list[checkv]): 
#             #why do we need checkV != i?? remove for testing and see what happens
#             list[i] = list[checkV]
#             list[checkV] = checkV
#             checkV = list[i]
#     return list[1:] + [list[0]]