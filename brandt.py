# -*- coding: utf-8 -*-
#!/usr/bin/env python
#!C:\Python37_64\python.exe
#quickParts.py
import sys
import webbrowser
import quickParts

global answer

def brandt_question(answer):
    print('Searching for catalogs....' +answer)
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
            if answer.casefold() == "brandt":
                webbrowser.open('https://www.brandt.ca/ageorder/')

        except:
            print("Some error Chad has not thought of occurred....please due tell!")
        break
    quickParts.answer()
