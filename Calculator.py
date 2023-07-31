#==================Windows setting============
import math
from tkinter import *
root= Tk()
root.title("Simple calculator")
root.resizable(width=False,height=False)
#================== frames  ============
color="#A556E6"

root.configure(bg=color)
top_first= Frame(root, width=400, height=100,bg= color)
top_first.pack(side=TOP)
top_sec= Frame(root, width=400, height=100,bg= color)
top_sec.pack(side=TOP)
top_third= Frame(root, width=400, height=100,bg= color)
top_third.pack(side=TOP)
top_forth= Frame(root, width=400, height=100,bg= color)
top_forth.pack(side=TOP)
top_five= Frame(root, width=400, height=100,bg= color)
top_forth.pack(side=LEFT)
#======================variables
num1= StringVar()
num2= StringVar()
res= StringVar()

#=====================labels and Entry==============
Label1= Label(top_first, text="Number 1: ",font= "arial", bg=color)
Label1.pack(side=LEFT,padx=3, pady=3)
entry_1= Entry(top_first,width=20,font= "arial", textvariable=num1)
entry_1.pack(side=LEFT,padx=3,pady=3)
label2= Label(top_sec, text="Number 2: ",font= "arial", bg=color)
label2.pack(side=LEFT, padx=3,pady=3)
entry_2= Entry(top_sec,width=20,font= "arial", textvariable=num2)
entry_2.pack(side=RIGHT)
label3= Label(top_forth, text="Result",font= "arial", bg=color)
label3.pack(side=LEFT,padx=3,pady=3)

#============ Functions==============

def plus():
    try:
        Values= float(num1.get())+ float(num2.get())
        res.set(Values)
    except:
        errormsg= ("Error in plus function")
def minus():
    try:
        min_values= float(num1.get())-float(num2.get())
        res.set(min_values)
    except:
        errormsg2= ("Error in minus function")
def multiplication():
    try:
        multiplication_values= float(num1.get()) * float(num2.get())
        res.set(multiplication_values)
    except:
        errormsg3= ("Error in multiplication function")
def devide():
    try:
        
        div_values= float(num1.get()) / float(num2.get())
        res.set(div_values)
    except:
        errormsg3= ("Error in divide function")
def to_power():
    try:
        power_val= float(num1.get()) ** float(num2.get())
        res.set(power_val)
    except:
        errormsg4= ("Error in power function")


    
#=====================Buttons==============
btn_plus= Button(top_third, text= "+",font= "arial",bg="#77A4E5",width=4,height=1,command= lambda: plus())
btn_plus.pack(side=LEFT,padx=3,pady=3)
btn_minus= Button(top_third,text="-",font= "arial",bg="#77A4E5",width=4,height=1,command=lambda: minus())
btn_minus.pack(side=RIGHT,padx=3,pady=3)
btn_multiplication= Button(top_third,text="X",font= "arial",bg="#77A4E5",width=4,height=1,command= lambda: multiplication())
btn_multiplication.pack(side=RIGHT,padx=3,pady=3)
btn_div= Button(top_third,text="/",font= "arial",bg="#77A4E5",width=4,height=1, command= lambda: devide())
btn_div.pack(side=RIGHT,padx=3,pady=3)
btn_power= Button(top_third,width=4, height=1, text="^",font= "arial",bg="#77A4E5",command= lambda: to_power())
btn_power.pack(side=LEFT,padx=3, pady=3)

#======================result====
entry_3= Entry(top_forth,width=23,state="readonly",font= "arial", textvariable=res)
entry_3.pack(side= TOP, padx=3,pady=3)



root.mainloop()
