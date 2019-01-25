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
    print('----------------------------------')
    while True:
        try:
                    #--------------------------------
                    #start of Catalogs
                    #--------------------------------               

                    #John Deere Misc Catalogs
                    #if-else loop filter/capacities
            if answer.lower() == "what is the new business band connectors":
                print("57M7500", "4")
                print("57M7501", "4")
                print("57M7725", "1")
                print("57M7726", "1")
                print("57M8270", "1")
                print("57M8843", "1")

            elif answer.lower() == "how many disks on air drill":
                print("1870", "40ft", "40")
                print("1870", "56ft", "56")
                print("1890", "30ft @ 7.5in Spacing", "48")
                print("1890", "30ft @ 10in Spacing", "36")
                print("1890", "36ft @ 7.5in Spacing", "58")
                print("1890", "36ft @ 10in Spacing", "44")
                print("1890", "40ft @ 7.5in Spacing", "64")
                print("1890", "40ft @ 10in Spacing", "48")
                print("1890", "42ft @ 7.5in Spacing", "68")
                print("1890", "42ft @ 10in Spacing", "50")
                print("1890", "50ft @ 7.5in Spacing", "80")
                print("1890", "50ft @ 10in Spacing", "60")
                print("1890", "60ft @ 7.5in Spacing", "96")
                print("1890", "60ft @ 10in Spacing", "72")
                print("1895", "30ft @ 10in Spacing", "36")
                print("1895", "30ft @ 20in Spacing", "18")
                print("1895", "36ft @ 10in Spacing", "44")
                print("1895", "36ft @ 20in Spacing", "22")
                print("1895", "40ft @ 10in Spacing", "48")
                print("1895", "40ft @ 20in Spacing", "24")
                print("1895", "43ft @ 10in Spacing", "52")
                print("1895", "43ft @ 20in Spacing", "26")

            elif answer.lower() =="show me car batteries":
                webbrowser.open('https://jdparts.deere.com/partsmkt/document/english/featbene/DKB5066_Batteries_rvFNL_2.pdf')

            elif answer.lower() == "show me batteries":
                webbrowser.open('https://jdparts.deere.com/partsmkt/document/english/featbene/DKD1631BatteryGuide.pdf')

            elif answer.lower() == "what is the part number for proseries openers":
                print("AA97392", "8 rows (4right/4left)")
                print("AA98693", "2 rows (1right/1left)")

            elif answer.lower() == "what is the part number for proseries":
                print("AA97392", "8 rows (4right/4left)")
                print("AA98693", "2 rows (1right/1left)")

            elif answer.lower() == "what is good better best harvest parts":
                webbrowser.open('https://jdparts.deere.com/partsmkt/document/english/pmac/60130_PlatformWearParts.htm')
            elif answer.lower() == "gbb harvest":
                webbrowser.open('https://jdparts.deere.com/partsmkt/document/english/pmac/60130_PlatformWearParts.htm')

            elif answer.lower() == "how many guards on a header":
                print('600R', '600F', '900D')	
                print('Platform', 'Length',	'Number of Guards')
                print('15 ft',	'15 S/L/S', '15 L/S/L')
                print('18 ft',	'18 S/L/S', '18 L/S/L')
                print('20 ft',	'20 S/L/S', '20 L/S/L')
                print('22 ft',	'22 S/L/S', '22 L/S/L')
                print('25 ft',	'25 S/L/S', '25 L/S/L')
                print('30 ft',	'30 S/L/S', '30 L/S/L')
                print('35 ft',	'34 S/L/S', '34 L/S/L')
                print('36 ft',	'36 S/L/S', '36 L/S/L')
                print('--------------------------------')
                print('--------------------------------')
                print('200', '900', '900F', '900R')	
                print('Platform Length',	'Number of Guards')
                print('13 ft','                  ', '24')
                print('15 ft','                  ', '28')
                print('16 ft','                  ', '30')
                print('18 ft','                  ', '34')
                print('20 ft','                  ', '38')
                print('22 ft Rigid','            ', '42')
                print('22 ft Flex','             ', '39')
                print('24 ft','                  ', '46')
                print('25 ft','                  ', '49')
                print('30 ft','                  ', '58')
                print('--------------------------------')
                print('--------------------------------')



        except:
            print("Some error Chad has not thought of occurred....please due tell!")
        break
    quickParts.answer()