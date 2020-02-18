# -*- coding: utf-8 -*-
#!/usr/bin/env python
#!C:\Python37_64\python.exe
#gui.py
import quickParts
import tkinter as tk

def app_question(question):
    app_inside_question = input('Do you really want to open the Application???:   ')
   
    while True:
        try:

            if app_inside_question.casefold() == "yes":
                class App(tk.Frame):
                    def __init__(self):
                        super(App, self).__init__()
                        self.widgets={}
                        self.grid(column=4, row=4)

                    # create the application
                myapp = App()

                #
                # here are method calls to the window manager class
                #
                myapp.master.title("QuickParts App")
                myapp.master.maxsize(1000, 400)

                # start the program
                myapp.mainloop()

            
            elif app_inside_question.casefold() == "no":
                quickParts()

        except:
            print("Some error Chad has not thought of occurred....please due tell!")

        break
    quickParts.answer()




