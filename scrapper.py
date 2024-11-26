import requests
from bs4 import BeautifulSoup
import re
import time as timeMod
def link_ext(url):
    info=[]
    response = requests.get(url)
    soup= BeautifulSoup(response.text,'lxml')
    link1= soup.find('a',class_='ui big inverted green button discBtn')
    response = requests.get(link1['href'])
    soup=BeautifulSoup(response.text,'lxml')

    link=soup.find('div',class_="ui segment")
    link=link.find('a')
    resp=requests.get(link['href'])
    timeMod.sleep(1)
    sup=BeautifulSoup(resp.text,'lxml')
    # timeMod.sleep(1)
    # time=sup.find_all('div',class_="course-landing-page__main-content" )
    # for t in time:
    #     print(t)
    #     timeMod.sleep(5)
    #     print("\n\n\n")
    uid=sup.find('body')
    uid=uid['data-clp-course-id']
    info={
        'uid':uid,
        'link':link['href'],
    }
    return info

def get_courses(i):
    courses=[]
    url=f'https://www.discudemy.com/language/english/{i if i > 1 else ''}'
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    desc=soup.find_all('section',class_='card')
    for d in desc:
        name= d.find('div',class_='header')
        price= d.find_all('span',style="float:right;font-size: 20px;")
        link = d.find('a',class_='card-header')
        image=d.find('div',class_='image')
        image=image.find('amp-img')['src'] if image else ''
        clink=link['href'] if link else ''
        for p in price:
            discounted=re.compile(r"\$\d+\s*->\s*\$0")
            hasDisc=any(discounted.search(p.text) for p in price)
        if(name and price and clink and hasDisc):  
            for p in price:
                price=p.text
            info=link_ext(clink)
            code=re.search('couponCode=(.*)',info['link']).group(1)
            code=(f"https://www.udemy.com/payment/checkout/express/course/{info['uid']}/?discountCode={code}")
            print(code)
            course={
                'name':name.text.strip(),
                'image':image,
                'price':price,
                'link':info['link'],
                'uid':info['uid'],
                'code':code
            }
            courses.append(course)
    return courses
for i in range(20):
    get_courses(i)