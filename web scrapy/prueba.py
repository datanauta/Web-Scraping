import requests
from bs4 import BeautifulSoup

url = 'https://es.wikipedia.org/wiki/Wikipedia:Qué_es_un_artículo_destacado'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

features_section = soup.find('div',{'class': 'mw-body-content'})

featured_list = features_section.find_all('li')

for article in featured_list[0:10]:
    title = article.text.strip()
    print(title)

burger_link = featured_list[0].find('a')['href']

print(burger_link)


