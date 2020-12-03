import requests, csv

from bs4 import BeautifulSoup

response = requests.get('http://quotes.toscrape.com/', 'html.parser')
html_data = BeautifulSoup(response.text)
quotes = html_data.find_all(class_="quote")
with open('quotes.csv', 'w', encoding="utf8") as file:
    headers=['text', 'author', 'keywords']
    csw_writer = csv.DictWriter(file, fieldnames=headers, delimiter="|")
    for quote in quotes:
        csw_writer.writerow({
            'text': quote.find(class_="text").get_text(),
            'author': quote.find(class_="author").get_text(),
            'keywords': quote.find(class_="keywords")['content'],
        })

