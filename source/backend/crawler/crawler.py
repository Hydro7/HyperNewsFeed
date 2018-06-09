from datetime import datetime

from bs4 import BeautifulSoup
import urllib.request
from database.news_post import NewsPost
from database.news_database import NewsDatabase

db = NewsDatabase('database/prod.db')

def url_crawler(url, company, address):
    try:
        res = urllib.request.urlopen(url, )
        soup = BeautifulSoup(res.read(), "html.parser")
        for a in soup.findAll('a'):
            l = a.get('href')
            #print(l)
            if(l):
                if('nieuws' in l or 'Nieuws' in l or 'news' in l or 'News' in l):
                    article_crawler(l, company, address)
    except:
        pass


def article_crawler(url, company, address):
    try:
        res = urllib.request.urlopen(url)
        soup = BeautifulSoup(res.read(), "html.parser")
        max1 = 0
        paragraph = 0
        for a in soup.findAll('article'):
            for p in a.findAll('p'):
                size = len(p.text)
                if size > max1:
                    max1 = size
                    paragraph = p.text
        if paragraph != 0:
            np = NewsPost('blah', paragraph, datetime.now(), company, address)
            db.store_news_post(np)
            print('Saved news post.')
    except:
        pass

