from tkinter import *

root = Tk()
root.title("Calculator")
#root.geometry('800x600')

curMathOperator = ""
curNumberValue = 0
lastNumberCaptured = False
mathDone = False

frame = Frame(root, bg="gray", padx=10, pady=10)
frame.pack(side=LEFT)

label = Label(frame, text=str(curNumberValue), justify=RIGHT, font=("Arial", 25), width=14, bd=2, relief="sunken", anchor="e")
label.grid(row=0, column=0, columnspan=4, pady=6)
#label.place(x=400, y=300, anchor="center")

def clear():
    global curMathOperator
    global curNumberValue
    global lastNumberCaptured
    curMathOperator = ""
    curNumberValue = 0
    lastNumberCaptured = False
    label.config(text = "0")

def doMath():
    global mathDone
    mathDone = True
    hasFloat = False
    strValue = label.cget("text")
    if strValue.find(".") > -1:
        curValue = round(float(strValue), 2)
        hasFloat = True
    else:
        curValue = int(strValue)

    global curMathOperator
    global curNumberValue
    newValue = 0
    if curMathOperator == "/":
        newValue = curNumberValue / curValue
    elif curMathOperator == "X":
        newValue = curNumberValue * curValue
    elif curMathOperator == "-":
        newValue = curNumberValue - curValue
    elif curMathOperator == "+":
        newValue = curNumberValue + curValue
    if hasFloat:
        return round(newValue, 2)
    else:
        return newValue

def handleMathOperatorClick(value):
    global curMathOperator
    global curNumberValue
    global lastNumberCaptured
    if curMathOperator != "":
        curNumberValue = doMath()
        label.config(text=str(curNumberValue))
    lastNumberCaptured = False
    curMathOperator = value

def handleNumberClick(value):
    global curMathOperator
    global curNumberValue
    global lastNumberCaptured
    global mathDone
    curValue = label.cget("text")
    if curValue.find(".") > -1 and value == ".":
        return
    mathDone = False
    if curMathOperator != "" and lastNumberCaptured == False and value != ".":
        strValue = label.cget("text")
        if strValue.find(".") > -1:
            curNumberValue = round(float(strValue), 2)
        else:
            curNumberValue = int(strValue)
        label.config(text=value)
        lastNumberCaptured = True
        return
    if curValue == "0":
        label.config(text = value)
    else:
        label.config(text = curValue+value)

def equals():
    global curMathOperator
    global curNumberValue
    global mathDone
    if mathDone == True:
        return
    if curMathOperator != "":
        curNumberValue = doMath()
        curMathOperator = ""
    label.config(text = str(curNumberValue))

button1 = Button(frame, text="AC", width=8, height=2, cursor="hand2", command=clear)
button1.grid(row=1, column=0, padx=2, pady=2)
button2 = Button(frame, text="C", width=8, height=2, cursor="hand2", command=clear)
button2.grid(row=1, column=1, padx=2, pady=2)
button3 = Button(frame, text="X", width=8, height=2, cursor="hand2", command=lambda:handleMathOperatorClick("X"))
button3.grid(row=1, column=2, padx=2, pady=2)
button4 = Button(frame, text="/", width=8, height=2, cursor="hand2", command=lambda:handleMathOperatorClick("/"))
button4.grid(row=1, column=3, padx=2, pady=2)
button5 = Button(frame, text="7", width=8, height=2, cursor="hand2", command=lambda:handleNumberClick("7"))
button5.grid(row=2, column=0, padx=2, pady=2)
button6 = Button(frame, text="8", width=8, height=2, cursor="hand2", command=lambda:handleNumberClick("8"))
button6.grid(row=2, column=1, padx=2, pady=2)
button7 = Button(frame, text="9", width=8, height=2, cursor="hand2", command=lambda:handleNumberClick("9"))
button7.grid(row=2, column=2, padx=2, pady=2)
button8 = Button(frame, text="+", width=8, height=2, cursor="hand2", command=lambda:handleMathOperatorClick("+"))
button8.grid(row=2, column=3, padx=2, pady=2)
button9 = Button(frame, text="4", width=8, height=2, cursor="hand2", command=lambda:handleNumberClick("4"))
button9.grid(row=3, column=0, padx=2, pady=2)
button10 = Button(frame, text="5", width=8, height=2, cursor="hand2", command=lambda:handleNumberClick("5"))
button10.grid(row=3, column=1, padx=2, pady=2)
button11 = Button(frame, text="6", width=8, height=2, cursor="hand2", command=lambda:handleNumberClick("6"))
button11.grid(row=3, column=2, padx=2, pady=2)
button12 = Button(frame, text="-", width=8, height=2, cursor="hand2", command=lambda:handleMathOperatorClick("-"))
button12.grid(row=3, column=3, padx=2, pady=2)
button13 = Button(frame, text="1", width=8, height=2, cursor="hand2", command=lambda:handleNumberClick("1"))
button13.grid(row=4, column=0, padx=2, pady=2)
button14 = Button(frame, text="2", width=8, height=2, cursor="hand2", command=lambda:handleNumberClick("2"))
button14.grid(row=4, column=1, padx=2, pady=2)
button15 = Button(frame, text="3", width=8, height=2, cursor="hand2", command=lambda:handleNumberClick("3"))
button15.grid(row=4, column=2, padx=2, pady=2)
button16 = Button(frame, text="=", bg="orange", width=8, height=5, cursor="hand2", command=equals)
button16.grid(row=4, column=3, rowspan=2, padx=2, pady=2)
button17 = Button(frame, text=".", width=8, height=2, cursor="hand2", command=lambda:handleNumberClick("."))
button17.grid(row=5, column=0, padx=2, pady=4)
button18 = Button(frame, text="0", width=18, height=2, cursor="hand2", command=lambda:handleNumberClick("0"))
button18.grid(row=5, column=1, columnspan=2, padx=2, pady=4)

root.mainloop()
