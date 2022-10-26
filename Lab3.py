import copy

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
        dictionary[char] = dictionary[char] + 1 if char in dictionary else 1
    return dictionary

# print(phraseDict('Ana has apples.'))

#Ex 3
def listComparison(a,b):
    if len(a) != len(b):
        return False
    else:
       for index in range(0,len(a)):
        if a[index]!=b[index]:
            return False
       return True

def setComparison(a,b):
    if a.difference(b) == set() and b.difference(a) == set():
        return True
    return False

def dictComparison(a,b):
    newDict=dict()
    for x in a:
        if x in b:
            if type(a[x]) == type(b[x]):
                if type(a[x]) is dict:
                    if not dictComparison(a[x],b[x]):
                        return False
                if type(a[x]) is list:
                    if not listComparison(a[x],b[x]):
                        return False
                if type(a[x]) is set:
                    if not setComparison(a[x],b[x]):
                        return False
                if type(a[x]) is str:
                    if a[x] != b[x]:
                        return False
                if type(a[x]) is int:
                    if a[x]-b[x]!=0:
                        return False
    for x in b:
        if x not in a:
            return False
    return True

# print(dictComparison({"A":3,"B":{"C":"3"}},{"A":3,"B":{"C":"3"}}))

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
            dictionary[f"{sets[index]} | {sets[index2]}"] = reunion
            dictionary[f"{sets[index]} & {sets[index2]}"] = intersection
            dictionary[f"{sets[index]} - {sets[index2]}"] = difference1
            dictionary[f"{sets[index2]} - {sets[index]}"] = difference2
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
def posKeyArgs(*num,**data):
    count=0
    dictionary = {}
    for key, value in data.items():
        dictionary[key] = value
    for number in num:
        for key in dictionary:
            count = count + 1 if dictionary[key]==number else count
    return count

# print(posKeyArgs(1,2,3,4,x=1,y=2,z=3,w=5))