#Title: Currency Convertor
#Author: Paul Grant
#Date: 22/09/2025
#Description: Program to convert currencies

#Note: PEP8 Standards

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