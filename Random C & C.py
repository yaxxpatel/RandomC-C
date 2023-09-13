# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 13:09:21 2023

@author: admin
"""

from tkinter import *
import random

root = Tk()
root.title("Random City and Country")
root.geometry("500x500")

enter_name_country = Entry(root)
enter_name_country.place(relx= 0.5, rely= 0.2, anchor= CENTER)

country_list = Label(root)
random_number_label = Label(root)
selected_country = Label(root)

list1 = []

def addCountry():
    country_name = enter_name_country.get()
    list1.append(country_name)
    country_list["text"] = " Selected Country List : " + str(list1)
    
def 
    
    
    country_list.place(relx = 0.5, rely = 0.5, anchor = CENTER)
root.mainloop()