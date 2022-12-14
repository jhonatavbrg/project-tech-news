from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    search_list = search_news({"title": {"$regex": title, "$options": "i"}})

    list_tuple = list()

    if search_list:
        list_tuple.append((search_list[0]["title"], search_list[0]["url"]))

    return list_tuple


def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    list_tuple = list()
    date_list_new = search_news({"timestamp": {"$regex": date}})

    if date_list_new:
        list_tuple.append((date_list_new[0]["title"], date_list_new[0]["url"]))

    return list_tuple


def search_by_source(source):
    search_list = search_news({"sources": {"$regex": source, "$options": "i"}})
    list_tuple = list()

    if search_list:
        list_tuple.append((search_list[0]["title"], search_list[0]["url"]))

    return list_tuple


def search_by_category(category):
    search_list = search_news(
        {"categories": {"$regex": category, "$options": "i"}}
    )
    list_tuple = list()

    if search_list:
        list_tuple.append((search_list[0]["title"], search_list[0]["url"]))

    return list_tuple
