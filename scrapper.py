import requests
from bs4 import BeautifulSoup

url='https://www.discudemy.com/language/english/'
response=requests.get(url)
soup=BeautifulSoup(response.text,"lxml")
desc=soup.find_all('section',class_='card')
i=1
for d in desc:
    name= d.find('div',class_='header')
    price= d.find_all('span',style="float:right;font-size: 20px;")
    link = d.find('a',class_='card-header')
    clink=link['href'] if link else ''
    if clink:
        nresp=requests.get(clink)
    if(nresp.status_code==200):
        nsoup=BeautifulSoup(nresp.text,'lxml')
        nlink= nsoup.find('a',class_="ui big inverted green button discBtn")
        response=requests.get(nlink['href'])
        soup=BeautifulSoup(response.text,'lxml')
        link=soup.find('div',class_="ui segment")
        link=link.find('a')
    if(name and price and clink):
        print(f"\n\n\n\nCourse No:{i}")
        i=i+1
        print(name.text)
        for p in price:
            print(p.text)
        print(f'{link['href']} and {len(link)}') if nlink else ''

