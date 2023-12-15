import time

from selenium import webdriver
from bs4 import BeautifulSoup

# driver = webdriver.Chrome()
# driver.get('https://s5.sir.sportradar.com/bet365/ja/1/season/93741/fixtures/round/21-27')
# time.sleep(5)

html = open('test.html')
soup = BeautifulSoup(html, 'html.parser')
elems = soup.select('tr.cursor-pointer')
print(len(elems))
for i in range(0, len(elems)):
    print(elems[i].get_text())
