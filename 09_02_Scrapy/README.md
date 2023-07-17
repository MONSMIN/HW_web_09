## Скрапінг цитат зі сайту quotes.toscrape.com

Цей скрипт використовує фреймворк Scrapy для скрапінгу веб-сайту quotes.toscrape.com та отримання цитат та даних про авторів. Отримані дані зберігаються у форматі JSON у двох окремих файлах: quotes.json (з інформацією про цитати) та authors.json (з інформацією про авторів).

## Вимоги

Перед використанням скрипту, переконайтеся, що ви маєте наступні залежності встановлені:

- Python 3.10
- Scrapy (встановлення: `pip install scrapy`)

## Використання

1. Запустіть скрипт `main.py` для початку процесу скрапінгу. Скрипт автоматично перейде на веб-сайт quotes.toscrape.com та почне збирати дані про цитати та авторів.

2. Після завершення скрапінгу, у вас будуть створені два JSON-файли:
   - `quotes.json`: містить інформацію про всі цитати зі сторінок сайту.
   - `authors.json`: містить інформацію про авторів цитат.

3. Ви можете використовувати ці файли для подальшого аналізу даних, імпорту до бази даних або використання у своєму проекті.

## Структура проекту

- `spiders/get_urls_spider.py`: містить паука Scrapy для скрапінгу цитат та даних про авторів.
- `pipelines.py`: визначає пайплайн Scrapy для обробки отриманих елементів та збереження їх у JSON-файлах.
- `items.py`: визначає класи `QuoteItem` та `AuthorItem` для відповідних елементів даних.
- `main.py`: виконує процес скрапінгу за допомогою Scrapy.


# English ver.

## Scraping Quotes from quotes.toscrape.com

This script uses the Scrapy framework to scrape the website quotes.toscrape.com and retrieve quotes and author information. The obtained data is stored in JSON format in two separate files: quotes.json (containing information about quotes) and authors.json (containing information about authors).

## Requirements

Before running the script, make sure you have the following dependencies installed:

- Python 3.10
- Scrapy (installation: `pip install scrapy`)

## Usage

1. Run the `main.py` script to start the scraping process. The script will automatically navigate to the quotes.toscrape.com website and begin gathering data about quotes and authors.

2. After the scraping process is complete, you will have two JSON files created:
   - `quotes.json`: contains information about all the quotes from the website pages.
   - `authors.json`: contains information about the authors of the quotes.

3. You can use these files for further data analysis, importing into a database, or using in your own project.

## Project Structure

- `spiders/get_urls_spider.py`: contains the Scrapy spider for scraping quotes and author data.
- `pipelines.py`: defines the Scrapy pipeline for processing the extracted items and saving them in JSON files.
- `items.py`: defines the `QuoteItem` and `AuthorItem` classes for the corresponding data items.
- `main.py`: executes the scraping process using Scrapy.



