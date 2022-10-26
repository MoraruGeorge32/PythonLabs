#Ex 1
import copy
import math

def nFibo(n):
    array = [0,1]
    if n <= 1:
        return 0
    else:
        i = len(array)
        while i<n:
            number = array[i-1]+array[i-2]
            array.append(number)
            i=i+1
        return array

# print(nFibo(30))

# print(nFibo(3))

# print(nFibo(8))

#Ex 2
def checkPrim(x):
    if x==2:
        return True
    if (x<2 or x%2==0):
        return False
    else:
        for i in range(3,math.ceil(math.sqrt(x))+1,2):
            if(x%i==0):
                return False
    return True

def checkPrimArray(array):
    arr=[]
    for element in array:
        if checkPrim(element):
            arr.append(element)
    return arr

# print(checkPrimArray([1,2,6,7,11,13,25,14,8,49]))\

#Ex 3
def intersection(a,b):
    arr = []
    for element in a:
        if element in b:
            arr.append(element)
    return arr

def reunion(a,b):
    arr = copy.deepcopy(a)
    for element in b:
        if element not in arr:
            arr.append(element)
    arr.sort()
    return arr

def elimination(a,b):
    arr = []
    for element in a:
        if element not in b:
            arr.append(element)
    return arr

def operations(a,b):
    a.sort()
    b.sort()
    print(intersection(a,b))
    print(reunion(a,b))
    print(elimination(a,b))
    print(elimination(b,a))

# operations([1,3,5,6,7,8],[2,4,5,6])

#Ex 4
def compose(notes, steps, initialStep):
    arr = []
    arr.append(notes[initialStep])
    for step in steps:
        initialStep = initialStep+step
        if initialStep > len(notes):
            initialStep = initialStep % len(notes)
        arr.append(notes[initialStep])
    return arr

# print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))

#Ex 5
def replaceZero(a):
    if len(a) != len(a[0]) or len(a)<1:
        print("Wrong input!")
    for row in range(0,len(a)):
        for col in range(0,row):
            a[row][col] = 0
    return a

# print(replaceZero([[1,3,5],[1,6,8],[2,4,6]]))

#Ex 6
def count(lines,x):
    arr = []
    allLines = []
    for line in lines:
        allLines = allLines + copy.deepcopy(line)
    for element in allLines:
        if allLines.count(element) == x:
            if element not in arr:
                arr.append(element)
    return arr

# print(count([[1,2,3],[2,3,4],[4,5,6],[4,1,"test"]],2))
        
#Ex 7
def palindrome(x):
    return str(x) == str(x)[::-1]

def tuplePalindrome(list):
    res = [0,0]
    for element in list:
        if palindrome(element):
            res[0] = res[0] + 1
            if (element>res[1]):
                res[1] = element
    return tuple(res)

# print(tuplePalindrome([121,323,545,12321]))

#Ex 8
def asciiCode(x=1, array=[], Flag=True):
    listOfLists=[]
    for string in array:
        arr = []
        for letter in string:
            if Flag:
                if ord(letter)%x==0:
                    arr.append(letter)
            else:
                if ord(letter)%x==1:
                    arr.append(letter)
        listOfLists.append(arr)
    return listOfLists

# print(asciiCode(2,["test","hello","lab002"],False))

#Ex 9
def field(a):
    if len(a) < 2:
        return []
    else:
        arr = []
        for row in range(1,len(a)):
            for col in range(0,len(a[row])):
                for frontSeat in range(row-1,-1,-1):
                    if a[row][col] <= a[frontSeat][col]:
                        arr.append((row,col))
                        break
        return arr

# print(field([[1,2,3,2,1,1],[2,4,4,3,7,2],[5,5,2,5,6,4],[6,6,7,6,7,5]]))

#Ex 10
def tuples(lists):
    max_length = max([len(x) for x in lists])
    for list in lists:
        while len(list)<max_length:
            list.append(None)
    arr = []
    index = 0 
    while index < max_length:
        second_arr = []
        for list in lists:
            second_arr.append(list[index])
        arr.append(tuple(second_arr))
        index = index + 1
    return arr

# print(tuples([[1,2,3],[5,6,7],["a","b","c"]]))

#Ex 11
def sortTuples(list):
    list.sort(key=lambda x:x[1][2])
    return list

# print(sortTuples([('abc','bcd'),('abc','zza')]))

#Ex 12
def group_by_rhyme(list):
    arr = []
    list2 = copy.deepcopy(list)
    while len(list)>1:
        element=list[0]
        group=[]
        group.append(copy.deepcopy(element))
        list2.remove(element)
        index=0
        while len(list2)>=1:
            element2=list2[index]
            if element[-2:] == element2[-2:] and element != element2:
                group.append(copy.deepcopy(element2))
                list.remove(element2)
                list2.remove(element2)
            else:
                index=index+1
            if(index == len(list2)):
                break
        list.remove(element)
        arr.append(group)
    if len(list) != 0:
        for element in list:
            arr.append([copy.deepcopy(element)])
    return arr

print(group_by_rhyme(['ana','carte','arme','palme','dame','parte','tarte','banana','marte']))