#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 12:28:01 2019

@author: rintu and aagam
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

def extract_id_value_with_Species(tagName,doc):
     tagName = 'Species'
     y= doc.getElementsByTagName(tagName)[0].childNodes[1].childNodes
     tagName_id=y.attributes.get('id').value
     tagName_val=y.attributes.get('value').value
     tagName_out={'id': tagName_id, 'value': tagName_val}
     return tagName_out
    
    

# not working for other tags 
# fix it
def extract_id_value_with_Instrument(tagName,doc):
    tagName = 'Instrument'
    y=doc.getElementsByTagName(tagName)[0].childNodes[1].childNodes
    tagName_id=y.attributes.get('id').value
    tagName_val=y.attributes.get('value').value
    tagName_out={'id': tagName_id, 'value': tagName_val}
    return tagName_out
"""
def extract_id_value_with_Modification(tagName,doc):
    tagName= 'Modification'
    ele=[]
    for num in range(0,8):
        if num % 2 != 0:
            ele.append(doc.getElementsByTagName(tagName)[0].childNodes[num].childNodes)
            tagName_id=ele.attributes.get('id').value
            tagName_val=ele.attributes.get('value').value
            tagName_out={'id': tagName_id, 'value': tagName_val}
    return tagName_out
"""            
def extract_id_value_with_FileList(tagName,doc):
    tagName= 'FileList'
    el=[]
    for n in range(0,18):
        if n % 2!=0:
            el.append(doc.getElementsByTagName(tagName)[0].childNodes[n].childNodes)
            tagName_id=el.attributes.get('id').value
            tagName_out={'id': tagName_id}
    return tagName_out
    
    

# Modification
# FileList