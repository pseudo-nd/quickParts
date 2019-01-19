#quickParts.py
#!/usr/bin/env python
#!C:\Python27\python.exe
# -*- coding: utf-8 -*-
import camelot
import jdfilters

def makelabels():

    tables = camelot.read_pdf('https://jdparts.deere.com/partsmkt/document/english/checklst/9070STScombine_filters_links.pdf')

    tables.export('70seriescombine.csv', f='csv', compress=True) # json, excel, html
    tables[0]
    print('Sending to Excel Spreadsheet....')

    
    tables[0].parsing_report
{
    'accuracy': 99.02,
    'whitespace': 12.24,
    'order': 1,
    'page': 1
}
