from tkinter import *
from tkinter import messagebox
import time
window = Tk()
window.title("manger your time")
window.config(bg="#fff")
window.geometry("350x150+500+100")
window.resizable(False, False)
def get_value():
    k=enter_1.get()
    return k
def first_function_tk():
    def get_v_1():
        value_1_tk_1 = enter_2.get()
        #time = time.strftime("%H:%M")
        while True:
            if value_1_tk_1 ==time.strftime("%H:%M"):
                ###############
                messagebox.showinfo("message","thats time bach takhod dwa dialk")
                break
    root_1 = Tk()
    root_1.title("manger your time")
    root_1.config(bg="#fff")
    root_1.geometry("350x150+500+100")
    root_1.resizable(False, False)
    #groot_1.mainloop()
    label_2= Label(root_1,text="awal mara here: ",bg="#fff").place(x=10,y=20)
    enter_2= Entry(root_1,bg="#ccc",bd=0)
    enter_2.place(x=10,y=40,width=330,height=40)
    btn_2 =Button(root_1,text="Submit",bd=0,bg="#0f0",fg="#fff",command=get_v_1).place(x=10,y=90,width=330,height=40)
    root_1.mainloop()

def second_function_tk():
    def get_value_2():
        value_2_get_enter_1 = enter_2.get()
        value_2_get_enter_2 = enter_3.get()
        while True:
            if value_2_get_enter_1 ==time.strftime("%H:%M") :
                ###############
                messagebox.showinfo(f"message","thats time bach takhod dwa dialk")
                break
        while True:
            if value_2_get_enter_2 ==time.strftime("%H:%M"):
                ###############
                messagebox.showinfo(f"message","thats time bach takhod dwa dialk dialk")
                break

    #root_1 = Tk()
    root_1 = Tk()
    root_1.title("manger your time")
    root_1.config(bg="#fff")
    root_1.geometry("350x250+500+100")
    root_1.resizable(False, False)
    #groot_1.mainloop()
    label_3= Label(root_1,text="awal mara here: ",bg="#fff").place(x=10,y=20)
    enter_2= Entry(root_1,bg="#ccc",bd=0)
    enter_2.place(x=10,y=40,width=330,height=40)
    #btn_3 =Button(root_1,text="Submit",bd=0,bg="#00f",fg="#0f0").place(x=10,y=90,width=330,height=40)
    label_4= Label(root_1,text="tani mara here: ",bg="#fff").place(x=10,y=90)
    enter_3= Entry(root_1,bg="#ccc",bd=0)
    enter_3.place(x=10,y=110,width=330,height=40)
    btn_4 =Button(root_1,text="Submit",bd=0,bg="#0f0",fg="#fff",command=get_value_2).place(x=10,y=170,width=330,height=40)
    root_1.mainloop()
def there_function_tk():
    def get_value_3():
        get_valeur_1 = enter_2.get()
        get_valeur_3 = enter_3.get()
        get_valeur_4 = enter_4.get()
        while True:
            if get_valeur_1 ==time.strftime("%H:%M") :
                ###############
                messagebox.showinfo(f"message","thats time bach takhod dwa dialk lowl")
                break
        while True:
            if get_valeur_3 ==time.strftime("%H:%M"):
                ###############
                messagebox.showinfo(f"message","thats time bach takhod dwa dialk dialk tani")
                break
        while True:
            if get_valeur_4 ==time.strftime("%H:%M"):
                ###############
                messagebox.showinfo(f"message","thats time bach takhod dwa dialk dialk talt")
                break
    root_1 = Tk()
    root_1.title("manger your time")
    root_1.config(bg="#fff")
    root_1.geometry("350x300+500+100")
    root_1.resizable(False, False)
    #groot_1.mainloop()
    label_3= Label(root_1,text="awal mara here: ",bg="#fff").place(x=10,y=20)
    enter_2= Entry(root_1,bg="#ccc",bd=0)
    enter_2.place(x=10,y=40,width=330,height=40)
    #btn_3 =Button(root_1,text="Submit",bd=0,bg="#00f",fg="#0f0").place(x=10,y=90,width=330,height=40)
    label_4= Label(root_1,text="tani mara here: ",bg="#fff").place(x=10,y=90)
    enter_3= Entry(root_1,bg="#ccc",bd=0)
    enter_3.place(x=10,y=110,width=330,height=40)
    label_5= Label(root_1,text="tani mara here: ",bg="#fff").place(x=10,y=160)
    enter_4= Entry(root_1,bg="#ccc",bd=0)
    enter_4.place(x=10,y=180,width=330,height=40)
    btn_4 =Button(root_1,text="Submit",bd=0,bg="#0f0",fg="#fff",command=get_value_3).place(x=10,y=230,width=330,height=40)
    root_1.mainloop()
def oncklick_btn():
    value_enter_1 =int(get_value())
    if value_enter_1 >3 or value_enter_1 <0:
        messagebox.showwarning("","kidrti liha malk 3la 7altk akhouya ana hna 3andib 3")
    else:
        if value_enter_1==1:
            first_function_tk()
        elif value_enter_1==2:
            second_function_tk()
        elif value_enter_1==3:
            there_function_tk()
label_1= Label(window,text="ch7al mn mara katakhod dwa fnhar: ",bg="#fff").place(x=10,y=20)
input_text = StringVar()
enter_1= Entry(window,bg="#ccc",bd=0,textvariable=input_text)
enter_1.place(x=10,y=40,width=330,height=40)
btn =Button(window,text="Submit",bd=0,bg="#00f",fg="#fff",command=oncklick_btn).place(x=10,y=90,width=330,height=40)











window.mainloop()