import requests
import json
from bs4 import BeautifulSoup
from settings import API

def search_request(search_string):
    search_string = search_string.replace(' ', '%20')
    api = API
    search = requests.get('http://www.faroo.com/api?q='+search_string+'&start=1&length=10&l=en&src=news&i=false&f=json&key='+api)
    search_json = search.json()
    results = search_json['results']
    return results

def scrape_site(url):
    url_html = requests.get(url)
    site_soup = BeautifulSoup(url_html.text)
    article_data = [site_soup.title.text]
    article_data.append(url)
    body_text = site_soup.find_all('p')
    page_text = ""
    for tag in body_text:
        page_text += tag.text
        page_text += "\n\n"
    article_data.append(page_text)
    return article_data