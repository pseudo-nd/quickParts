# -*- coding: utf-8 -*-
#!/usr/bin/env python
#!C:\Python37_64\python.exehow m
#quickParts.py
import sys
import os
import time
import webbrowser
import jdfilters
import catalogs
import misc
import app
import macdon

global question
global answer

def main():
        print('---------------------------------------------------------')
        print('        QuickParts! Find your part numbers by a keystroke')
        print('---------------------------------------------------------')
        answer()

def answer():
        try:
                question = input("How can I help you?: ")
                if 'filter'.casefold() in question:
                        ask_a_question(question)
                elif 'filters'.casefold() in question:
                        ask_a_question(question)
                elif 'catalog'.casefold() in question:
                        ask_a_question2(question)
                elif 'show'.casefold() in question:
                        ask_a_question3(question)
                elif 'what'.casefold() in question:
                        ask_a_question3(question)
                elif 'how'.casefold() in question:
                        ask_a_question3(question)
                elif 'app'.casefold() in question:
                        ask_a_question4(question)
                elif 'manual'.casefold() in question:
                        ask_a_question5(question)
                elif 'macdon'.casefold() in question:
                        ask_a_question6(question)
                elif 'brandt'.casefold() in question:
                        ask_a_question7(question)
                elif 'exit'.casefold() in question:
                        exit(question)
                

                
                        
        except:
                print("------------------------------------- \n[I do not understand that] \n-------------------------------------")
                answer()
        finally:
                answer()
        
def ask_a_question(answer):
                jdfilters.filter_question(answer)

def ask_a_question2(answer):
                catalogs.catalog_question(answer)

def ask_a_question3(answer):
                misc.misc_question(answer)

def ask_a_question4(answer):
                app.app_question(answer)

def ask_a_question5(answer):
                manuals.manuals_question(answer)

def ask_a_question6(answer):
                macdon.macdon_question(answer)

def ask_a_question7(answer):
                brandt.brandt_question(answer)

def exit(question):
        print("Exiting quickParts.....", question)
        time.sleep(1.5)
        os._exit(0)
        
if __name__ == "__main__":
        main()
