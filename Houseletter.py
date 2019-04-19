import requests
from bs4 import BeautifulSoup
import sys
import datetime

payload = {'key': 'b5bde5d3527582e1bc8284c0a1a73720', 'url':
'https://www.lawrenceville.org/houseletter'}


def get_letter():
    resp = requests.get('http://api.scraperapi.com', params=payload)
    soup=BeautifulSoup(resp.text,'html.parser')
    # print soup

    items=soup.findAll("div",{"class":"event-detail"})
    items_list=[]

    for item in items:
        items_list.append(item.get_text().encode('utf-8'))
    # for item in items_list:
    #     print(item)
    return items_list
