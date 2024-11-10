import requests
from bs4 import BeautifulSoup

url='https://www.startech.com.bd/lenovo-ideapad-slim-3-15abr8-ryzen-7-7730u-arctic-grey-15-6-inch-fhd-laptop'
response=requests.get(url)
soup=BeautifulSoup(response.text,"lxml")
print(soup.find_all('table')[1])