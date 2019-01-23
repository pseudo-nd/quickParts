#quickParts.py
#!/usr/bin/env python
#!C:\Python27\python.exe
# -*- coding: utf-8 -*-
import sys
import os
import time
import webbrowser
import jdfilters
import catalogs
import misc

global question
global answer

def main():
        print('---------------------------------------------------------')
        print('        QuickParts! Find your part numbers by a keystroke')
        print('---------------------------------------------------------')
        answer()

def answer():
        try:
                question = raw_input("How can I help you?: ")
                if 'filter'.lower() in question:
                        ask_a_question(question)
                elif 'filters'.lower() in question:
                        ask_a_question(question)
                elif 'catalog'.lower() in question:
                        ask_a_question2(question)
                elif 'how'.lower() in question:
                        ask_a_question3(question)
                elif 'what'.lower() in question:
                        ask_a_question3(question)
                elif 'show'.lower() in question:
                        ask_a_question3(question)
                elif 'exit'.lower() in question:
                        exit(question)
                else:
                        print('')
                        raise Exception("------------------------------------- \n[I do not understand that] \n-------------------------------------")
                        
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

def exit(question):
        print("Exiting quickParts.....", question)
        time.sleep(1.5)
        exit(question)
        
if __name__ == "__main__":
        main()