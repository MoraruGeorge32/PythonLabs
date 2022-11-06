from utils import process_item
#Ex 1
def primeOrNot():
    number=input("Please enter a number (q to want to quit): ")
    while number != 'q':
        if number == 'q':
            exit(0)
        else:
            process_item(int(number))
            number=input("Please enter a number (q to want to quit): ")

# primeOrNot()

#Ex 2
def keySum(**args):
    sum = 0
    for number in args.items():
        sum = sum + number[1]
    return sum

sumArgs = lambda **args: sum(args.values())

# print(keySum(a=1,b=2))
# print(sumArgs(a=1,b=2))

#Ex 3
def vowels(sentence):
    vowelList = []
    for character in sentence:
        if character in ['a','e','i','o','u']:
            vowelList.append(character)
    return vowelList

vowel = lambda stringList: [x for x in stringList if x in ['a','e','i','o','u']]

def vowelCheck(letter):
    vowels = ['a','e','i','o','u']
    return True if letter in vowels else False

def vowelFilter(sequence):
    vowels = list(filter(vowelCheck,sequence))
    return vowels

# print(vowels('Programming in Python is fun'))
# print(vowel('Programming in Python is fun'))
# print(vowelFilter('Programming in Python is fun'))

#Ex 4
def dictCheck(dictionary):
    if type(dictionary) is dict:
        if len(dictionary.keys()) >= 2:
            for key in dictionary.keys():
                if type(key) is str:
                    if len(key)>2:
                        return True
    return False

def checkArguments(*arg, **args):
    dictionaries = list(filter(dictCheck,list(arg)))
    dictionaries.extend(list(filter(dictCheck,list(args.values()))))
    return dictionaries

# print(checkArguments({1:2,3:4,5:6},{'a':5,'b':7,'c':'e'},{2:3},[1,2,3],{'abc':4,'def':5},3764,dictionar={'ab':4,'ac':'abcde','fg':'abc'},test={1:1,'test':True}))

#Ex 5
def checkNumber(number):
    return True if type(number) is int or type(number) is float else False

def filterList(elList):
    array = list(filter(checkNumber,elList))
    return array

# print(filterList([1,"2",{"3": "a"},{4,5},5,6,3.0]))

#Ex 6
def positionTuples(numberList):
    evens = [x for x in numberList if x%2==0]
    odds = [x for x in numberList if x%2==1]
    tupleList=[]
    for index in range(0,len(odds)):
        tupleList.append((evens[index],odds[index]))
    return tupleList

# print(positionTuples([1,3,5,2,8,7,4,10,9,2]))

#Ex 7
def sum_digits(x):
    return sum(map(int,str(x)))

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

def process(**args):
    fibonacciNumbers = nFibo(50)
    limitNumber = 0
    offsetNumber = 0
    for argument in args.items():
        if argument[0] == 'filters':
            for function in argument[1]:
                fibonacciNumbers = list(filter(function,fibonacciNumbers))
        elif argument[0] == 'offset':
            offsetNumber = argument[1]
        elif argument[0] == 'limit':
            limitNumber = argument[1]
    fibonacciNumbers = fibonacciNumbers[offsetNumber:]
    fibonacciNumbers = fibonacciNumbers[:limitNumber]
    return fibonacciNumbers

# print(process(filters=[lambda item: item%2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20], limit = 2, offset = 2))

#Ex 8
def multiply_by_two(x):
    return x*2

def add_numbers(a,b):
    return a+b

def print_arguments(function):
    def printArgs(*arg,**args):
        return f'Arguments are: {arg}, {args} and will return {function(*arg,**args)}'
    return printArgs


# augmented_multiply_by_two = print_arguments(multiply_by_two)
# x = augmented_multiply_by_two(10)
# print(x)
    
# augmented_add_numbers = print_arguments(add_numbers)
# x = augmented_add_numbers(3,4)
# print(x)

#Ex 8 b.
def multiply_by_three(x):
    return x*3

def multiply_output(function):
    def executeFunction(*arg,**args):
        return 2*function(*arg,**args)
    return executeFunction

# augmented_multiply_by_three = multiply_output(multiply_by_three)
# x = augmented_multiply_by_three(10)
# print(x)

#Ex 8 c.
def augment_function(function, decorators):
    def executeDecorators(*arg,**args):
        value = function
        index = 0
        while(index<len(decorators)):
            decorator = decorators[len(decorators)-index-1]
            value = decorator(value)
            index = index+1
        return value(*arg,**args)
    return executeDecorators

# decorated_function = augment_function(add_numbers,[print_arguments,multiply_output])
# x=decorated_function(3,4)
# print(x)

#Ex 9
def f9(pairs=[]):
    arrayOfDict = []
    for tuples in pairs:
        dictionary = {}
        dictionary['sum'] = tuples[0] + tuples[1]
        dictionary['prod'] = tuples[0] * tuples[1]
        dictionary['pow'] = tuples[0] ** tuples[1]
        arrayOfDict.append(dictionary)
    return arrayOfDict

print(f9([(5,2),(19,1),(30,6),(2,2)]))


