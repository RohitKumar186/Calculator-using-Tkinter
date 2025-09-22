from tkinter import *

from fontTools.cffLib import buildOrder

window = Tk()
window.geometry("500x500")
window.title("Calculator")

e=Entry(window,width=60,borderwidth=10,justify=CENTER)
e.place(x=50,y=50)
def click(num):
    result =e.get()
    e.delete(0, END)
    e.insert(0,str(result)+str(num))

def clear():
    e.delete(0,END)

b1=Button(window,text="AC",width=10,height=3,command=clear)
b1.place(x=50,y=100)

def backspace():
    current = e.get()
    e.delete(0, END)
    e.insert(0, current[:-1])

b2=Button(window,text="<x",width=10,height=3, command=backspace)
b2.place(x=50,y=150)
b2.place(x=150,y=100)

def toggle_sign():
    current = e.get()
    if current.startswith("-"):
        e.delete(0, END)
        e.insert(0, current[1:])
    elif current != "":
        e.delete(0, END)
        e.insert(0, "-" + current)

b3=Button(window,text="+/-",width=10,height=3,command=toggle_sign)
b3.place(x=250,y=100)

def div():
    n1=e.get()
    global math
    math="division"
    global i
    i=float(n1)
    e.delete(0,END)
b5=Button(window,text="/",width=10,height=3,command=div)
b5.place(x=350,y=100)
b6=Button(window,text="7",width=10,height=3,command=lambda:click(7))
b6.place(x=50,y=180)
b7=Button(window,text="8",width=10,height=3,command=lambda:click(8))
b7.place(x=150,y=180)
b8=Button(window,text="9",width=10,height=3,command=lambda:click(9))
b8.place(x=250,y=180)

def mul():
    n1=e.get()
    global math
    math="multiplication"
    global i
    i=float(n1)
    e.delete(0,END)
b9=Button(window,text="x",width=10,height=3,command=mul)
b9.place(x=350,y=180)
b10=Button(window,text="4",width=10,height=3,command=lambda:click(4))
b10.place(x=50,y=260)
b11=Button(window,text="5",width=10,height=3,command=lambda:click(5))
b11.place(x=150,y=260)
b12=Button(window,text="6",width=10,height=3,command=lambda:click(6))
b12.place(x=250,y=260)

def sub():
    n1=e.get()
    global math
    math="subtraction"
    global i
    i=float(n1)
    e.delete(0,END)
b13=Button(window,text="-",width=10,height=3,command=sub)
b13.place(x=350,y=260)
b14=Button(window,text="1",width=10,height=3,command=lambda:click(1))
b14.place(x=50,y=340)
b15=Button(window,text="2",width=10,height=3,command=lambda:click(2))
b15.place(x=150,y=340)
b16=Button(window,text="3",width=10,height=3,command=lambda:click(3))
b16.place(x=250,y=340)

def add():
    n1=e.get()
    global math
    math="addition"
    global i
    i=float(n1)
    e.delete(0,END)
b17=Button(window,text="+",width=10,height=3,command=add)
b17.place(x=350,y=340)

def rem():
    n1=e.get()
    global math
    math="remainder"
    global i
    i=float(n1)
    e.delete(0,END)
b18=Button(window,text="%",width=10,height=3,command=rem)
b18.place(x=50,y=420)
b19=Button(window,text="0",width=10,height=3,command=lambda:click(0))
b19.place(x=150,y=420)
b20=Button(window,text=".",width=10,height=3,command=lambda:click("."))
b20.place(x=250,y=420)

def equal():
    n2=e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0,i+float(n2))
    elif math=="subtraction":
        e.insert(0,i-float(n2))
    elif math=="multiplication":
        e.insert(0,i*float(n2))
    elif math=="division":
        e.insert(0,i/float(n2))
    elif math == "remainder":
        e.insert(0, int(i) % int(float(n2)))


b21=Button(window,text="=",width=10,height=3,command=equal)
b21.place(x=350,y=420)
mainloop()
