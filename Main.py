from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb # "A Algorithm from stegano module "

root=Tk()
root.title("Image Steganography")
root.geometry("700x500+150+180")
root.resizable(False,False)
root.configure(bg="#2f4155")

def selectimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Please Select Image for Hide Message",filetypes=(("PNG File","*.png"),
                                                                                                                       ("JPG File","*.jpg"),
                                                                                                                       ("All File","*.text")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image=img
    
def encrypt():
    global secret
    message=text1.get(1.0,END)
    secret = lsb.hide(str(filename),message)

def decrypt():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0,END)
    text1.insert(END,clear_message)

def select():
    secret.save("encrypt.png")



Label(root,text="Image Steganography - Hide data Into Image",bg="#2d4155",fg="white",font="arial 20 bold").place(x=50,y=20)

#first Frame
frame1=Frame(root,bd=3,bg="black",width=340,height=280,relief=GROOVE)
frame1.place(x=10,y=80)

lbl=Label(frame1,bg="black")
lbl.place(x=40,y=10)

#second frame
frame2=Frame(root,bd=3,bg="white",width=340,height=280,relief=GROOVE)
frame2.place(x=350,y=80)

text1=Text(frame2,font="arial 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=320,height=295)

scrollbar1=Scrollbar(frame2)
scrollbar1.place(x=320,y=0,height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#third frame
frame3=Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
frame3.place(x=10,y=370)

Button(frame3,text="Select Image",width=10,height=2,font="arial 14 bold",command=selectimage).place(x=20,y=30)
Button(frame3,text="Save Image",width=10,height=2,font="arial 14 bold",command=select).place(x=180,y=30)
Label(frame3,text="Please select Image from Hide data",bg="#2f4155",fg="yellow").place(x=50,y=5)

#third frame
frame4=Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
frame4.place(x=360,y=370)

Button(frame4,text="Encrypt",width=10,height=2,font="arial 14 bold",command=encrypt).place(x=20,y=30)
Button(frame4,text="Decrypt",width=10,height=2,font="arial 14 bold",command=decrypt).place(x=180,y=30)
Label(frame4,text="Please select Image from Encrypt and Decrypt",bg="#2f4155",fg="yellow").place(x=20,y=5)
    


root.mainloop()

