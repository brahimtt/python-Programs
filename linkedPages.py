import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_linked_pages(url):
    r=requests.get(url)
    if r.status_code==200:
        soup=BeautifulSoup(r.content,'html.parser')
        links=soup.find_all('a',href=True)
        for link in links:
            linked_url=urljoin(url,link['href'])
            linked_response=requests.head(linked_url)
            if linked_response.status_code==404:
                print('broken link : %s' % linked_url )
            else:
                download_linked_pages(linked_url)
                print('downloading page of url:%s' % linked_url)
download_linked_pages('https://www.winnyskill.com')
