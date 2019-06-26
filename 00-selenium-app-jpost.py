from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#------------
#
#------------
driver = webdriver.Firefox()

from lxml import html
for page in range(1,15):
    if page == 1:
        driver.get('https://repository.jpostdb.org')
    else:
        driver.find_element_by_xpath("//a[@data-page=%d]" %page).click()
    page_source = driver.page_source
	page_content = html.document_fromstring(page_source)
