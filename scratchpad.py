
#print("What is your name?")
#name = input()
#print("Hello "+name)
#print("What city do you live in?")
#city = input()
#print("I bet the weather is nice in "+city)
#print("How old are you?")
#age = int(input())

#if age >= 40 and age < 50:
    #print("Man, middle age is great!")
#elif age >= 50:
    #print("That's old dude!")
#else:
    #print("Sure is good to be young!")

from re import T


print("What fruit do you want to find?")
fruitToFind = input()
index = 0
fruitFound = False
fruits = ["apple", "orange", "banana", "pineapple", "kiwi"]

for curFruit in fruits:
    if curFruit == fruitToFind:
        fruitFound = True
        break
    #print(curFruit)
    #print(index)
    else:
        fruitFound = False
    index = index + 1

if fruitFound == True:
    print("The "+fruitToFind+" was found at index: "+str(index))
else: 
    print("The "+fruitToFind+" was NOT found!")
    
#print(fruits[0])
