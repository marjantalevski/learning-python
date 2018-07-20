import requests
from bs4 import BeautifulSoup

base_url = "https://tocka.com.mk/"
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")
for title in soup.find_all(class_="item") and soup.find_all(class_="caption"):
    if title.a:
        print(title.a.text)
    else: 
        print(title.contents[0])


