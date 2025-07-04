import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

top_books = []
for book in books:
    rating = book.p.find("star-rating")
    if "Five" in book.p["class"]:
        title = book.h3.a["title"]
        top_books.append(title)

with open("top_books.txt", "w", encoding="utf-8") as file:
    for title in top_books:
        file.write(title + "\n")
