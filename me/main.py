from tkinter import *
import tkinter as tk

window = Tk()
window.title("calculator")
window.resizable(False,False)
window.geometry("300x350+500+100")
window.config(bg="#ccc")
text_input = StringVar()

entry = tk.Entry(window,bd=1,bg="#ccc",font=("Arial",26),fg="#000",textvariable=text_input)
entry.place(x=0,y=50,width=300,height=60)

def affivher_nbr(nbr):
    current_number = text_input.get()
    text_input.set((current_number) + str(nbr))
def clear():
    entry.delete(0, tk.END)
def button_add():
    first_number_str = text_input.get()
    global first_number
    global operation
    first_number = float(first_number_str)
    operation = "+"
    entry.delete(0,tk.END)
def button_moin():
    first_number_str = text_input.get()
    global first_number
    global operation
    first_number = float(first_number_str)
    operation = "-"
    entry.delete(0,tk.END)
def button_darb():
    first_number_str = text_input.get()
    global first_number
    global operation
    first_number = float(first_number_str)
    operation = "x"
    entry.delete(0,tk.END)
def button_l0issma():
    first_number_str = text_input.get()
    global first_number
    global operation
    first_number = float(first_number_str)
    operation = "/"
    entry.delete(0,tk.END)
def answear_button():
    second_number = text_input.get()
    entry.delete(0,tk.END)
    if operation == "+":
        text_input.set((first_number) + float(second_number))
    if operation == "-":
        text_input.set((first_number) - float(second_number))
    if operation == "x":
        text_input.set((first_number) * float(second_number))
    if operation == "/":
        text_input.set((first_number) / float(second_number))
  

Btn1 = Button(window,text="1",width=8,height=2,bd=0,font=("Arial",10),bg="#fff",command=lambda:affivher_nbr(1)).place(x=1,y=130)
Btn2 = Button(window,text="2",width=8,height=2,bd=0,font=("Arial",10),bg="#fff",command=lambda:affivher_nbr(2)).place(x=80,y=130)
Btn3 = Button(window,text="3",width=8,height=2,bd=0,font=("Arial",10),bg="#fff",command=lambda:affivher_nbr(3)).place(x=160,y=130)
Btnc = Button(window,text="c",width=7,height=2,bd=0,font=("Arial",10),bg="orange",command=clear).place(x=235,y=130)
Btn4 = Button(window,text="4",width=8,height=2,bd=0,font=("Arial",10),bg="#fff",command=lambda:affivher_nbr(4)).place(x=1,y=180)
Btn5 = Button(window,text="5",width=8,height=2,bd=0,font=("Arial",10),bg="#fff",command=lambda:affivher_nbr(5)).place(x=80,y=180)
Btn6 = Button(window,text="6",width=8,height=2,bd=0,font=("Arial",10),bg="#fff",command=lambda:affivher_nbr(6)).place(x=160,y=180)
Btns = Button(window,text="/",width=7,height=2,bd=0,font=("Arial",10),bg="orange",command=button_l0issma).place(x=235,y=180)
Btn7 = Button(window,text="7",width=8,height=2,bd=0,font=("Arial",10),bg="#fff",command=lambda:affivher_nbr(7)).place(x=1,y=230)
Btn8 = Button(window,text="8",width=8,height=2,bd=0,font=("Arial",10),bg="#fff",command=lambda:affivher_nbr(8)).place(x=80,y=230)
Btn9 = Button(window,text="9",width=8,height=2,bd=0,font=("Arial",10),bg="#fff",command=lambda:affivher_nbr(9)).place(x=160,y=230)
Btn_darb = Button(window,text="*",width=7,height=2,bd=0,font=("Arial",10),bg="orange",command=button_darb).place(x=235,y=230)
Btn_fassila = Button(window,text="0",width=8,height=2,bd=0,font=("Arial",10),bg="#fff",command=lambda:affivher_nbr(0)).place(x=1,y=280)
Btn_na9iss = Button(window,text="-",width=8,height=2,bd=0,font=("Arial",10),bg="orange",command=button_moin).place(x=80,y=280)
Btn9_place = Button(window,text="+",width=8,height=2,bd=0,font=("Arial",10),bg="orange",command=button_add).place(x=160,y=280)
Btn_resulta = Button(window,text="=",width=7,height=2,bd=0,font=("Arial",10),bg="orange",command=answear_button).place(x=235,y=280)

window.mainloop()
