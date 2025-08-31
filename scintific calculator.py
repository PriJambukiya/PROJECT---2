from tkinter import *
import math
import tkinter.messagebox
root=Tk()
root.geometry("650x400+300+300")
root.title("scientific calculator")
switch=None

def btn_1():
    if pris.get() == "0":
        pris.delete(0,END)
    pos=len(pris.get())
    pris.insert(pos, "1")
    
def btn_2():
    if pris.get() == "0":
        pris.delete(0,END)
    pos=len(pris.get())
    pris.insert(pos, "2")
    
def btn_3():
    if pris.get() == "0":
        pris.delete(0,END)
    pos=len(pris.get())
    pris.insert(pos, "3")

def btn_4():
    if pris.get() == "0":
        pris.delete(0,END)
    pos=len(pris.get())
    pris.insert(pos, "4")
    
def btn_5():
    if pris.get() == "0":
        pris.delete(0,END)
    pos=len(pris.get())
    pris.insert(pos, "5")
    
def btn_6():
    if pris.get() == "0":
        pris.delete(0,END)
    pos=len(pris.get())
    pris.insert(pos, "6")

def btn_7():
    if pris.get() == "0":
        pris.delete(0,END)
    pos=len(pris.get())
    pris.insert(pos, "7")
    
def btn_8():
    if pris.get() == "0":
        pris.delete(0,END)
    pos=len(pris.get())
    pris.insert(pos, "8")
    
def btn_9():
    if pris.get() == "0":
        pris.delete(0,END)
    pos=len(pris.get())
    pris.insert(pos, "9")
    
    
def btn_0():
    if pris.get() == "0":
        pris.delete(0,END)
    pos=len(pris.get())
    pris.insert(pos, "0")
    
def btn_p():
    pos=len(pris.get())
    pris.insert(pos, "+")
    
def btn_s():
    pos=len(pris.get())
    pris.insert(pos, "-")
    
def btn_ml():
    pos=len(pris.get())
    pris.insert(pos, "*")
    
def btn_di():
    pos=len(pris.get())
    pris.insert(pos, "/")

def sin():
    try:
        ans = float(pris.get())
        if switch is True:
            ans = math.sin(math.radians(ans))
        else: 
            ans = math.sin(ans)
            pris.delete(0, END)
            pris.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("velue error! check your operator and operand")   
        
def cos():
    try:
        ans=float(pris.get())
        if switch is True:
            ans=math.cos(math.radiants(ans))
        else:
            ans=math.cos(ans)
            pris.delete(0,END)
            pris.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("velue error! check your operator and operand") 
def tan():
    try:
        ans=float(pris.get())
        if switch is True:
            ans=math.tan(math.radiants(ans))
        else:
            ans=math.tan(ans)
            pris.delete(0,END)
            pris.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("velue error! check your operator and operand")    
def asin():
    try:
        ans=float(pris.get())
        if switch is True:
            ans=math.asin(math.radiants(ans))
        else:
            ans=math.asin(ans)
            pris.delete(0,END)
            pris.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("velue error! check your operator and operand")   
        
def acos():
    try:
        ans=float(pris.get())
        if switch is True:
            ans=math.acos(math.radiants(ans))
        else:
            ans=math.acos(ans)
            pris.delete(0,END)
            pris.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("velue error! check your operator and operand") 
def atan():
    try:
        ans=float(pris.get())
        if switch is True:
            ans=math.atan(math.radiants(ans))
        else:
            ans=math.atan(ans)
            pris.delete(0,END)
            pris.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("velue error! check your operator and operand")  
def pow():
    pos=len(pris.get())
    pris.insert(pos,"**")
    
def dot():
    pos=len(pris.get())
    pris.insert(pos,".")
    
def br():
    pos=len(pris.get())
    pris.insert(pos,")")
    
def bl():
    pos=len(pris.get())
    pris.insert(pos,"(")

def cl(*args):
    pris.delete(0,END)
    pris.insert(0,'0')
    
def mod():
    pos = len(pris.get())
    pris.insert(pos, '%')    
    
def eq():
    try:
        ans = pris.get()
        ans = eval(ans)
        pris.delete(0, END)
        pris.insert(0, ans)
    except Exception:
        tkinter.messagebox.showerror("velue error! check your operator and operand")   
        
def round():
    try:
        ans = float(pris.get())
        ans = round(ans)
        pris.delete(0, END)
        pris.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("velue error! check your operator and operand")  

def sqrt():
    try:
        ans=float(pris.get())
        ans=math.sqrt(ans)
        pris.delete(0,END)
        pris.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("velue error! check your operator and operand")  



def log():
    try:
        ans=float(pris.get())
        ans=math.log10(ans)
        pris.delete(0,END)
        pris.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("velue error! check your operator and operand")  

def ln():
    try:
        ans=float(pris.get())
        ans=math.log(ans)
        pris.delete(0,END)
        pris.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("velue error! check your operator and operand") 
         
def fact():
    try:
        ans = float(pris.get())
        ans = math.factorial(ans)
        pris.delete(0, END)
        pris.insert(0, str(ans))    
    except Exception:
        tkinter.messagebox.showerror("velue error! check your operator and operand")  
            
        
def btn_pi():
    if pris.get() == "0":
        pris.delete(0,END)
    pos=len(pris.get())
    pris.insert(pos,str(math.pi))
                   
def btn_ex():
    if pris.get() == "0":
        pris.delete(0, END)
    pos = len(pris.get())
    pris.insert(pos, str(math.e))
        
        
def beck():
    pos=len(pris.get())
    display=str(pris.get())
    if display=='':
        pris.insert(0,"0")
    elif display=='':
        pris.insert(0,"0")
    elif display=="0":
        pass
    else:
        pris.delete(0, END)
        pris.insert(0,display[0:pos-1])
