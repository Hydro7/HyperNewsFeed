from bs4 import BeautifulSoup
import urllib.request
from source.backend.dataInterperter import get_data_set

def urlCrawler(url):
    try:
        res = urllib.request.urlopen(url)
        soup = BeautifulSoup(res.read(), "html.parser")
        for a in soup.findAll('a'):
            l = a.get('href')
            #print(l)
            if(l):
                if('nieuws' in l or 'Nieuws' in l or 'news' in l or 'News' in l):
                    articleCrawler(l)
    except:
        pass


def articleCrawler(url):
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


list = get_data_set()
for i in list:
    sub = ""
    if i.subdomain:
        sub = i.subdomain + "."
    if i.SSL_certificate == "Yes":
        #print ("https://" + sub + i.domain)
        urlCrawler("https://" + sub + i.domain)
    else:
        #print("http://" + sub + i.domain)
        urlCrawler("http://" + sub + i.domain)
#print(parsed_html.body.find('div', attrs={'class':'container'}).text)