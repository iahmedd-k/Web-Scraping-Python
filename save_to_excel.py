import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "http://books.toscrape.com/"

response = requests.get(URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
books = soup.select("article.product_pod")

data = []
for book in books:
    title = book.h3.a["title"]
    price = book.select_one("p.price_color").text.strip()
    data.append({"Title": title, "Price": price})

# Export to Excel
df = pd.DataFrame(data)
df.to_excel("books.xlsx", index=False)
print(f"📁 Saved {len(data)} books to books.xlsx")
