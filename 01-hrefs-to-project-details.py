from selenium import webdriver

import pickle
import lxml.html as html

hrefs = open('hrefs-jPOST.pickle', 'rb')
hrefs_data = pickle.load(hrefs)
hrefs.close()

driver = webdriver.Firefox()
xmls = []
for href in hrefs_data:
    webpage = 'https://repository.jpostdb.org/' + href
    driver.get(webpage)
    time.sleep(4)
    page_source=driver.page_source
    page_content=html.document_fromstring(page_source)
    t= page_content.getchildren()[1].getchildren()[13].getchildren()[2].getchildren()[0].getchildren()[3].getchildren()[0].getchildren()[11].getchildren()[1]
    xmls.append(t.getchildren()[0].get('href'))


import pickle
output2=open('hrefs-to-project-details.pickle','wb')
pickle.dump(xmls,output2)
output2.close()    
