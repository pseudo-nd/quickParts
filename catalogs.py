#catalogs.py
# -*- coding: utf-8 -*-
import sys
import webbrowser
import quickParts

global answer

def catalog_question(answer):
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
            if answer.lower() == "quick hitch catalog":

                webbrowser.open('https://jdparts.deere.com/partsmkt/document/english/checklst/1023E_1025R_1026R.pdf')

            if answer.lower()== "hose catalog":

                webbrowser.open("https://jdparts.deere.com/partsmkt/document/english/featbene/DKD1617HoseGuide06.pdf")

        except:
            print("Some error Chad has not thought of occurred....please due tell!")
        break
    quickParts.answer()