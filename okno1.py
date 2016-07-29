from tkinter import *

root = Tk()
lab = Label(root, text="Адрес:", font="Arial 18")
lab.pack()
ent = Entry(root,width=20,bd=3)
ent.pack()

lab = Label(root, text="Ваш комментарий:", font="Arial 18")
lab.pack()
ent = Entry(root,width=20,bd=3)
ent.pack()
#tex = Text(root,width=40,height=20,
#          font="Verdana 12",
#          wrap=WORD)
#tex.pack()

but = Button(root,
          text="Отправить", #надпись на кнопке
         width=30,height=5, #ширина и высота
       bg="white",fg="blue") #цвет фона и надписи

but.pack()

var=IntVar()
var.set(1)
rad0 = Radiobutton(root,text="0-10",
          variable=var,value=0)
rad1 = Radiobutton(root,text="11-20",
          variable=var,value=1)
rad2 = Radiobutton(root,text="21-30",
          variable=var,value=2)
rad3 = Radiobutton(root,text="31-40",
          variable=var,value=3)
rad0.pack()
rad1.pack()
rad2.pack()
rad3.pack()

c1 = IntVar()
c2 = IntVar()
c3 = IntVar()
c4 = IntVar()

che1=Checkbutton(root,text="Красный",
                         variable=c1, onvalue=1, offvalue=0,
                         bg="red",fg="black")
che2=Checkbutton(root,text="Зеленый",
                         variable=c2, onvalue=1, offvalue=0,
                         bg="green",fg="black")
che3=Checkbutton(root,text="Желтый",
                         variable=c3, onvalue=1, offvalue=0,
                         bg="yellow",fg="black")
che4=Checkbutton(root,text="Оранжевый",
                         variable=c4, onvalue=1, offvalue=0,
                         bg="orange",fg="black")
che1.pack()
che2.pack()
che3.pack()
che4.pack()


root.mainloop()
