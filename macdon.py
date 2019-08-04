# -*- coding: utf-8 -*-
#!/usr/bin/env python
#!C:\Python37_64\python.exe
#quickParts.py
import sys
import webbrowser
import quickParts

global answer

def macdon_question(answer):
    print('Searching for catalogs....' +answer)
    print('----------------------------------')
    print('Found....--> ' +answer)
    print('Sent to browser....')
    print('----------------------------------')
    while True:
        try:
                    #--------------------------------
                    #start of Macdon
                    #--------------------------------               

                    #Macdon Quick
                    #if-else loop filter/capacities
            if answer.casefold() == "macdon":
                webbrowser.open('http://portal.macdon.com/')

            if answer.casefold() == "macdon knifes":
                webbrowser.open("https://1drv.ms/b/s!AiooZ5RuTuwkhMtk_Grv-78JL8lDNA?e=JgFidv")

            if answer.casefold() == "macdon maintenance":
                webbrowser.open("https://1drv.ms/b/s!AiooZ5RuTuwkhMtlbfyhskscmZXHUg?e=P50aEp")

            if answer.casefold() == "macdon compatibility":
                webbrowser.open("https://1drv.ms/b/s!AiooZ5RuTuwkhqYDqI2L_ul2CbLXvA")

        except:
            print("Some error Chad has not thought of occurred....please due tell!")
        break
    quickParts.answer()