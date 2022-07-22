from gettext import find
from ...models import Headline
from bs4 import BeautifulSoup
import requests

def business(per_site):
    
    bus_html = requests.get('https://www.inshorts.com/en/read/business').text
    soup = BeautifulSoup(bus_html, 'lxml')

    bus_list = soup.find_all(class_='news-card')

    bus_count = 0
    for art in bus_list:
        if bus_count < per_site:
            headline = Headline()
            headline.leaning = 'left'
            headline.title = art.find(class_='news-card-title').find('a').text
            headline.img = art.find(class_='news-card-image')['style'].split("'")[1]
            # headline.url = art.find(class_='read-more').find('a').get('href')
            headline.content = art.find(class_='news-card-content').find('div').text
            headline.date = art.find(clas='date').text

            headline.save()
            bus_count += 1





