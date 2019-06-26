#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 12:28:01 2019

@author: rintu
"""

# for reading and locating xml files 
import os

from xml.dom import minidom

xml_files = []
for (dirpath, dirname, filenames) in os.walk("./xml"):
    for filename in filenames:
        xml_file = ''.join([dirpath,'/',filename])
        print(xml_file)
        xml_files.append(xml_file)



doc = minidom.parse(xml_files[1])

def extract_id_value_with_tagName(tagName,doc):
    # tagName = 'Species'
    x = doc.getElementsByTagName(tagName)[0].childNodes    
    tagName_id = x.attributes.get('id').value
    tagName_val = x.attributes.get('value').value
    tagName_out = {'id': tagName_id, 'value': tagName_val}
    return tagName_out

extract_id_value_with_tagName('Species',doc)

# not working for other tags 
# fix it
extract_id_value_with_tagName('Instrument',doc)