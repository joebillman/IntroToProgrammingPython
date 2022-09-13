# This program shows examples of variables and functions.
import math


greeting = "Hello World!" #string
age = 42 #integer
height = 6.1 #float
isOld = True #boolean

def print_my_greeting():
    print(greeting+" I'm "+str(age)+" years old")
    print("I'm "+str(height)+" tall")
    print("I'm old: "+str(isOld))
    if num1 > num2:
        print("num1 is greater than num2")
    else:
        print("num1 is NOT greater than num2")

num1 = 2
num2 = 10

#if num1 > num2:
    #print("num1 is greater than num2")
#else:
    #print("num1 is NOT greater than num2")

originalValue = 3.7
roundedValue = math.ceil(originalValue)
print("original value: "+str(originalValue))
print("rounded value: "+str(roundedValue))

#print("round up: "+str(math.ceil(3.7)))

#print_my_greeting()
#print_my_greeting()

backWheel = "something"
frontWheel = "something else"

def peddle():
    #Do something to variables
    #Move something on the screen



"""
function peddle() {
    document.getElementById("myHeading");
}

<html>
    <header id="myHeading">Hello World</header>
    <p>This is a paragraph</p>
</html>
"""




















firstName = "joe"
lastName = "billman"

print("hi "+str(firstName))

print("welcome to our class "+str(firstName)+" "+str(lastName))

greeting = "welcome to our class "+str(firstName)+" "+str(lastName)
