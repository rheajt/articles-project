import requests
import json
from bs4 import BeautifulSoup

def search_request(search_string):
    search_string = search_string.replace(' ', '%20')
    api = 'zsPq6ggkKM6bJ8BhES4oui9ZBeg_'
    search = requests.get('http://www.faroo.com/api?q='+search_string+'&start=1&length=10&l=en&src=news&i=false&f=json&key='+api)
    search_json = search.json()
    results = search_json['results']
    return results

def scrape_site(url):
    url_html = requests.get(url)
    site_soup = BeautifulSoup(url_html.text)
    body_text = site_soup.find_all('p')


    return body_text
