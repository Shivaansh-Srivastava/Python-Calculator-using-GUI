# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 11:05:55 2021

@author: SHIVAANSH
"""

import tkinter as tK
from tkinter import messagebox

root=tK.Tk()
root.title("Calculator")
v1=tK.StringVar()
expression=""
def press(num):
    global expression
    expression=expression+str(num)
    v1.set(expression)
def equalpress():
    global expression
    total=str(eval(expression))
    v1.set(total)
    expression=""
def clear():
    global expression
    expression=""
    v1.set("")
en1=tK.Entry(root,textvariable=v1)
en1.grid(columnspan=4,padx=0,pady=0)
b1=tK.Button(root,text="C",height=1,width=7,command=clear)
b1.grid(row=1,padx=0,pady=0)
b2=tK.Button(root,text="√",height=1,width=7,command=lambda: press("**(0.5)"))
b2.grid(row=1,column=1,padx=0,pady=0)
b3=tK.Button(root,text="x^y",height=1,width=7,command=lambda: press("**"))
b3.grid(row=1,column=2,padx=0,pady=0)
b4=tK.Button(root,text="%",height=1,width=7)
b4.grid(row=1,column=3,padx=0,pady=0)
b5=tK.Button(root,text="1",height=1,width=7,command=lambda: press(1))
b5.grid(row=2,column=0,padx=0,pady=0)
b6=tK.Button(root,text="2",height=1,width=7,command=lambda: press(2))
b6.grid(row=2,column=1,padx=0,pady=0)
b7=tK.Button(root,text="3",height=1,width=7,command=lambda: press(3))
b7.grid(row=2,column=2,padx=0,pady=0)
b8=tK.Button(root,text="+",height=1,width=7,command=lambda: press("+"))
b8.grid(row=2,column=3,padx=0,pady=0)
b9=tK.Button(root,text="4",height=1,width=7,command=lambda: press(4))
b9.grid(row=3,padx=0,pady=0)
b10=tK.Button(root,text="5",height=1,width=7,command=lambda: press(5))
b10.grid(row=3,column=1,padx=0,pady=0)
b11=tK.Button(root,text="6",height=1,width=7,command=lambda: press(6))
b11.grid(row=3,column=2,padx=0,pady=0)
b12=tK.Button(root,text="-",height=1,width=7,command=lambda: press("-"))
b12.grid(row=3,column=3,padx=0,pady=0)
b13=tK.Button(root,text="7",height=1,width=7,command=lambda: press(7))
b13.grid(row=4,padx=0,pady=0)
b14=tK.Button(root,text="8",height=1,width=7,command=lambda: press(8))
b14.grid(row=4,column=1,padx=0,pady=0)
b15=tK.Button(root,text="9",height=1,width=7,command=lambda: press(9))
b15.grid(row=4,column=2,padx=0,pady=0)
b16=tK.Button(root,text="*",height=1,width=7,command=lambda: press("*"))
b16.grid(row=4,column=3,padx=0,pady=0)
b17=tK.Button(root,text="0",height=1,width=7,command=lambda: press(0))
b17.grid(row=5,padx=0,pady=0)
b18=tK.Button(root,text=".",height=1,width=7,command=lambda: press("."))
b18.grid(row=5,column=1,padx=0,pady=0)
b19=tK.Button(root,text="=",bg="yellow",height=1,width=7,command=equalpress)
b19.grid(row=5,column=2,padx=0,pady=0)
b20=tK.Button(root,text="/",height=1,width=7,command=lambda: press("/"))
b20.grid(row=5,column=3,padx=0,pady=0)
root.mainloop()