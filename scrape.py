# scrape everything from lexfridmanlibrary.com

from bs4 import BeautifulSoup
import requests

x = requests.get('https://www.lexfridmanlibrary.com/')
soup = BeautifulSoup(x.text, 'html.parser')

shows = soup.select('div.bg-white.p-10.rounded-lg')
for show in shows:
    for title in show.select('h3'):
        print()
        print(f'## {title.text}')
        print()

    for book in show.select('a'):
        link = book['href']
        for div in book.select('div > p.text-center'):
            print(f'* [{div.text}]({link})')
