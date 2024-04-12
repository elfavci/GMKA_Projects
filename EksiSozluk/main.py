"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

url = " https://eksisozluk.com/mustafa-kemal-ataturk--34712"

browser.get(url)

time.sleep(5)

elements = browser.find_elements(By.CSS_SELECTOR,'.content')

for element in elements:
    print("***************")
    print(element.text)

browser.close()
"""
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import random

browser = webdriver.Chrome()

url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="

pageCount = 1
entries = []
entryCount = 1

while pageCount<=10:
    randomPage = random.randint(1,2361)
    newUrl = url + str(randomPage)
    browser.get(newUrl)
    elements =browser.find_elements(By.CSS_SELECTOR,'.content')
    for element in elements:
        entries.append(element.text)
    time.sleep(2)
    pageCount+=1

for entry in entries:
    print(str(entryCount) + "**********************")
    print(element.text)
    entryCount += 1
    
browser.close()
"""


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import random

browser = webdriver.Chrome()

url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="

pageCount = 1
entries = []
entryCount = 1

while pageCount<=10:
    randomPage = random.randint(1,2361)
    newUrl = url + str(randomPage)
    browser.get(newUrl)
    elements =browser.find_elements(By.CSS_SELECTOR,'.content')
    for element in elements:
        entries.append(element.text)
    time.sleep(2)
    pageCount+=1

with open("entries.txt", "w",encoding ="UTF-8") as file:
    for entry in entries:
        file.write(str(entryCount)+".\n"+ entry + "\n")
        file.write("******************\n")
        entryCount +=1
    

browser.close()





















