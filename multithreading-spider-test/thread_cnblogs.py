import requests
from random_ua import random_UA
from bs4 import BeautifulSoup
urls = [f'https://www.cnblogs.com/#p{page}' for page in range(1,21)]
headers = {'user-agent':random_UA().select_ua()}

def crawl(url):
    response = requests.get(url=url,headers=headers)
    return response.text

def parse(html):
    soup = BeautifulSoup(html,"html.parser")
    links = soup.find_all("a", class_="post-item-title")
    return [(link["href"],link.get_text()) for link in links]
