
while True:
    var = input("Enter any input: ")
    if var:
        break

string ="Monty Python's Flying Circus"
list = string.split()
for word in list:
    print(word +" = "+ str(len(word)))


def patternOne(number):
    for i in range(1,number+1):
        for j in range(1,i+1):
            print(j,end="")
        print(end="\n")         

def patternTwo(number):
    for i in range(1,number+1):
        for j in range(1,i+1):
            print(i,end="")
        print(end="\n")
    print(end="\n")      
while True:
    number = int(input("Enter a number: "))
    if number >0 and number < 10:
        patternTwo(number)
        patternOne(number)
        break
    else:
        print("Please enter a number between 1 and 9")


def divsibleBySevenAndFive(start,end):
    for i in range(start,end):
        if i%7==0 and i%5==0:
            print(i,end=" ")
    print(end="\n")

divsibleBySevenAndFive(1500,2701)

string =input("enter a string to be reversed: ")
print(string[::-1] ,"is the reverse of ",string)      


def printNum():
    for i in range(0,7):
        if i==3 or i==6:
            continue
        print(i,end=" ")

printNum()

def validatePhoneNumber():
    number = input("Enter a phone number: ")
    if len(number) == 10 and number.isdigit():
        if(number.startswith("6") or number.startswith("7") or number.startswith("8") or number.startswith("9")):
            print("Valid phone number")
    else:
        print("Invalid phone number")
validatePhoneNumber()
 

while True:
    string1=input("enter first string: ")
    string2=input("enter two string: ")
    if string1 and string2:
        print(string1+" "+string2)
        break
    else:
        print("Please enter a valid string")

while True:
    number =int(input("Enter a number: "))
    if number >1 and number < 500:
        break
    else:
        print("Please enter a number between 1 and 500")





string =input("Enter a string: ")
ans=""
for ch in string:
    if ch=="a" or ch=="A" or ch=="e" or ch=="E" or ch=="i" or ch=="I" or ch=="o" or ch=="O" or ch=="u" or ch=="U":
        continue
    else:
        ans+=ch
print(ans)
