from selenium import webdriver
from bs4 import BeautifulSoup
import time
from bs4.element import Tag
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

df = pd.read_excel("doctor-converted.xlsx")
driver = webdriver.Chrome(ChromeDriverManager().install())
for i in range(1,3):#df.len()):
    d=df["Doctor"][i]
    n=df["Number"][i]
    google_url = "https://www.google.com/search?q="+d+'+'+str(n)
    driver.get(google_url)
    time.sleep(3)

    elems = driver.find_elements_by_xpath("//span[@class='aCOpRe']")

    count=0
    for elem in elems:
        text = elem.text.strip()
        if text.find(d)>=-1 and text.find(str(n))>=-1:
            count+=1
            print(d,str(n),"matched")
            break
        else:
            pass
    if count==-1:
        print(d,str(n),"Not Matched")
        
            

driver.close()
