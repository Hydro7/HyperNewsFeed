from bs4 import BeautifulSoup
import urllib.request

def url_crawler(url):
    try:
        res = urllib.request.urlopen(url)
        soup = BeautifulSoup(res.read(), "html.parser")
        for a in soup.findAll('a'):
            l = a.get('href')
            #print(l)
            if(l):
                if('nieuws' in l or 'Nieuws' in l or 'news' in l or 'News' in l):
                    article_crawler(l)
    except:
        pass


def article_crawler(url):
    try:
        res = urllib.request.urlopen(url)
        soup = BeautifulSoup(res.read(), "html.parser")
        max1 = 0
        paragraph = 0
        #print(url)
        for a in soup.findAll('article'):
            for p in a.findAll('p'):
                size = len(p.text)
                if size > max1:
                    max1 = size
                    paragraph = p.text
        print(paragraph)
        print()
    except:
        pass

