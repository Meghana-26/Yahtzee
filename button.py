from tkinter import *
root = Tk()
root.title("YAHTZEE_GAME")
e = Entry(root,width=20,borderwidth=20)
e.grid(row=0,column=1,padx =20, pady =20)
e1 = Entry(root,width=20,borderwidth=20)
e1.grid(row=1,column=1,padx =10, pady =10)
e2 = Entry(root,width=20,borderwidth=20)
e2.grid(row=2,column=1,padx =10, pady =10)
e3 = Entry(root,width=20,borderwidth=20)
e3.grid(row=3,column=1,padx =10, pady =10)
e4 = Entry(root,width=20,borderwidth=20)
e4.grid(row=4,column=1,padx =10, pady =10)
e5 = Entry(root,width=20,borderwidth=20)
e5.grid(row=5,column=1,padx =10, pady =10)
e6 = Entry(root,width=20,borderwidth=20)
e6.grid(row=0,column=4,padx =10, pady =10)
e7 = Entry(root,width=20,borderwidth=20)
e7.grid(row=1,column=4,padx =10, pady =10)
e8 = Entry(root,width=20,borderwidth=20)
e8.grid(row=2,column=4,padx =10, pady =10)
e9 = Entry(root,width=20,borderwidth=20)
e9.grid(row=3,column=4,padx =10, pady =10)
e10 = Entry(root,width=20,borderwidth=20)
e10.grid(row=4,column=4,padx =10, pady =10)
e11 = Entry(root,width=20,borderwidth=20)
e11.grid(row=5,column=4,padx =10, pady =10)
e12 = Entry(root,width=20,borderwidth=20)
e12.grid(row=6,column=4,padx =10, pady =10)
Button_1 = Button(root,text = "1",padx = 10, pady= 10,command = lambda : ones([1,1,2,3,4]) )
Button_2 = Button(root,text = "2",padx = 10, pady= 10,command = lambda : ones([1,2,2,3,4])
Button_3 = Button(root,text = "3",padx = 10, pady= 10),command = lambda : ones([1,3,2,3,4])
Button_4 = Button(root,text = "4",padx = 10, pady= 10,command = lambda : ones([1,3,2,3,4])
Button_5 = Button(root,text = "5",padx = 10, pady= 10,command = lambda : ones([5,3,5,3,4])
Button_6 = Button(root,text = "6",padx = 10, pady= 10,command = lambda : ones([1,3,6,6,6])
Button_7 = Button(root,text = "3x",padx = 10, pady= 10)
Button_8 = Button(root,text = "4x",padx = 10, pady= 10)
Button_9 = Button(root,text = "ss",padx = 10, pady= 10)
Button_10 = Button(root,text = "ls",padx = 10, pady= 10)
Button_11 = Button(root,text = "f",padx = 10, pady= 10)
Button_12 = Button(root,text = "y",padx = 10, pady= 10)
Button_13 = Button(root,text = "c",padx = 10, pady= 10)
Button_1.grid(row =0 , column =0)
Button_2.grid(row =1 , column = 0)
Button_3.grid(row =2 , column =0)
Button_4.grid(row =3 , column =0)
Button_5.grid(row =4 , column =0)
Button_6.grid(row =5 , column =0)
Button_7.grid(row =0 , column =3)
Button_8.grid(row =1 , column =3)
Button_9.grid(row =2 , column =3)
Button_10.grid(row =3 , column =3)
Button_11.grid(row =4 , column =3)
Button_12.grid(row =5, column =3)
Button_13.grid(row =6, column =3)

def ones():
    total = sum ([num for num in dice if num == 1])
    e1.insert (0, total)


def twos():
    total = sum ([num for num in dice if num == 2])
    e2.insert (0, total)


def threes():
    total = sum ([num for num in dice if num == 3])
    e3.insert (0, total)


def fours():
    total = sum ([num for num in dice if num == 4])
    e4.insert (0, total)


def fives():
    total = sum ([num for num in dice if num == 5])
    e5.insert (0, total)


def sixes():
    total = sum ([num for num in dice if num == 6])
    e6.insert (0, total)

root.mainloop()
