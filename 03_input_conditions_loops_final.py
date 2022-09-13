# This program shows examples of the input function, conditional statements, and loops.

#input function
print("What is your name?")
name = input()
print("Hello, "+name)

#conditional statements
num1 = 33
num2 = 33
if num2 > num1:
  print("b is greater than a")
elif num1 == num2:
  print("a and b are equal")

#loops
fruits = ["apple", "banana", "cherry"]
for curFruit in fruits:
  print(curFruit)