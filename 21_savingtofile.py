import requests
from bs4 import BeautifulSoup

base_url = "https://tocka.com.mk/"
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

filename = input("File to save to: ")
the_file = open(filename + ".txt", "wb")

for title in soup.find_all(class_="item") and soup.find_all(class_="caption"):
    if title.a:
        the_file.write((title.a.text + "\n").encode("utf-8"))
    else:
        the_file.write(title.contents[0].encode("utf-8"))

the_file.close()