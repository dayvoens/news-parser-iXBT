import requests
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('news.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS articles (
               id INTEGER PRIMARY KEY AUTOINCREMENT ,
               url TEXT UNIQUE,
               title TEXT
)
""")
conn.commit()

url = "https://ixbt.games/news/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")
    
    all_links = soup.find_all("a")
    
for link in all_links:
        href = link.get('href', '')
        title = link.text.strip()
        
        if href.startswith("https://ixbt.games/news/") and href.endswith(".html") and title:
            if "Сегодня" in title:
                title = title[:title.rfind("Сегодня")].strip().rstrip("0123456789 ")
            elif "Вчера" in title:
                title = title[:title.rfind("Вчера")].strip().rstrip("0123456789 ")

            cursor.execute("SELECT id FROM articles WHERE url = ?", (href,))
            result = cursor.fetchone()

            if result is None:
                cursor.execute("INSERT INTO articles (url, title) VALUES (?, ?)", (href, title))
                conn.commit() 
                
                print(f"⚡ НОВАЯ НОВОСТЬ: {title}")
                print(f"🔗 {href}")
                print("-" * 40)

cursor.close()
conn.close()