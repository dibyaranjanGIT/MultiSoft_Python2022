import requests
from bs4 import BeautifulSoup

# Making a GET request
r = requests.get('https://dibyaranjangit.github.io/personal/')


# print(r.content)

# # Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
# print(soup)


# # Finding by id
mydivs = soup.find_all("div", {"class": "top"})
print(mydivs)


# # All the li under the above ul
# lines = soup.find_all('li')
#
# for line in lines:
#     print(line.text)