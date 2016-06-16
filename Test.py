My first Python program

"""
Created on Monday, April 25, 2016 in Scottsdale
"""

"""
print ("1. hello world")
print ("2. execute this file from Python shell by saying > exec(open(first.py).read())")      

def hello():
    print("3. my first Python function called Hello")

hello()

myvar="4. passing a variable to a function"
def hello2 (myvar):
    print (myvar)
hello2(myvar)


def mularg(ArgNo, *VarArgs):
    print ("The number of arguments passed is ", ArgNo, ".")
    for test in VarArgs:
        print (test)

mularg (4, "One", "2", "3 +4", "five")

def mularg(*VarArgs):
    print ("The number of arguments passed is ", *VarArgs, ".")
    for test in VarArgs:
        print (test)

mularg ("One", "2", "3 +4", "five")


def AddArg(arg1, arg2, arg3):   
    print ("inputs were ", arg1, arg2, arg3) 
    # print ("and output is ",AddArg(arg1, arg2, arg3))#- went into infinite loop! Ha ha
    return (arg1 + arg2 + arg3) 
    print ("End") #never executed as the function already returned

AddArg (2,2,2)
print ("Output is", AddArg(2,2,2))


Name = input ("What is your name? ")
Age = float (input ("Now tell me your age: ")) #changed from int to float
if Age == 52 and Name == "S":
    print ("Hello", Name,"!", "You will be" , int(Age+1), "next year")
else:
    print ("You are young")

var  = 1
for letter in "Good Morning":
    print ("Letter ", var, " is ", letter)
    var += 1

value = input("Type a string no longer than 6 character: ")
var  = 1
for letter in value:
    print ("Letter ", var, " is ", letter)
    var +=1
#else :
    #print ("You didnt enter any value, dingbat")
    if var  > 6:
        print ("The string is too long")
        break

var  = 1
for letter in "Good Morning":
    if letter == "o" :
        continue
        print (" Encountered o, not printed")
    print ("Letter ", var, " is ", letter)
    var += 1


try:
    Value = int(input("Type a number between 1 and 10:"))
except ValueError:
    print ("You must type a number between 1 and 10")
else:
    if (Value > 0) and (Value <=10):
        print ("You typed ", Value)
    else:
        print ("The value is incorrect")

try:
    Value = int(input("Type a number between 1 and 10:"))
except KeyboardInterrupt:
    print ("Did you really have to press Control-C?")
except ValueError:
    print ("You must type a number between 1 and 10")
else:
    if (Value > 0) and (Value <=10):
        print ("You typed ", Value)
    else:
        print ("The value is incorrect")
        


import sys

try:
    File = open('myfile.txt')
except IOError as e:
    print ("Error opening file ! \r\n" +
           "Error Number: {0}\r\n".format(e.errno) +
           "Error Text: {0}".format(e.strerror))
else :
    print ("File opened as expected")
    File.close();
    
            
import sys

try:
    File = open('myfile.txt')
except IOError as e:
    for Arg in e.args:
        print (Arg)
"""

TryAgain = True
while TryAgain:
    try:
        Value1 = int(input("Type a number between 1 and 10:"))
        Value2 = int(input("Type a number between 1 and 10:"))
        Output1 = Value1 / Value2
        Output2 = Value1 // Value2
    except (ValueError, KeyboardInterrupt):
        print ("You must type a number between 1 and 10")
        TryAgain = False #Till I added this line, I couldnt kill the program!
    except ZeroDivisionError:
        print (" Tut, tut! Can't divide by zero")
    else:
        print ("Floating Point Output is " , Output1)
        print ("Using the floor division operator " , Output2)















