import tkinter as tk 
from tkinter import ttk
win = tk.Tk()
win.title("PYthon Gui")
ttk.Label(win,text="A label").grid(row=0,column=0)
win.resizable(50,7)
win.mainloop()