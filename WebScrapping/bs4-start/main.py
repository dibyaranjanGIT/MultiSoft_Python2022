from bs4 import BeautifulSoup
# import lxml

with open("website.html", mode="r", encoding="utf8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
#
# print("========")
#
# all_anchor_tags = soup.find_all(name='a')
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.get("href"))
#
# for tag in all_anchor_tags:
#     print(tag.getText())
#
# print("========")
#
# heading = soup.find(name='h1', id='name')
# print(heading)
#
# print("========")
#
# class_heading = soup.find(name='h3', class_='heading')
# print(class_heading.get_text())
#
# print("========")
#
# h3_heading = soup.find_all(name="h3", class_="heading")
# print(h3_heading)
#
# name = soup.select_one(selector="p a")
# print(name)
#
#
# name = soup.select_one(selector="#name")
# print(name)
#
heading = soup.select(selector='.heading')
print(heading)