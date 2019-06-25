# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 22:08:03 2019

@author: Aaga
"""
import urllib 
import pickle

project = open('hrefs-to-project-details.pickle', 'rb')
hrefs = pickle.load(project)
project.close()

import os
#os.mkdir('./xml')
i = 1
for p in project_data:        
    file=urllib.request.urlopen('https://repository.jpostdb.org' + p)
    data=file.read()
    file.close()
    output =  '.' + p
    print(i,'=',output)
    i = i + 1
    filehandle = open(output,'wb')
    filehandle.write(data)
    filehandle.close()

    
    