from bs4 import BeautifulSoup
import requests
import datetime

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/"
                        "features/best-movies-2/")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")

title = soup.findAll(name="h3", class_="title")
print("Started ..")
start = datetime.datetime.now()
for item in title:
    try:
        with open("Top100Movies.txt", mode="a", encoding="utf-8") as file:
            file.write(f"{item.getText()}\n")
    except FileNotFoundError:
        with open("Top100Movies.txt", mode="w", encoding="utf-8") as file:
            file.write(f"{item.getText()}\n")

end = datetime.datetime.now()
time_take = (end-start) / 60
print("Done ..")
print(f"Took {time_take} mins")
