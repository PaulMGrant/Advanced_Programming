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

#procedure to display list boxes
#def list_box():
  #create list box
  #listbox=Listbox(window)
  #listbox.insert(1, "Lexmoto")
  #listbox.insert(2, "BMW")
  #listbox.insert(3, "Indian")
  #listbox.insert(4, "Royal Enfield")
  #listbox.insert(5, "Harley Davidson")
  #listbox.place(x=400, y=50)
  #btn_list=Button(window, text="Press Me", command=lambda: display_message("Choice:" +listbox.get(listbox.curselection())))
  #btn_list.place(x=550, y=80)

#Procedure to display Radio buttons
#def radio_buttons():
  #create a string variable to store the pressed button
  #book_name=StringVar()
  #create the radio buttons
  #radio1=Radiobutton(window, text="HTML5", variable=book_name, value="HTML in easy steps")
  #radio2=Radiobutton(window, text="Python", variable=book_name, value="Python for beginners")
  #radio3=Radiobutton(window, text="Java", variable=book_name, value="Java for android")
  #radio4=Radiobutton(window, text="SQL", variable=book_name, value="Advanced SQL")
  #default button needs to be selected
  #radio1.select()
  #radio1.place(x=50, y=50)
  #radio2.place(x=50, y=75)
  #radio3.place(x=50, y=100)
  #radio4.place(x=50, y=125)
  #add a clickable button
  #btn_list=Button(window, text="Books", command=lambda: display_message("Selection: " + book_name.get()))
  #btn_list.place(x=150, y=50)

#procedure for check boxes
def check_boxes():
  #create intergers for storing the selection
  var1=IntVar()
  var2=IntVar()
  var3=IntVar()
  var4=IntVar()
  #create the check boxes
  item1=Checkbutton(window, text = "apples", variable=var1, onvalue=1, offvalue=0)
  item2=Checkbutton(window, text = "Pear", variable=var2, onvalue=1, offvalue=0)
  item3=Checkbutton(window, text = "Pineapple", variable=var3, onvalue=1, offvalue=0)
  item4=Checkbutton(window, text = "Oranges", variable=var4, onvalue=1, offvalue=0)

#place the check buttons
item1.place(x=200, y=300)
item2.place(x=200, y=325)
item3.place(x=200, y=350)
item4.place(x=200, y=375)

#add a button
btn=Button(window, text="Fruit", command=lambda: checked_items(var1, var2, var3, var4))
btn.place(x=200, y=375)

#checked items procedure for check boxes
def checked_items(v1, v2, v3, v4)
  str_msg="you chose: "
  if v1.get()==1:
  str_msg=str_msg+"/nApples"
    if v1.get()==1:
  str_msg=str_msg+"/nPear"
    if v1.get()==1:
  str_msg=str_msg+"/nPineapple"
    if v1.get()==1:
  str_msg=str_msg+"/nOranges"
#Main programme
display_window("500x600","interface Test")
display_label(80, 150, "Enter login name")
#display_message("This is some message")
click_buttons()
#list_box()
#radio_buttons()
check_boxes()
#if not using IDLE
window.mainloop()