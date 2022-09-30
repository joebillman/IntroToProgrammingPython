from tkinter import *

root = Tk()
root.title("My GUI Window")
root.geometry('800x600')

frame = Frame(root, bg="blue", padx=10, pady=10, width=800, height=600)
frame.grid(row=0, sticky="ew")

label = Label(frame, text="Hello World", font=("Arial", 25))
label.grid(row=1)
#label.place(x=400, y=300, anchor="center")

button = Button(frame, text="Exit", command=root.destroy)
button.grid(row=2)

root.mainloop()
