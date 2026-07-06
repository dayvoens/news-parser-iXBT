# 🎮 Парсер игровых новостей iXBT с БД

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/SQLite-3-green?style=for-the-badge&logo=sqlite" alt="SQLite">
  <img src="https://img.shields.io/badge/Status-Релиз-success?style=for-the-badge" alt="Status">
</p>

---

🤖 **Консольный скрипт на Python**, который автоматически собирает свежие игровые новости с сайта iXBT и бережно сохраняет их в базу данных SQLite. 

🛡️ **Защита от дубликатов:** встроенная проверка проверяет уникальность ссылок — повторно одни и те же новости в базу не запишутся!

## 🛠️ Технологии
* 🐍 **Python 3** — основа скрипта
* 🗄️ **SQLite 3** — легковесная база данных для хранения новостей
* 🌐 **Requests , BeautifulSoup4** — парсинг и сбор данных с веб-страниц

## 🚀 Как запустить

1. **Клонировать репозиторий:**
   ```bash
   git clone https://github.com/dayvoens/news-parser-iXBT.git

2. Установка зависимостей
   ```bash
   pip install BeautifulSoup requests

3. Прокладываем путь к коду
   ```bash
   cd путь_к_коду

4. Запуск кода
   ```bash
   python gamesnews.py
