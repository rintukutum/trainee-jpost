# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 20:21:03 2019

@author: Aaga
"""
import time
from selenium import webdriver

import pickle
import lxml.html as html

hrefs = open('hrefs-jPOST.pickle', 'rb')
hrefs_data = pickle.load(hrefs)
hrefs.close()

driver = webdriver.Firefox()
page_contents = []
for href in hrefs_data:
    webpage = 'https://repository.jpostdb.org/' + href
    driver.get(webpage)
    time.sleep(4)
    page_source=driver.page_source
    page_content=html.document_fromstring(page_source)
    page_contents.append(page_content)
     #xmls.append(t.getchildren()[0].get('href'))
   
    
def extract_href(x):
    tb = x.getchildren()[1].getchildren()[13].getchildren()[2].getchildren()[0].getchildren()[3].getchildren()[0].getchildren()
    # to find XML file
    idx = []
    i = 0
    for element in tb:
        out = element.getchildren()[0].text
        if out == 'XML file':
            idx.append(i)
        i = i + 1
    # href elemnt
    output = tb[idx[0]].getchildren()[1].getchildren()[0].get('href')
    return output


i = 0
xmls = []
for page in page_contents:
    print(i)
    xmls.append(extract_href(page))
    i = i + 1
    


import pickle
output2=open('hrefs-to-project-details.pickle','wb')
pickle.dump(xmls,output2)
output2.close()    
    
