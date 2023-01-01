from tkinter import *
from tkinter import messagebox
root=Tk()

ck=True
count=0




def checkifwin():
    global winner
    winner=False
    if(b1["text"]=="X"and b2["text"]=="X" and b3["text"]=="X"):
        b1.config("green")
        b2.config("green")
        b3.config("green")
        winner=True
        messagebox.showinfo("cong")
        disable_all_btns()
    elif(b4["text"]=="X"and b5["text"]=="X" and b6["text"]=="X"):
        b4.config("green")
        b5.config("green")
        b6.config("green")
        winner=True
        messagebox.showinfo("cong")
        disable_all_btns()
    
    elif(b7["text"]=="X"and b8["text"]=="X" and b9["text"]=="X"):
        b7.config("green")
        b8.config("green")
        b9.config("green")
        winner=True
        messagebox.showinfo("cong")
        disable_all_btns()
            
    elif(b1["text"]=="X"and b4["text"]=="X" and b7["text"]=="X"):
        b1.config("green")
        b4.config("green")
        b7.config("green")
        winner=True
        messagebox.showinfo("cong")
        disable_all_btns()
                
    elif(b2["text"]=="X"and b5["text"]=="X" and b8["text"]=="X"):
        b2.config("green")
        b5.config("green")
        b8.config("green")
        winner=True
        messagebox.showinfo("cong")
        disable_all_btns()
    elif(b3["text"]=="X"and b6["text"]=="X" and b9["text"]=="X"):
        b3.config("green")
        b6.config("green")
        b9.config("green")
        winner=True
        messagebox.showinfo("cong")
        disable_all_btns()
    elif(b1["text"]=="X"and b5["text"]=="X" and b9["text"]=="X"):
        b1.config("green")
        b5.config("green")
        b9.config("green")
        winner=True
        messagebox.showinfo("cong")
        disable_all_btns()
    elif(b3["text"]=="X"and b5["text"]=="X" and b7["text"]=="X"):
        b3.config("green")
        b5.config("green")
        b7.config("green")
        winner=True
        messagebox.showinfo("cong")
        disable_all_btns()
                                                                            

    if(b1["text"]=="Y"and b2["text"]=="Y" and b3["text"]=="Y"):
        b1.config("green")
        b2.config("green")
        b3.config("green")
        winner=True
        messagebox.showinfo("cong")
        disable_all_btns()
    elif(b4["text"]=="Y"and b5["text"]=="Y" and b6["text"]=="Y"):
        b4.config("green")
        b5.config("green")
        b6.config("green")
        winner=True
        messagebox.showinfo("cong")
        disable_all_btns()
    
    elif(b7["text"]=="Y"and b8["text"]=="Y" and b9["text"]=="Y"):
        b7.config("green")
        b8.config("green")
        b9.config("green")
        winner=True
        messagebox.showinfo("cong")
        disable_all_btns()
            
    elif(b1["text"]=="Y"and b4["text"]=="Y" and b7["text"]=="Y"):
        b1.config("green")
        b4.config("green")
        b7.config("green")
        winner=True
        messagebox.showinfo("cong")
        disable_all_btns()
                
    elif(b2["text"]=="Y"and b5["text"]=="Y" and b8["text"]=="Y"):
        b2.config("green")
        b5.config("green")
        b8.config("green")
        winner=True
        messagebox.showinfo("cong")
        disable_all_btns()
    elif(b3["text"]=="Y"and b6["text"]=="Y" and b9["text"]=="Y"):
        b3.config("green")
        b6.config("green")
        b9.config("green")
        winner=True
        messagebox.showinfo("cong")
        disable_all_btns()
    elif(b1["text"]=="Y"and b5["text"]=="Y" and b9["text"]=="Y"):
        b1.config("green")
        b5.config("green")
        b9.config("green")
        winner=True
        messagebox.showinfo("cong")
        disable_all_btns()
    elif(b3["text"]=="Y"and b5["text"]=="Y" and b7["text"]=="Y"):
        b3.config("green")
        b5.config("green")
        b7.config("green")
        winner=True
        messagebox.showinfo("cong")
        disable_all_btns()
                

def b_click(b):
    global ck,count
    if b["text"]==" " and ck==True:
       b["text"]="X"
       ck=False
       count+=1
       checkifwin()
    elif b["text"]==" " and ck==False:
       b["text"]="Y"
       ck=True
       count+=1
       checkifwin()
    else:
        messagebox.showerror("there is an error")      
def disable_all_btns():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)




b1=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b1))
b2=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b2))
b3=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b3))

b4=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b4))
b5=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b5))
b6=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b6))

b7=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b7))
b8=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b8))
b9=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b9))



b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)





root.title("tic tac")
root.mainloop()