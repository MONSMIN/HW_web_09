## Скрапінг цитат з сайту quotes.toscrape.com

Цей скрипт використовує бібліотеку BeautifulSoup для скрапінгу веб-сайту http://quotes.toscrape.com та отримання інформації про цитати та їх авторів. 


## Залежності

Перед використанням скрипту, переконайтеся, що ви імпортуєте наступні модулі:

- `json`: Модуль для роботи з форматом JSON.
- `requests`: Модуль для виконання HTTP-запитів.
- `BeautifulSoup` з бібліотеки `bs4`: Модуль для парсингу HTML-коду та витягування даних.
- `pprint` з модулю `pprint`: Модуль для красивого виводу даних.
- `urljoin` з модулю `urllib.parse`: Модуль для об'єднання URL-адреси з відносним посиланням.

```python 
 - import json 
 - import requests 
 - from bs4 import BeautifulSoup 
 - from pprint import pprint
 - from urllib.parse import urljoin
 ```

## Використання

1. Запустіть скрипт `main.py` для початку скрапінгу.
2. Скрипт автоматично перейде на веб-сайт quotes.toscrape.com та отримає інформацію про цитати та авторів.

3. Після виконання скрипту, у вас будуть створені два файли:
   - `quotes.json`: містить інформацію про всі цитати з усіх сторінок сайту.
   - `authors.json`: містить інформацію про авторів цитат.

# English ver.

## Scraping Quotes from quotes.toscrape.com

This script uses the BeautifulSoup library to scrape the website http://quotes.toscrape.com and retrieve information about quotes and their authors.

## Dependencies

Before using the script, make sure you import the following modules:

- `json`: Module for working with JSON format.
- `requests`: Module for executing HTTP requests.
- `BeautifulSoup` from the `bs4` library: Module for parsing HTML code and extracting data.
- `pprint` from the `pprint` module: Module for pretty-printing data.
- `urljoin` from the `urllib.parse` module: Module for joining a URL address with a relative link.

```python
import json
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from urllib.parse import urljoin
```

## Usage

1. Run the `main.py` script to start the scraping process.

2. The script will automatically navigate to the quotes.toscrape.com website and retrieve information about quotes and authors.

3. After the script finishes, two files will be created:

 - `quotes.json`: contains information about all the quotes from the website pages.
 - `authors.json`: contains information about the authors of the quotes.

