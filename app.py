import tkinter as tk
import time
numbr = (5)
ass = input("How frequently do you want to be asked to drink water the (default is 5 hours (you are limited to hours and stick to just numbers NO letters))")
if ass != " ":
    numbr = ass
if ass == " ":
     numbr = numbr
print(numbr)
root = tk.Tk()
root.title("have you hydrated?")
root.minsize(300, 100)
root.maxsize(300, 100)
root.configure(background="gray")
tk.Label(root, text="have you drunk water in the past hours").pack()
root.mainloop()
