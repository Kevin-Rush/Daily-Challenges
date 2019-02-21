# This problem was asked by Twitter.
# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, 
# return all strings in the set that have s as a prefix.

# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries


def fillBrute(frac, list):

    matches = []
    fracLen = len(frac)

    for i in list:                  #simple brute force method
        if len(i) >= fracLen:
            beg = i[0:fracLen]
            if beg == frac:
                matches.append(i)
    return matches

frac = "de"
list = ["dog", "deer", "deal"]
#print(fill(frac, list))


                
# need to take a fraction of a word and return all words that begin with the fraction

# if word.legnth < frac.length then we ignore the word because it's too small (i.e. do nothing)

# if word.length >= frac.length then we can consider it

# compare word[0:frac.length] because we just have to look at the first letters of the word 

# if they match then include the word in the list to return

# if they don't match don't add it (i.e. do nothing)



# how can we store a dictionary in a DS?
#     BST? how do I choose a root, how do I split it up? alphabetically
#     research best ways to store a dictionary

# https://www.cs.helsinki.fi/u/tpkarkka/opetus/10s/spa/lecture07.pdf

# what I can do is store it in a BST where the root is = the first letter of the first word
# then you have the word fill out on the right 

# or what about a Tree where the root = -1 and then has a child where each branch is a word with the same
# first letter and then all of it's children are then spelt out as nodes and this will build the permutations
# of each word 


