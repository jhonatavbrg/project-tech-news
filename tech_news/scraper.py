import requests
from bs4 import BeautifulSoup
import time


def fetch(url):
    time.sleep(1)
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        html = requests.get(url, headers=headers, timeout=3)
        if html.status_code == 200: 
            return html.text

    except:
        return None 

def scrape_novidades(html_content):
    """Seu código deve vir aqui"""

# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
