
#    elif value=="delete character":
#        equation=(equation[0:len(equation)-1])
#Delete_character=Button(text="delete character",width=20,bg="yellow")
#Delete_character.grid(row=7,column=1)

from tkinter import *
root= Tk()
root.geometry("600x200")
root.title("Avi's calculator")
root.config(bg="yellow")
equation=StringVar()
start_new=False
def calculator(event):
    global start_new
    value=event.widget.cget("text")
    if value=="=":
        equation.set(eval(equation.get()))
        start_new=True
    elif value=="delete character":
        strequation=equation.get()
        equation.set(strequation[0:len(strequation)-1])
    else:
        if start_new:
            equation.set("")
            start_new=False
        equation.set(equation.get()+value)

entry=Entry(textvariable=equation,width=20,bg="yellow")
entry.grid(row=0,column=1,columnspan=4)

seven=Button(text="7",width=20,bg="yellow")
seven.grid(row=3,column=1)
seven.bind("<Button-1>",calculator)

eight=Button(text="8",width=20,bg="yellow")
eight.grid(row=3,column=2)
eight.bind("<Button-1>",calculator)
nine=Button(text="9",width=20,bg="yellow")
nine.grid(row=3,column=3)
nine.bind("<Button-1>",calculator)
divide=Button(text="/",width=20,bg="yellow")
divide.grid(row=3,column=4)
divide.bind("<Button-1>",calculator)
four=Button(text="4",width=20,bg="yellow")
four.grid(row=4,column=1)
four.bind("<Button-1>",calculator)
five=Button(text="5",width=20,bg="yellow")
five.grid(row=4,column=2)
five.bind("<Button-1>",calculator)
six=Button(text="6",width=20,bg="yellow")
six.grid(row=4,column=3)
six.bind("<Button-1>",calculator)
multiply=Button(text="*",width=20,bg="yellow")
multiply.grid(row=4,column=4)
multiply.bind("<Button-1>",calculator)
one=Button(text="1",width=20,bg="yellow")
one.grid(row=5,column=1)
one.bind("<Button-1>",calculator)
two=Button(text="2",width=20,bg="yellow")
two.grid(row=5,column=2)
two.bind("<Button-1>",calculator)
three=Button(text="3",width=20,bg="yellow")
three.grid(row=5,column=3)
three.bind("<Button-1>",calculator)
subtract=Button(text="-",width=20,bg="yellow")
subtract.grid(row=5,column=4)
subtract.bind("<Button-1>",calculator)
zero=Button(text="0",width=20,bg="yellow")
zero.grid(row=6,column=1)
zero.bind("<Button-1>",calculator)
answer=Button(text="=",width=20,bg="yellow")
answer.grid(row=6,column=2)
answer.bind("<Button-1>",calculator)
dot=Button(text=".",width=20,bg="yellow")
dot.grid(row=6,column=3)
dot.bind("<Button-1>",calculator)
addition=Button(text="+",width=20,bg="yellow")
addition.grid(row=6,column=4)
addition.bind("<Button-1>",calculator)
Delete_character=Button(text="delete character",width=20,bg="yellow")
Delete_character.grid(row=7,column=1)
Delete_character.bind("<Button-1>",calculator)
root.mainloop()