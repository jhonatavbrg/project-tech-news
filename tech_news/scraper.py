import requests
from bs4 import BeautifulSoup
import time
from tech_news.database import create_news

from tech_news.aux_func import (
    get_title,
    get_timestamp,
    get_writer,
    get_shares,
    get_comments,
    get_summary,
    get_sources,
    get_categories,
)


def fetch(url):
    time.sleep(1)
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)"
            + "AppleWebKit/537.36 (KHTML, like Gecko)"
            + "Chrome/50.0.2661.102 Safari/537.36"
        }
        html = requests.get(url, headers=headers, timeout=3)

        if html.status_code == 200:
            return html.text

    except requests.ReadTimeout:
        return None


def scrape_novidades(html_content):
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        soup.prettify()

        news = list()
        for new in soup.find_all("div", {"class": "tec--list__item"}):
            news.append(
                new.find("a", {"class": "tec--card__thumb__link"})["href"]
            )

        return news

    except Exception:
        return []


def scrape_next_page_link(html_content):
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        soup.prettify()

        button_pagination = soup.find(
            "a",
            {
                "class": "tec--btn tec--btn--lg"
                + " tec--btn--primary z--mx-auto z--mt-48"
            },
        )["href"]

        return button_pagination

    except Exception:
        return None


def scrape_noticia(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    soup.prettify()
    links = list()
    new_dict = dict()

    links.append(soup.find("link", {"rel": "canonical"})["href"])

    for link in links:
        new_dict["url"] = link
        new_dict["title"] = get_title(soup)
        new_dict["timestamp"] = get_timestamp(soup)
        new_dict["writer"] = get_writer(soup)
        new_dict["shares_count"] = get_shares(soup)
        new_dict["comments_count"] = get_comments(soup)
        new_dict["summary"] = get_summary(soup)
        new_dict["sources"] = get_sources(soup)
        new_dict["categories"] = get_categories(soup)

    return new_dict


def get_amount_url(amount):
    html_content = fetch("https://www.tecmundo.com.br/novidades")
    urls_list = list()

    while len(urls_list) < amount:
        news = scrape_novidades(html_content)
        urls_list.extend(news)
        if len(urls_list) < amount:
            new_page = scrape_next_page_link(html_content)
            html_content = fetch(new_page)

    return urls_list[0:amount]


def get_tech_news(amount):
    urls_list = get_amount_url(amount)
    news_list = list()

    for url in urls_list:
        if len(news_list) < amount:
            fetch_html_content = fetch(url)
            new = scrape_noticia(fetch_html_content)
            news_list.append(new)

    create_news(news_list)

    return news_list
