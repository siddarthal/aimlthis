# string =input("enter a string : ")   

# def returnDictonary(string):
#     spacecnt=len(string.strip().split(" "))-1
#     print(spacecnt)
#     countVowels = 0
#     for ch in string:
#         if ch.lower() =="a" or ch.lower() =="e" or ch.lower() =="i" or ch.lower() =="o" or ch.lower() =="u":
#             countVowels+=1
#     countConsonants = len(string)-countVowels-spacecnt
#     return {"consonants":countConsonants,"vowels":countVowels}

# print(returnDictonary(string))


# string = input("Enter a string: ")
# listA = string.split(" ")
# setA = set()
# for item in listA:
#     setA.add(item.lower())
# print(list(setA))





def countTypeWords(string):
    countCapitals=0
    countSpace=len(string.split(" "))-1
    for item in string:
        if item.isupper():
            countCapitals+=1
    return {"uc":countCapitals,"lc":len(string)-countCapitals-countSpace}
string = input("Enter a string: ")
print(countTypeWords(string.strip(" ")))


# def capitalS(string):
#     listA =list()
#     for item in string:
#         if item.isupper():
#             listA.append(item)
#     return tuple(listA)
# string = input("Enter a string: ")
# print(capitalS(string.strip(" ")))


# def isPalindrome(string):
#       return string == string[::-1]  


# def palindromeList(list):
#     ansList=[]
#     for item in list:
#         if isPalindrome(item):
#             ansList.append(item)
#     return ansList

# list = ["php","121","css", "madam", "java", "1331"]

# print(palindromeList(list))