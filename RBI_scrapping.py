import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
url = "https://rbi.org.in/Scripts/ATMView.aspx"
html_doc = requests.get(url)
soup = BeautifulSoup(html_doc)
url_temp = soup.find_all('a', href = re.compile("http://rbidocs.rbi.org.in/rdocs/ATM/DOCs"))
url_list = []
for link in url_temp:
  url_fetched = link.get('href')
  url_list.append(url_fetched)

