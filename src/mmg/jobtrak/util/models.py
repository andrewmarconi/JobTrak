from django.db import models
import requests
from bs4 import BeautifulSoup

# ## Sample of Scraping a Site to extract the company name
# r = requests.get('<<URL>>')
# soup = BeautifulSoup(r.text)
# company = soup.find('span', class_='company').string