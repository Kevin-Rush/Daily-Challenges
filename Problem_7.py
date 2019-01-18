# This problem was asked by Facebook.

# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.

# Note: 
#     - Base case is when there is one diget 
#     - Any combination of digets that is above 26 is irrelevant

def decode(message):

    count = 0

    if len(message) == 1:
        count = 1
    else:
        print("hi")
        if int(message) > 26 and len(message) == 2:
            count = 2
        else: #if int(message) > 26:
            print("hello")
            curNum = 0
            nextNum = 1
            print(len(message))
            while nextNum < len(message):
                possible = int(message[curNum] + message[nextNum])
                if possible < 27:
                    count += count
                    curNum += 1
                    nextNum += 1 


    return count

message = '111'
print(decode(message))