def conv():
      global switch
      if switch is None:
          switch = True  
          conv['text'] = "Deg" 
      else:
          switch = None
          conv['text'] = "Rad"
           
pris=Entry(root, font="verdana 20", fg="Black", bg="mistyrose", bd=4, justify=RIGHT)
pris.insert(0, "0")
pris.pack(expand=TRUE, fill=BOTH)

# row 1 Buttons
btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand=TRUE, fill=BOTH)
pi_btn = Button(btnrow1, text="π", font="segoe 18", relief=GROOVE, bd=0, command=btn_pi, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           
fact_btn = Button(btnrow1, text=" x! ", font="segoe 18", relief=GROOVE, bd=0, command=fact, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           
sin_btn = Button(btnrow1, text="sin", font="segoe 18", relief=GROOVE, bd=0, command=sin, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           
cos_btn = Button(btnrow1, text="cos", font="segoe 18", relief=GROOVE, bd=0,  command=cos, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           
tan_btn = Button(btnrow1, text="tan", font="segoe 18", relief=GROOVE, bd=0,  command=tan, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           
btn1 = Button(btnrow1, text="1", font="segoe 23", relief=GROOVE, bd=0, command=btn_1, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           
btn2 = Button(btnrow1, text="2", font="segoe 23", relief=GROOVE, bd=0, command=btn_2, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           
btn3 = Button(btnrow1, text="3", font="segoe 23", relief=GROOVE, bd=0, command=btn_3, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           
btnp = Button(btnrow1, text="+", font="segoe 23", relief=GROOVE, bd=0, command=btn_p, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           

# Row 2 Buttons
btnrow2 = Frame(root)
btnrow2.pack(expand=TRUE, fill=BOTH)
e_btn = Button(btnrow2, text="e", font="segoe 18", relief=GROOVE, bd=0, command=btn_ex, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           
sqr_btn = Button(btnrow2, text=" √x ", font="segoe 18", relief=GROOVE, bd=0, command=sqrt, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           
sinh_btn = Button(btnrow2, text="sin-1", font="segoe 11 bold", relief=GROOVE, bd=0,  command=asin, fg="pink",bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           
cosh_btn = Button(btnrow2, text="cos-1", font="segoe 11 bold", relief=GROOVE, bd=0,  command=acos, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           
tanh_btn = Button(btnrow2, text="tan-1", font="segoe 11 bold", relief=GROOVE, bd=0,  command=atan, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           
btn4 = Button(btnrow2, text="4", font="segoe 23", relief=GROOVE, bd=0, command=btn_4, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           
btn5 = Button(btnrow2, text="5", font="segoe 23", relief=GROOVE, bd=0, command=btn_5,fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           
btn6 = Button(btnrow2, text="6", font="segoe 23", relief=GROOVE, bd=0, command=btn_6, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           
btnm = Button(btnrow2, text="-", font="segoe 23", relief=GROOVE, bd=0, command=btn_s, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           

# Row 3 Buttons
btnrow3 = Frame(root)
btnrow3.pack(expand=TRUE, fill=BOTH)
conv_btn = Button(btnrow3, text="Rad", font="segoe 12 bold", relief=GROOVE, bd=0, command=conv, fg="pink", bg="#FF6984").pack(side=LEFT, expand=TRUE, fill=BOTH)    
round_btn = Button(btnrow3, text="round", font="segoe 10 bold", relief=GROOVE, bd=0, command=round, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           
ln_btn = Button(btnrow3, text="ln", font="segoe 18", relief=GROOVE, bd=0, fg="pink", command=ln, bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           
logarithm_btn = Button(btnrow3, text="log", font="segoe 17", relief=GROOVE, bd=0, command=log, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           
pow_btn = Button(btnrow3, text="x^y", font="segoe 17", relief=GROOVE, bd=0,  command=pow, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           
btn7 = Button(btnrow3, text="7", font="segoe 23", relief=GROOVE, bd=0, command=btn_7, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           
btn8 = Button(btnrow3, text="8", font="segoe 23", relief=GROOVE, bd=0, command=btn_8, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           
btn9 = Button(btnrow3, text="9", font="segoe 23", relief=GROOVE, bd=0, command=btn_9, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           
btnml = Button(btnrow3, text="*", font="segoe 23", relief=GROOVE, bd=0, command=btn_ml, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           

# Row 4 Buttons
btnrow4 = Frame(root)
btnrow4.pack(expand=TRUE, fill=BOTH)
mod_btn = Button(btnrow4, text="%", font="segoe 21", relief=GROOVE, bd=0, command=mod, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           
bl_btn = Button(btnrow4, text=" ( ", font="segoe 21", relief=GROOVE, bd=0, command=bl, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           
br_btn = Button(btnrow4, text=" ) ", font="segoe 21", relief=GROOVE, bd=0, command=br, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           
dot_btn = Button(btnrow4, text=" . ", font="segoe 18 bold", relief=GROOVE, bd=0, command=dot, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           
btnc = Button(btnrow4, text=" C ", font="segoe 23", relief=GROOVE, bd=0, command=cl, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           
del_btn = Button(btnrow4, text="<--", font="segoe 20", relief=GROOVE, bd=0, command=beck, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           
btn0 = Button(btnrow4, text="0", font="segoe 23", relief=GROOVE, bd=0, command=btn_0, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           
btneq = Button(btnrow4, text="=", font="segoe 18", relief=GROOVE, bd=0, command=eq, fg="pink", bg="#FA8072").pack(side=LEFT, expand=TRUE, fill=BOTH)           
btnd = Button(btnrow4, text="/", font="segoe 23", relief=GROOVE, bd=0, command=btn_di, fg="pink", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH)           

root.mainloop()
