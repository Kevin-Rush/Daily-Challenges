# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

def findK(list, k):
    #take the first item, search the list to see if it adds to K
    #take second item, search list (exclude the first item) to see if it adds to k
    #continue

    found = False
    count = 0
    while count < len(list):
        i = list[count]
        nextNum = count + 1
        print("i: "+str(i))
        while nextNum < len(list):
            print("list[c] "+str(list[nextNum]))
            added = i + list[nextNum]
            if added == k:
                found = True
                return found
            nextNum += 1
        count += 1
    return found


def findK_2(list, k):

    found = False
    i = 0
    j = len(list)-1
    list.sort()

    while i < j:
        print(list)
        sum = list[i] + list[j]
        print(sum)
        if sum < k:
            i += 1
        elif sum > k:
            j -= 1
        else:
            print("Found")
            return True

    return False

def findK_3(n, numbers):
    n = 181
    n2 = n//2
    numbers = [80, 98, 83, 92, 1, 38, 37, 54, 58, 89]
    goodnums = {n-x for x in numbers if x<=n2} & {x for x in numbers if x>n2}
    pairs = {(n-x, x) for x in goodnums}

k = 17
list = [10, 15, 3, 7]
# list = [80, 98, 83, 92, 1, 38, 37, 54, 58, 89]
# k = 181
print(findK(list, k))