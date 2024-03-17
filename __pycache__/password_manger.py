from tkinter import * 
import tkinter as tk
import cv2
from tkinter import messagebox
import os
window = Tk()
password= "12345678"
window.geometry("320x450+600+100")
window.resizable(False,False)
window.config(bg="#ddd")

# window.attributes("-alpha",0.6)
label_title = Label(window,text="Welcome Here",bg="#ddd",fg="#000",font=("Arial",15)).place(x=0,y=10,width=320,height=30)
label_password = Label(window,text="enter the password: ",bg="#ddd",fg="#000").place(x=0,y=60)
input_text = StringVar()
enter_1 = tk.Entry(window,bd=1,bg="#ddd",justify=CENTER,font=("Arial",16),textvariable=input_text).place(x=-10,y=80,width=340,height=40)
#buttons
def get_value(nbr):
    value = input_text.get()
    input_text.set(value + str(nbr))
def clear():
    value = input_text.get()
    if value:
        input_text.set(value[:-1])  # Remove the last character
def true_code():
    value = input_text.get()
    if value == password:
        os.startfile("C:\LDPlayer\LDPlayer9\dnplayer.exe")
        
    else:
        input_text.set("")
        s = cv2.VideoCapture(0)
        image = s.read()
        cv2.imwrite("jassos.png",image)
        del(s)
        messagebox.showerror("","error try again")

btn_1 = Button(window,text="1",font=("Arial",30),bg="#ddd",bd=0,command=lambda:get_value(1)).place(x=10,y=150,width= 60,height=60)
btn_1 = Button(window,text="2",font=("Arial",30),bg="#ddd",bd=0,command=lambda:get_value(2)).place(x=120,y=150,width=60,height=60)
btn_1 = Button(window,text="3",font=("Arial",30),bg="#ddd",bd=0,command=lambda:get_value(3)).place(x=230,y=150,width=60,height=60)
btn_1 = Button(window,text="4",font=("Arial",30),bg="#ddd",bd=0,command=lambda:get_value(4)).place(x=10,y= 240,width=60,height=60)
btn_1 = Button(window,text="5",font=("Arial",30),bg="#ddd",bd=0,command=lambda:get_value(5)).place(x=120,y=240,width=60,height=60)
btn_1 = Button(window,text="6",font=("Arial",30),bg="#ddd",bd=0,command=lambda:get_value(6)).place(x=230,y=240,width=60,height=60)
btn_1 = Button(window,text="7",font=("Arial",30),bg="#ddd",bd=0,command=lambda:get_value(7)).place(x=10,y= 310,width=60,height=60)
btn_1 = Button(window,text="8",font=("Arial",30),bg="#ddd",bd=0,command=lambda:get_value(8)).place(x=120,y=310,width=60,height=60)
btn_1 = Button(window,text="9",font=("Arial",30),bg="#ddd",bd=0,command=lambda:get_value(9)).place(x=230,y=310,width=60,height=60)
btn_1 = Button(window,text="Rest",font=("Arial",10),bg="#f00",bd=0,command=clear).place(x=0,y=400,width=165,height=60)
btn_1 = Button(window,text="Submit",font=("Arial",10),bg="#0ff",bd=0,command=true_code).place(x=160,y=400,width=165,height=60)
window.mainloop()
