from tkinter import *

a=1
def oval_func(event):
    global a
    if a==1:
        cv.create_oval(30,10,100,80,fill='red')
        a=-1
    else:
        cv.create_oval(30,10,100,80,fill='grey')
        a=1
cv = Canvas(width=150,height=100,bg='grey80')
cv.create_oval(30,10,100,80,fill='grey')
cv.pack(side=LEFT)

but=Button()
but['text'] ='Выключатель'
but.pack(side=LEFT)

but.bind('<Button-1>',oval_func)
mainloop()