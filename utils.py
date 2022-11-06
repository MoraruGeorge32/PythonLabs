import copy
import math

#Ex 1
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

def process_item(number):
    numb = copy.deepcopy(number)
    while not checkPrim(numb):
        numb = numb + 1
    print(f'The least prime number greater than {number} is {numb}!')