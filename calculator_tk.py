from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
root = Tk()
root.geometry("644x900")
root.title("Calculator by Harshith")
# root.wm_iconbitmap("1.ico")


scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

# create frame 1
f = Frame(root, bg="grey")
b = Button(f, text="9",padx=31, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="8", padx=31, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="7",padx=31,pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)
f.pack()

# create frame 2
f = Frame(root, bg="grey")
b = Button(f, text="6", padx=31, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="5", padx=31, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="4", padx=31, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)
f.pack()

# create frame 3
f = Frame(root, bg="grey")
b = Button(f, text="3", padx=31, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="2", padx=31, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="1", padx=31, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)
f.pack()

# create frame 4
f = Frame(root, bg="grey")
b = Button(f, text="0", padx=31, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="-", padx=31, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="*", padx=31, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)
f.pack()

# create frame 5
f = Frame(root, bg="grey")
b = Button(f, text="/", padx=30, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="%", padx=30,pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="=", padx=30, pady=18, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)
f.pack()

# create frame 6
f = Frame(root, bg="grey")
b = Button(f, text="c", padx=31,pady=18, font="lucida 35 bold")
b.pack(side=BOTTOM, padx=18, pady=5)
b.bind("<Button-1>", click)
# b = Button(f, text="-", padx=31,pady=18, font="lucida 35 bold")
# b.pack(side=LEFT, padx=18, pady=5)
# b.bind("<Button-1>", click)
# b = Button(f, text="*", padx=31,pady=18, font="lucida 35 bold")
# b.pack(side=LEFT, padx=18, pady=5)
# b.bind("<Button-1>",click)
f.pack()

root.mainloop()
