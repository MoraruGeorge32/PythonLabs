import re

#Ex 1
def extractWords(text):
    words = re.findall("[\w]+",text)
    return words

# print(extractWords("A wolf is an animal who lives in mountain sides at almost 1200 meters above the base of the earth."))

#Ex 2
def longLengthRegex(regex,text,x):
    wordsLength = re.findall(regex+'{'+f"{x}"+'}',text)
    return wordsLength

# print(longLengthRegex("\w","Ana are argint",6))

#Ex 3
def listOfRegex(text,regexes):
    setOfWords = set()
    for regex in regexes:
        listOfWords = re.findall(regex,text)
        listOfWords = set(listOfWords)
        setOfWords = setOfWords.union(listOfWords)
    setOfWords = list(setOfWords)
    return setOfWords

# print(listOfRegex("Cameleon 1234 lup c123 432",["\d+","^[C][a-z]*"]))

#Ex 4
def checkAllAttributes(tag,attrs):
    listOfAttributes = re.findall('(\S+\=\"\S+")',tag)
    count = 0
    for attribute in listOfAttributes:
        key, value = attribute.split("=")
        if key in attrs.keys():
            if '"' + attrs[key] + '"' == value:
                count = count + 1
    if count == len(attrs):
        return True
    return False


def xmlDict(pathToXML,attrs):
    tags = []
    with open(pathToXML,'r') as f:
        for line in f.readlines():
            if checkAllAttributes(line,attrs):
                line = str.lstrip(line)
                line = str.rstrip(line,"\n")
                tags.append(str.lstrip(line))
    return tags

# print(xmlDict('./Example.xml',{"class":"url","name":"url-form","data-id":"item"}))


#Ex 5
def retrieveAttributesAsDictionary(tag,attrs):
    listOfAttributes = re.findall('(\S+\=\"\S+")',tag)
    for attribute in listOfAttributes:
        key, value = attribute.split("=")
        if key in attrs.keys():
            if '"' + attrs[key] + '"' == value:
                return True
    return False


def xmlDict1(pathToXML,attrs):
    tags = []
    with open(pathToXML,'r') as f:
        for line in f.readlines():
            if retrieveAttributesAsDictionary(line,attrs):
                tags.append(str.lstrip(line))
    return tags

# print(xmlDict1('./Example.xml',{"class":"url","name":"url-form","data-id":"item"}))


#Ex 6
def censor(word):
    for index in range(1,len(word)-1,2):
        word = word.replace(word[index],"*")
    return word

def censorWords(text):
    listOfWords = re.findall(r"(\b[aeiouAEIOU][a-zA-Z]*[aeiouAEIOU]\b)",text)
    listOfCensoredWords = list(map(lambda x: censor(x),listOfWords))
    return listOfCensoredWords

# print(censorWords("oaie alama ici acolo soarece imn cactus"))


#Ex 7
def validCNP(text):
    cnp = re.match("^[1-8][0-9]{2}(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])(0[1-9]|[1-3][0-9]|4[0-8]|5[12])(00[1-9]|(\d){3})[0-9]",text)
    if cnp is not None:
        print("CNP-ul este valid!")

# validCNP("5010222226794")