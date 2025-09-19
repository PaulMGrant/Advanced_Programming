#Title: Interface Examples
#Author: Paul Grant
#Date: 19/09/2025
#Description: Programs to dempnstrate the use of TKinter

#Note: PEP88 Standards

#Libraries
from tkinter import *
import tkinter.messagebox as box

#Instance
window=Tk()

#procedures and functions will go here
def display_window(size,name):
  window.geometry(size)
  window.title(name)

#Procedure label
def display_label(xlbl,ylbl,textlbl):
  label=Label(window,text=textlbl)
  label.place(x=xlbl, y=ylbl)

#Procedure to display message boxes
def display_message(the_message):
  box.showinfo("info", the_message)
  #box.showerror("Error",the_message)
  #box.askquestion("Question", the_message)
  #box.askokcancel("OK/Cancel", the_message)
  #box.askyesnocancel("Option", the_message)
  #box.askretrycancel("R/C",the_message)

#Procedure to quit the program
def quit_prog():
  quit()

#Procedure to use buttons onClick event
def click_buttons():
  #entry box
  entry=Entry(window)
  entry.place(x=100, y=200)
  #create a log in button
  btn_login=Button(window, text="log in", command=lambda:display_message("User: " + entry.get() + " is Authorized"))
  btn_login.place(x=105, y=230)
  #this is to quit the program
  btn_quit=Button(window, text="Quit", command=quit_prog)
  btn_quit.place(x=250, y=500)

#Main programme
display_window("500x600","interface Test")
display_label(80, 150, "Enter login name")
#display_message("This is some message")
click_buttons()
#if not using IDLE
window.mainloop()