#misc.py
# -*- coding: utf-8 -*-
import sys
import webbrowser
import quickParts

global answer

def misc_question(answer):
    print('Searching through alot of indexes....' +answer)
    print('----------------------------------')
    print('Found....--> ' +answer)
    print('Sent to browser....')
    print('----------------------------------')
    while True:
        try:
                    #--------------------------------
                    #start of Catalogs
                    #--------------------------------               

                    #John Deere Misc Catalogs
                    #if-else loop filter/capacities
            if answer.lower() == "new business band connector":
                webbrowser.open('')
        except:
            print("Some error Chad has not thought of occurred....please due tell!")
        break
    quickParts.answer()