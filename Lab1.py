import math

#ex 1
def cmmdclist(*args):
    x = math.gcd(*args)
    return x

# print(cmmdclist(12,24,6,18))        

#ex 2
def vowels(seq):
    count = 0
    for letter in seq:
        if letter in ['a','e','i','o','u']:
            count = count + 1
    return count

# print(vowels("abracadabra"))

#ex 3
def substrings(first,second):
    return second.count()

