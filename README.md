# Web Scraping Project

This repository contains Python scripts for web scraping using **Requests + BeautifulSoup** and **Selenium**. It includes examples for both static and dynamic websites, with the ability to export scraped data to **CSV** or **Excel** files. This project is perfect for learning web scraping for Upwork projects or freelance work.

---

## 📂 Project Structure

├── basic_request.py # Scrapes static websites (Books to Scrape example)
├── using_selenium.py # Scrapes JS-rendered websites using Selenium
├── requirements.txt # Python dependencies



---

## ⚙️ Features

- Scrape product/menu data from websites
- Works with **static HTML** and **JavaScript-rendered** pages
- Checks `robots.txt` before scraping
- Export scraped data to **CSV** or **Excel**
- Uses `webdriver-manager` for automatic ChromeDriver management
- Configurable CSS selectors and target URLs


requirements:
requests
beautifulsoup4
pandas
selenium
webdriver-manager
openpyxl   # Required for exporting to Excel


---

## 🛠️ Setup Instructions
