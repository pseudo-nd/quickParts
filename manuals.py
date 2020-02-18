# -*- coding: utf-8 -*-
#!/usr/bin/env python
#!C:\Python37_64\python.exe
#misc.py
import sys
import os
import webbrowser
import quickParts

def manuals_question(answer):
    print('Searching through alot of indexes....' +answer)    
    print('----------------------------------')
    print('Found manual....--> ' +answer)    
    print('----------------------------------')  

    while True:        
        try:
            
            #MACON Self-Propelled Windrowers
            if answer.casefold() == "m1240 manual":
                webbrowser.open('https://www.macdon.com/images/parts_catalogues/M1240_PC_214384_RevA.pdf')

            if answer.casefold() == "m1170 manual":
                webbrowser.open('https://www.macdon.com/images/parts_catalogues/M1170_PC_214387_RevA.pdf')

            if answer.casefold() == "m155e4 manual":
                webbrowser.open('https://www.macdon.com/images/parts_catalogues/M155E4_PC_214295_RevA.pdf')

            if answer.casefold() == "m205 manual":
                webbrowser.open('https://www.macdon.com/images/parts_catalogues/M205_PC_147956_RevA.pdf')
                
            if answer.casefold() == "m105 manual":
                webbrowser.open('https://www.macdon.com/images/parts_catalogues/M105_PC_169891_RevB.pdf')

            if answer.casefold() == "m150 manual":
                webbrowser.open('https://www.macdon.com/images/parts_catalogues/M150-M200-Parts-Catalog-Rev-C.pdf')

            if answer.casefold() == "m200 manual":
                webbrowser.open('https://www.macdon.com/images/parts_catalogues/M150-M200-Parts-Catalog-Rev-C.pdf')
  
            if answer.casefold() == "m100 manual":
                webbrowser.open('https://www.macdon.com/images/parts_catalogues/M100-Parts-Catalog-Model-Year-2010.pdf')

            if answer.casefold() == "9250 manual":
                webbrowser.open('https://www.macdon.com/images/parts_catalogues/9350-9352-9352i_-9352c_PC_46583_Iss_April_2009_Web_Update_Jan_2012.pdf')

            if answer.casefold() == "9350 manual":
                webbrowser.open('https://www.macdon.com/images/parts_catalogues/9350-9352-9352i_-9352c_PC_46583_Iss_April_2009_Web_Update_Jan_2012.pdf')
                
            if answer.casefold() == "9352 manual":
                webbrowser.open('https://www.macdon.com/images/parts_catalogues/9350-9352-9352i_-9352c_PC_46583_Iss_April_2009_Web_Update_Jan_2012.pdf')

            if answer.casefold() == "9352i manual":
                webbrowser.open('https://www.macdon.com/images/parts_catalogues/9350-9352-9352i_-9352c_PC_46583_Iss_April_2009_Web_Update_Jan_2012.pdf')
                
            if answer.casefold() == "9000 manual":
                webbrowser.open('https://www.macdon.com/images/parts_catalogues/9000_PC_46062_Issue_03-99.pdf')

            if answer.casefold() == "7000 manual":
                webbrowser.open('https://www.macdon.com/images/parts_catalogues/12910_7000_SP_Parts_Catalog.pdf')
                
            if answer.casefold() == "":
                webbrowser.open('')

            if answer.casefold() == "":
                webbrowser.open('')
                
            if answer.casefold() == "":
                webbrowser.open('')

            if answer.casefold() == "sprayer manual":
                webbrowser.open('https://jdparts.deere.com/partsmkt/document/english/featbene/76794_JD_SprayerPartsCatalog.pdf')
                
                
        except:
            print("Some error Chad has not thought of occurred....please due tell!")
        break
    quickParts.answer(
