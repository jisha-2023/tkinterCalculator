from tkinter import *

wind = Tk()
wind.title("My Calculator")
wind.geometry("530x300")
wind.configure(background="black",borderwidth="3",relief="sunken")
wind.resizable(False,False)

calcul =""
def insert_symbol(sym):
    global calcul
    calcul  += str(sym)
    results.delete(1.0,"end")
    results.insert(1.0,calcul)

def perform_calc():
    global calcul
    try:
        calcul=str(eval(calcul))
        results.delete(1.0,"end")
        results.insert(1.0,calcul)
    except:
        clear_values()
        results.insert(1.0,"Error!!")


def clear_values():
    global calcul
    calcul=""
    results.delete(1.0,"end")

but_1 = Button(wind,text="1",command=lambda: insert_symbol(1),width=10,font=("Times New Roman",16),relief="raised",fg="black",bg="#adadad")
but_1.grid(row=2,column=1)
but_2 = Button(wind,text="2",background="#adadad",command=lambda: insert_symbol(2),width=10,font=("Times New Roman",16),relief="raised")
but_2.grid(row=2,column=2)
but_3 = Button(wind,text="3",background="#adadad",command=lambda: insert_symbol(3),width=10,font=("Times New Roman",16),relief="raised")
but_3.grid(row=2,column=3)
but_4 = Button(wind,text="4",background="#adadad",command=lambda: insert_symbol(4),width=10,font=("Times New Roman",16),relief="raised")
but_4.grid(row=3,column=1)
but_5 = Button(wind,text="5",background="#adadad",command=lambda: insert_symbol(5),width=10,font=("Times New Roman",16),relief="raised")
but_5.grid(row=3,column=2)
but_6 = Button(wind,text="6",background="#adadad",command=lambda: insert_symbol(6),width=10,font=("Times New Roman",16),relief="raised")
but_6.grid(row=3,column=3)
but_7 = Button(wind,text="7",background="#adadad",command=lambda: insert_symbol(7),width=10,font=("Times New Roman",16),relief="raised")
but_7.grid(row=4,column=1)
but_8 = Button(wind,text="8",background="#adadad",command=lambda: insert_symbol(8),width=10,font=("Times New Roman",16),relief="raised")
but_8.grid(row=4,column=2)
but_9 = Button(wind,text="9",background="#adadad",command=lambda: insert_symbol(9),width=10,font=("Times New Roman",16),relief="raised")
but_9.grid(row=4,column=3)
but_0 = Button(wind,text="0",background="#adadad",command=lambda: insert_symbol(0),width=10,font=("Times New Roman",16),relief="raised")
but_0.grid(row=5,column=2)
but_divide = Button(wind,text="/",background="#b4eeb4",command=lambda: insert_symbol("/"),width=10,font=("Times New Roman",16),relief="raised")
but_divide.grid(row=6,column=1)
but_multi = Button(wind,text="*",background="#b4eeb4",command=lambda: insert_symbol("*"),width=10,font=("Times New Roman",16),relief="raised")
but_multi.grid(row=6,column=2)
but_minus = Button(wind,text="-",background="#b4eeb4",command=lambda: insert_symbol("-"),width=10,font=("Times New Roman",16),relief="raised")
but_minus.grid(row=6,column=3)
but_plus = Button(wind,text="+",background="#b4eeb4",command=lambda: insert_symbol("+"),width=10,font=("Times New Roman",16),relief="raised")
but_plus.grid(row=6,column=4)
but_leftbracket = Button(wind,text="(",background="#b4eeb4",command=lambda: insert_symbol("("),width=10,font=("Times New Roman",16),relief="raised")
but_leftbracket.grid(row=5,column=1)
but_rightbracket = Button(wind,text=")",background="#b4eeb4",command=lambda: insert_symbol(")"),width=10,font=("Times New Roman",16),relief="raised")
but_rightbracket.grid(row=5,column=3)
but_equal = Button(wind,text="=",background="#e97451",command=lambda: perform_calc(),width=10,height=5,font=("Times New Roman",16),relief="raised")
but_equal.grid(row=3,column=4,rowspan=3)
but_clear = Button(wind,text="C",background="#b4eeb4",command=lambda: clear_values(),width=10,font=("Times New Roman",16),relief="raised")
but_clear.grid(row=2,column=4)


results = Text(wind,height=2,width=33,font=("Arial",20),background="black",relief="flat",fg="white")
results.grid(row=1,columnspan=5)  # took the first row and whole 5 columns

wind.mainloop()