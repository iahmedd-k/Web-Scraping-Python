import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.robotparser import RobotFileParser
from urllib.parse import urljoin

# =========================
# CONFIG
# =========================
BASE_URL = "https://books.toscrape.com/"
TARGET_URL = "https://books.toscrape.com/catalogue/page-1.html"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; UpworkScraper/1.0)"
}
TIMEOUT = 10

# =========================
# ROBOTS.TXT CHECK
# =========================
def is_scraping_allowed(url, user_agent="*"):
    robots_url = urljoin(url, "robots.txt")
    rp = RobotFileParser()
    rp.set_url(robots_url)
    rp.read()
    return rp.can_fetch(user_agent, url)

# =========================
# SCRAPER
# =========================
def scrape_books():
    if not is_scraping_allowed(BASE_URL):
        print("❌ Scraping disallowed by robots.txt")
        return []

    print("✅ Scraping allowed")

    response = requests.get(TARGET_URL, headers=HEADERS, timeout=TIMEOUT)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.select(".product_pod")

    data = []

    for book in books:
        title = book.h3.a["title"]
        price = book.select_one(".price_color").text.strip()

        data.append({
            "Title": title,
            "Price": price
        })

    print(f"✅ Extracted {len(data)} books")
    return data

# =========================
# SAVE CSV
# =========================
def save_to_csv(data, filename="books.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"📁 Saved to {filename}")

# =========================
# MAIN
# =========================
if __name__ == "__main__":
    try:
        data = scrape_books()
        if data:
            save_to_csv(data)
        else:
            print("⚠️ No data extracted")
    except Exception as e:
        print("❌ Error:", e)
