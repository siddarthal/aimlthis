# Question 1

string =input("enter a string : ")   

def returnDictonary(string):
    spacecnt=len(string.strip().split(" "))-1
    print(spacecnt)
    countVowels = 0
    for ch in string:
        if ch.lower() =="a" or ch.lower() =="e" or ch.lower() =="i" or ch.lower() =="o" or ch.lower() =="u":
            countVowels+=1
    countConsonants = len(string)-countVowels-spacecnt
    return {"consonants":countConsonants,"vowels":countVowels}

print(returnDictonary(string))

# Question 2
string = input("Enter a string: ")
listA = string.split(" ")
setA = set()
for item in listA:
    setA.add(item.lower())
print(list(setA))



# Question 3

def countTypeWords(string):
    countCapitals=0
    countSpace=len(string.split(" "))-1
    for item in string:
        if item.isupper():
            countCapitals+=1
    return {"uc":countCapitals,"lc":len(string)-countCapitals-countSpace}
string = input("Enter a string: ")
print(countTypeWords(string.strip(" ")))


# Question 4
def capitalS(string):
    listA =list()
    for item in string:
        if item.isupper():
            listA.append(item)
    return tuple(listA)
string = input("Enter a string: ")
print(capitalS(string.strip(" ")))



# Question 5

def isPalindrome(string):
      return string == string[::-1]  


def palindromeList(list):
    ansList=[]
    for item in list:
        if isPalindrome(item):
            ansList.append(item)
    return ansList

list = ["php","121","css", "madam", "java", "1331"]

print(palindromeList(list))

# Implementing Stack question 6

class Stack:
    listStack = list()
    top=0
    def __init__(self):
        self.top=-1
    
    def pop(self):
        if self.top==-1:
            print("stack is empty")
        else:
            print("pop",self.listStack[self.top])
            self.top-=1
    
    def push(self,element):
        self.listStack.insert(self.top+1,element)
        self.top+=1
        print("pushed",self.listStack[self.top])

print("enter total number operations")
n = int(input())
stack =Stack()
print("for push enter push and element with space for pop enter pop")

for i in range(0,n):
    print("enter operation ")
    entry =input()
    listEntries=entry.strip(" ").split(" ")
    if(len(listEntries)==2):
        stack.push(int(listEntries[1]))
    else:
        stack.pop()


# Implementing Queue question 7

class Queue:
    ListQueue =list()
    left=0
    right=0
    def enqueue(self,element):
        self.ListQueue.insert(self.right,element)
        self.right+=1
    def dequeue(self):
        if self.left == self.right:
            print("Queue is empty")
        else:
            print("dequeued",self.ListQueue[self.left])
            self.left+=1
print("enter total number operations")
n = int(input())
queue=Queue()
print("for enqueue enter  and element with space for dequeue enter dequeue")

for i in range(0,n):
    print("enter operation ")
    entry =input()
    listEntries=entry.strip(" ").split(" ")
    if(len(listEntries)==2):
        queue.enqueue(int(listEntries[1]))
    else:
        queue.dequeue()


# Question 8
string = input("Enter a string: ")

def countOccurences(string):
    dictA = dict()
    for item in string:
        if item in dictA:
            dictA[item]+=1
        else:
            dictA[item]=1
    return dictA
print(countOccurences(string))


# Question 9

string = input("Enter a string: ")
listA = string.split()
def countOccurencesWord(listA):
    dictA = dict()
    for item in listA:
        if item in dictA:
            dictA[item]+=1
        else:
            dictA[item]=1
    return dictA
print(countOccurencesWord(listA))


# Question 10
string = input("Enter a string: ")
def countOccurencesMax(string):
    dictA = dict()
    maxKey=""
    maxVal=0
    for item in string:
        if item in dictA:
            dictA[item]+=1
            if(maxVal<dictA[item]):
                maxVal=dictA[item]
                maxKey=item
        else:
            dictA[item]=1
    return [maxKey,maxVal]
listA=countOccurencesMax(string)
print("character '"+ listA[0] +"' with '"+ str(listA[1])+"' occurrences")


