from bs4 import BeautifulSoup
import requests

def run(url):
    req = requests.get(url)
    html_doc = req.text
    soup = BeautifulSoup(html_doc, 'lxml')
    texts = soup.find('div', class_='showtxt')
    text = texts.get_text()
    print(text)
    return texts


if __name__ == '__main__':
    url = 'http://www.biqukan.com/1_1094/17930894.html'
    run(url)