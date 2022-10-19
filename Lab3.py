from calendar import different_locale
import copy

from Lab2 import intersection, reunion

#Ex 1
def operations(a,b):
    x = set(a)
    y = set(b)
    arr = []
    arr.append(x.intersection(y))
    arr.append(x.union(y))
    arr.append(x.difference(y))
    arr.append(y.difference(x))
    return arr

# print(operations([1,2,3],[2,3,4]))

#Ex 2
def phraseDict(sentence):
    dictionary = dict()
    for char in sentence:
        if char in dictionary:
            dictionary[char] = dictionary[char]+1
        else:
            dictionary[char]=1
    return dictionary

# print(phraseDict('Ana has apples.'))

#Ex 3
def listComparison(a,b):
    if len(a) != len(b):
        return [a,b]
    else:
       for index in range(0,len(a)):
        if a[index]==b[index]:
            del a[index]
            del b[index]
       return [a,b]

def setComparison(a,b):
    if a.difference(b) == set() and b.difference(a) == set():
        return {}
    return {a,b}

def dictComparison(a,b):
    newDict=dict()
    for x in a:
        if x in b:
            if type(a[x]) == type(b[x]):
                if type(a[x]) is dict:
                    if type(dictComparison(a[x],b[x])) is dict:
                        newDict[x] = dictComparison(a[x],b[x]) 
                if type(a[x]) is list:
                    [first,last] = listComparison(a[x],b[x])
                    changes = first + last
                    if len(changes)>0:
                        newDict[x] = changes
                if type(a[x]) is set:
                    if setComparison(a[x],b[x]) != {}:
                        newDict[x] = [a[x],b[x]]
                if type(a[x]) is str:
                    if a[x] != b[x]:
                        newDict[x] = [a[x],b[x]]
                if type(a[x]) is int:
                   if a[x]-b[x]!=0:
                     newDict[x] = [a[x],b[x]]
        else:
            newDict[x] = a[x]
    for x in b:
        if x not in a:
            newDict[x] = b[x]
    if newDict == {}:
        return "They are equal!"
    else:
        return newDict

# print(dictComparison({"A":2,"B":{"C":"3"}},{"A":2,"B":{"C":"3"}}))

#Ex 4
def build_xml_element(tag,content,dictionary):
    name_parameters=""
    for x in dictionary:
        name_parameters=name_parameters+f' {x}="{dictionary[x]}"'
    return f"<{tag}{name_parameters}> {content} </{tag}>"

# print(build_xml_element("a","Hello there",{"href":"http://python.org","_class":"my_link","id":"someid"}))

#Ex 5
def check_suffix(sentence, suffix):
    if sentence[-len(suffix):] == suffix or len(suffix) == 0:
        return True
    return False

def check_prefix(sentence,prefix):
    if sentence[:len(prefix)] == prefix or len(prefix) == 0:
        return True
    return False

def check_middle(sentence, middle):
    if not check_prefix(sentence,middle) and not check_suffix(sentence,middle) and middle in sentence:
        return True
    return False

def validate_dict(dictionary, rules):
 rules=list(rules)
 keyRules=[]
 for rule in rules:
    keyRules.append(rule[0])
 for x in dictionary:
    if x not in keyRules:
        return False #the dictionary contains a key the rule set doesn't have
 for rule in rules:
    sentence = dictionary[rule[0]]
    if check_prefix(sentence,rule[1]) == False or check_middle(sentence,rule[2]) == False or check_suffix(sentence, rule[3]) == False:
        return False
 return True

# print(validate_dict({"key1":"come inside, it's too cold out", "key3": "this is not valid"},{("key1","","inside",""),("key2","start","middle", "winter")}))
# print(validate_dict({"key1":"come inside, it's too cold out", "key2": "this is not valid"},{("key1","come","inside",""),("key2","this","not","valid")}))

#Ex 6
def uniqueElements(numbers):
    setNumbers = set(copy.deepcopy(numbers))
    tupleReturned = [len(numbers),0]
    for x in numbers:
        if x in setNumbers:
            setNumbers.remove(x)
        else:
            tupleReturned[0] = tupleReturned[0]-1
            tupleReturned[1] = tupleReturned[1]+1
    tupleReturned = tuple(tupleReturned)
    return tupleReturned

# print(uniqueElements([1,1,2,3,4,5,5]))

#Ex 7
def operationsSet(sets):
    dictionary = dict()
    for index in range(0, len(sets)-1):
        for index2 in range(index+1,len(sets)):
            reunion=sets[index].union(sets[index2])
            intersection=sets[index].intersection(sets[index2])
            difference1=sets[index].difference(sets[index2])
            difference2=sets[index2].difference(sets[index])
            dictionary[f"{sets[index]} | {sets[index2]}"] = len(reunion)
            dictionary[f"{sets[index]} & {sets[index2]}"] = len(intersection)
            dictionary[f"{sets[index]} - {sets[index2]}"] = len(difference1)
            dictionary[f"{sets[index2]} - {sets[index]}"] = len(difference2)
    return dictionary

# print(operationsSet([{1,2},{2,3}]))
# print(operationsSet([{1,2},{2,3},{3,4}]))

#Ex 8
def mapping(dictionary):
    key='start'
    visited_keys=[]
    array=[]
    while key!=dictionary[key] and key not in visited_keys:
        if dictionary[key] not in visited_keys:
            array.append(dictionary[key])
        last_key = copy.deepcopy(key)
        key = dictionary[key]
        visited_keys.append(last_key)
    return array

# print(mapping({'start':'a', 'b':'a', 'a':'6', '6':'z', 'x': '2', 'z':'2', '2': '2', 'y':'start'}))

#Ex 9
def posKeyArgs(numbers,dictionary):
    count=0
    for x in numbers:
        for y in dictionary:
            if x == dictionary[y]:
                count=count+1
                break
    return count

# print(posKeyArgs([1,2,3,4],{'x':1,'y':2,'z':3,'w':5}))