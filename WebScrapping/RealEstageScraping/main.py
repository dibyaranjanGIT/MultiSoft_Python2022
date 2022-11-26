from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.pararius.com/apartments/amsterdam?ac=1"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('section', class_="listing-search-item")

with open('housing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Price', 'Desc']
    thewriter.writerow(header)
    # print(lists)
    for li in lists:
        title = li.find('a', class_="listing-search-item__link--title").text.replace('\n', '')
        # location = li.find('div', class_="listing-search-item__location").text.replace('\n', '')
        price = li.find('div', class_="listing-search-item__price").text.replace('\n', '')
        feature = li.find('div', class_="listing-search-item__features").text.replace('\n', '')

        info = [title, price, feature]
        thewriter.writerow(info)
