print("tt")
import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://beautiful-soup-4.readthedocs.io/en/latest/#quick-start'  # PTT 八卦版的一頁
response = requests.get(url)  # 繞過年齡限制
if response.status_code == 200:
  soup = BeautifulSoup(response.text, 'html.parser')
soup.find_all('a', class_='reference internal')
for article in soup.find_all('a', class_='reference internal'):
  print(article.text.strip())