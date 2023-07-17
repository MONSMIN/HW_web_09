import json
import requests

from bs4 import BeautifulSoup
from pprint import pprint
from urllib.parse import urljoin

base_url = "http://quotes.toscrape.com/"


def get_urls():
    urls = []
    next_url = "/"

    while next_url:
        url = urljoin(base_url, next_url)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        author_links = soup.select("div.quote span > a[href^='/author/']")
        next_page_link = soup.find("li", class_="next")

        for author_link in author_links:
            author_url = urljoin(base_url, author_link["href"])
            urls.append(author_url)

        if next_page_link:
            next_url = next_page_link.find("a")["href"]
        else:
            next_url = None

    return urls


def get_quotes():
    quotes = []
    next_url = "/"
    while next_url:
        url = base_url + next_url
        html_doc = requests.get(url)
        soup = BeautifulSoup(html_doc.text, 'html.parser')
        content = soup.select("div.quote")

        for quote in content:
            quote_data = {
                "tags": [tag.text for tag in quote.select("a.tag")],
                "author": quote.select_one("small.author").text,
                "quote": quote.select_one("span.text").text
            }
            quotes.append(quote_data)

        next_page_link = soup.find("li", class_="next")
        if next_page_link:
            next_url = next_page_link.find("a")["href"]
        else:
            next_url = None

    return quotes


def get_authors(url):
    authors_data = []
    html_doc = requests.get(url)
    soup = BeautifulSoup(html_doc.text, "html.parser")
    author_name = soup.select_one("h3.author-title").get_text(strip=True)
    born_date = soup.select_one("span.author-born-date").get_text(strip=True)
    born_location = soup.select_one("span.author-born-location").get_text(strip=True)
    description = soup.select_one("div.author-description").get_text(strip=True)

    author_data = {
        "fullname": author_name,
        "born_date": born_date,
        "born_location": born_location,
        "description": description
    }
    authors_data.append(author_data)

    return authors_data


def main(urls):
    data = []
    for url in urls:
        data.extend(get_authors(url))

    return data


def save_data(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    urls = get_urls()
    result = main(urls)
    pprint(result)
    save_data(result, 'authors.json')
    print("*50")
    pprint("The file with authors is saved")
    print("*50")
    data_quotes = get_quotes()
    pprint(data_quotes)
    save_data(data_quotes, 'quotes.json')
    print("*50")
    pprint("The file with quotes is saved")
    print("*50")
