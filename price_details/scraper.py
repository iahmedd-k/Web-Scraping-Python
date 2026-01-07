import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

URL = "https://books.toscrape.com/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

products = soup.select(".product_pod")

data = []

for product in products:
    name = product.h3.a["title"]
    price = product.select_one(".price_color").text
    availability = product.select_one(".availability").text.strip()
    link = product.h3.a["href"]

    data.append({
        "Product Name": name,
        "Price": price,
        "Availability": availability,
        "Product URL": URL + link,
        "Scraped At": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

df = pd.DataFrame(data)

# CHANGE: Use to_excel instead of to_csv
# The file extension should be .xlsx
df.to_excel("output.xlsx", index=False)

print("Scraping completed. Data saved to output.xlsx")