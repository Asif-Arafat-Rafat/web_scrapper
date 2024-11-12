import requests
from bs4 import BeautifulSoup

def link_ext(url):
    response = requests.get(url)
    soup= BeautifulSoup(response.text,'lxml')
    link1= soup.find('a',class_='ui big inverted green button discBtn')
    response = requests.get(link1['href'])
    soup=BeautifulSoup(response.text,'lxml')
    link=soup.find('div',class_="ui segment")
    link=link.find('a')
    print(link['href'])
i=1

j=1
run=0
url=f'https://www.discudemy.com/language/english/{i if i > 1 else ''}'
response=requests.get(url)
soup=BeautifulSoup(response.text,"lxml")
desc=soup.find_all('section',class_='card')
for d in desc:
    name= d.find('div',class_='header')
    price= d.find_all('span',style="float:right;font-size: 20px;")
    link = d.find('a',class_='card-header')
    image=d.find('img')
    image=image['src'] if image else ''
    clink=link['href'] if link else ''
    if(name and price and clink and price != "$0"):
        print(f"\n\n\n\nCourse No:{j}")
        j=j+1
        print(f"Name:{name.text}")
        print(f'Image:{image}') if image else d
        for p in price:
            print(p.text)
        link_ext(clink)        
