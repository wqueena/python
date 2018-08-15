from bs4 import BeautifulSoup
from urllib.request import urlopen

#import requests


def run(url):
    html_doc = urlopen(url)
    soup = BeautifulSoup(html_doc, 'lxml')
    t1 = soup.find_all('a')
    for t2 in t1:
        t3 = t2.get('href')
        print(t3)


if __name__ == '__main__':
    url = 'http://www.biqukan.com/1_1094/17930894.html'
    run(url)