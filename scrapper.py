import requests
from bs4 import BeautifulSoup

url='https://www.discudemy.com/language/english'
response=requests.get(url)
soup=BeautifulSoup(response.text,"lxml")
print(soup.find_all('div',class_='description'))