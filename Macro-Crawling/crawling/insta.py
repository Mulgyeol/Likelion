from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import tkinter
from tkinter import filedialog
import pyautogui

baseURL = 'https://www.instagram.com/explore/tags/'
plusURL = pyautogui.prompt("검색할 태그를 입력해 주세요.")

root = tkinter.Tk()
root.withdraw()
folder = tkinter.filedialog.askdirectory(parent = root, initialdir="/", title = "Select Folder")

URL = baseURL + quote_plus(plusURL)

driver = webdriver.Chrome()
driver.get(URL)

time.sleep(3)

html  = driver.page_source
soup = BeautifulSoup(html)

insta = soup.select('.v1Nh3.kIKUG._bz0w')

print(insta[0])

n = 1
for i in insta:
#    print('https://www.instagram.com'+i.a['href'])
    imgURL = i.select_one('.KL4Bh').img['src']
    with urlopen(imgURL) as f:
        with open(folder + '/' +plusURL + str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    n += 1
#    print(imgURL)
#    print()
#    print(folder + plusURL + str(n) + '.jpg')

driver.close()