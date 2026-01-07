import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://webscraper.io/test-sites/e-commerce/static"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

items = soup.select(".thumbnail")

leads = []

for item in items:
    name = item.select_one(".title").text.strip()
    price = item.select_one(".price").text.strip()
    description = item.select_one(".description").text.strip()

    leads.append({
        "Business / Product Name": name,
        "Price": price,
        "Description": description
    })

df = pd.DataFrame(leads)
df.to_excel("leads.xlsx", index=False)

print(f"Scraped {len(df)} leads successfully!")
