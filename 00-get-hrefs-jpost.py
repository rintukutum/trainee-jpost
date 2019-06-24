import time
from selenium import webdriver
import lxml.html as html
# from selenium.webdriver.common.Keys import Keys
#-----------
#Aagam Mishra
#-----------
def extract_tb(page_source):
    page_content=html.document_fromstring(page_source)
    table = page_content.getchildren()[1].getchildren()[13].getchildren()[2].getchildren()[4].getchildren()[8].getchildren()[1].getchildren()
    href = []
    for number in range(0,40):
        if number % 2 == 0:
            href.append(table[number].getchildren()[0].getchildren()[0].get('href'))
    return href


driver = webdriver.Firefox()
time.sleep(5)
jpost_href = []
for i in range(1,15):
   if i==1:
      driver.get('https://repository.jpostdb.org/')
      time.sleep(4)
      page_source=driver.page_source
      jpost_href.append(extract_tb(page_source))
   else:
      driver.find_element_by_xpath("//a[@data-page=%d]" % (i)).click()
      page_source=driver.page_source
      jpost_href.append(extract_tb(page_source))

hrefs=[]
for i in jpost_href:
    for j in i:
        hrefs.append(j)
        
import pickle
output = open('hrefs-jPOST.pickle','wb')
pickle.dump(hrefs,output)           
output.close()
             
