from datetime import datetime

from bs4 import BeautifulSoup
import urllib.request
from database.news_post import NewsPost
from database.news_database import NewsDatabase

db = NewsDatabase('database/prod.db')


def url_crawler(url, company, address, icon_url):
    try:
        res = urllib.request.urlopen(url, )
        soup = BeautifulSoup(res.read(), "html.parser")
        for a in soup.findAll('a'):
            l = a.get('href')
            #print(l)
            if(l):
                if('nieuws' in l or 'Nieuws' in l or 'news' in l or 'News' in l):
                    article_crawler(l, company, address, icon_url)
    except:
        pass


def article_crawler(url, company, address, icon_url):
    try:
        res = urllib.request.urlopen(url)
        soup = BeautifulSoup(res.read(), "html.parser")
        max1 = 0
        par = 0
        for a in soup.findAll('article'):
            for p in a.findAll('p'):
                size = len(p.text)
                if size > max1:
                    max1 = size
                    par = p
        if par != 0:
            title = par.parent.parent.find('h2').text
            cnt = 0
            reached = 0
            temp_title = ""
            for c in title:
                if cnt > 3 and reached != 0:
                    break
                if ord(c) == 9 or ord(c) == 13:
                    continue
                if c == " ":
                    if cnt == 0:
                        temp_title = temp_title + " "
                    cnt += 1
                else:
                    temp_title = temp_title + c
                    reached = 1
                    cnt = 0
            if not title:
                temp_title = ""
            print(temp_title)
            np = NewsPost(temp_title, par.text, datetime.now(), company, address, icon_url)
            db.store_news_post(np)
            print('Saved news post.')
    except:
        pass