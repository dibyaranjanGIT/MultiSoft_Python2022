from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
a_tag = soup.findAll(class_="titleline")
# print(a_tag)
for items in soup.findAll(class_="titleline"):
    print(items.getText())
    hreffing = items.find(name="a")
    print(hreffing.get("href"))

    score = soup.find(class_="score")
    print(score.getText())

    print("=====")

article_text = [item.getText() for item in soup.findAll(class_="titleline")]
print(article_text)