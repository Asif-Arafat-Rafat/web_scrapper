import requests
from bs4 import BeautifulSoup

url='https://www.discudemy.com/language/english/114'
response=requests.get(url)
soup=BeautifulSoup(response.text,"lxml")
desc=soup.find_all('section',class_='card')
i=1
for d in desc:
    name= d.find('div',class_='header')
    price= d.find_all('span',style="float:right;font-size: 20px;")
    link = d.find('a',class_='card-header')
    clink=link['href'] if link else ''
    if(name and price and clink):
        print(f"\n\n\n\nCourse No:{i}")
        i=i+1
        print(name.text)
        for p in price:
            print(p.text)
        print(clink)