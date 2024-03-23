from tkinter import *
import pywhatkit

window = Tk()
window.title("WhatsApp Manager")
window.config(bg="#ccc")
window.geometry("400x460+500+100")
window.resizable(False, False)

def get_numero():
    return input_text1.get()

def get_message():
    return input_text2.get()

def get_time_hour():
    return input_text3.get()

def get_time_minutes():
    return input_text4.get()

def button():
    pywhatkit.sendwhatmsg(get_numero(),get_message(),get_time_hour(),get_time_minutes())

Label(window, text="Numero de WhatsApp", bg="#ccc").place(x=10, y=18)
input_text1 = StringVar()
Entry(window, bg="#fff", bd=0, textvariable=input_text1).place(x=10, y=50, width=370, height=50)

Label(window, text="Message", bg="#ccc").place(x=10, y=108)
input_text2 = StringVar()
Entry(window, bg="#fff", bd=0, textvariable=input_text2).place(x=10, y=140, width=370, height=50)

Label(window, text="Time with Hour", bg="#ccc").place(x=10, y=198)
input_text3 = StringVar()
Entry(window, bg="#fff", bd=0, textvariable=input_text3).place(x=10, y=230, width=370, height=50)

Label(window, text="Time with Minutes", bg="#ccc").place(x=10, y=295)
input_text4 = StringVar()
Entry(window, bg="#fff", bd=0, textvariable=input_text4).place(x=10, y=330, width=370, height=50)

Button(window, text="Submit", bg="#0f0", fg="white", bd=0, activebackground="green", command=button).place(x=10, y=400, width=370, height=42)

window.mainloop()
