from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# ========================from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# =========================
# SETUP SELENIUM
# =========================
options = Options()
options.add_argument("--headless")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://quotes.toscrape.com/js/")
time.sleep(2)

quotes = driver.find_elements(By.CSS_SELECTOR, ".quote")

data = []
for q in quotes:
    text = q.find_element(By.CSS_SELECTOR, ".text").text
    author = q.find_element(By.CSS_SELECTOR, ".author").text
    data.append({"Quote": text, "Author": author})

df = pd.DataFrame(data)
df.to_csv("quotes.csv", index=False)
print("Saved", len(data), "quotes")

driver.quit()

# CONFIG
# =========================
URL = "http://books.toscrape.com/"
CSV_FILE = "products_selenium.csv"

# =========================
# SELENIUM SETUP
# =========================
chrome_options = Options()
chrome_options.add_argument("--headless")  # run Chrome in background
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Automatically download and use correct ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# =========================
# SCRAPING
# =========================
driver.get(URL)
time.sleep(3)  # wait for page to load fully

# Adjust the CSS selector according to the site structure
products = driver.find_elements(By.CSS_SELECTOR, ".product, .menu-item, .item")

data = []
for product in products:
    title_el = product.find_element(By.CSS_SELECTOR, "h2, h3, .title, .name")
    price_el = product.find_element(By.CSS_SELECTOR, ".price, .amount")
    
    title = title_el.text.strip() if title_el else "N/A"
    price = price_el.text.strip() if price_el else "N/A"
    
    data.append({
        "Title": title,
        "Price": price
    })

# =========================
# SAVE TO CSV
# =========================
df = pd.DataFrame(data)
df.to_csv(CSV_FILE, index=False)
print(f"📁 Data saved to {CSV_FILE}, total items: {len(data)}")

# =========================
# CLEANUP
# =========================
driver.quit()
