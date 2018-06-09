from crawler.crawler import url_crawler
from dataInterperter import get_data_set

def start():
    list = get_data_set()
    for i in list:
        sub = ""
        if i.subdomain:
            sub = i.subdomain + "."
        if i.SSL_certificate == "Yes":
            url_crawler("https://" + sub + i.domain)
        else:
            url_crawler("http://" + sub + i.domain)

start()