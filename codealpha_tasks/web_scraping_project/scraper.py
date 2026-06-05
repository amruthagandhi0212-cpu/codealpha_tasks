#import requests

#url = "https://books.toscrape.com"

#response = requests.get(url)

#print(response.text) import requests


#import requests
#from bs4 import BeautifulSoup

#url = "https://books.toscrape.com"

#response = requests.get(url)

#soup = BeautifulSoup(response.text, "html.parser")

#books = soup.find_all("article", class_="product_pod")

#print(len(books))


#import requests
#from bs4 import BeautifulSoup

#url = "https://books.toscrape.com"

#response = requests.get(url)

#soup = BeautifulSoup(response.text, "html.parser")

#books = soup.find_all("article", class_="product_pod")

#for book in books:

 #   title = book.h3.a["title"]

 #   print(title)import requests
#


#from bs4 import BeautifulSoup

#url = "https://books.toscrape.com"

#response = requests.get(url)

#soup = BeautifulSoup(response.text, "html.parser")

#books = soup.find_all("article", class_="product_pod")

#for book in books:

   # title = book.h3.a["title"]

   # price = book.find("p", class_="price_color").text

  #  print(title)
   # print(price)
   # print("------") 
   # 

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

titles = []
prices = []

for book in books:

    title = book.h3.a["title"]

    price = book.find("p", class_="price_color").text

    titles.append(title)
    prices.append(price)

data = {
    "Title": titles,
    "Price": prices
}

df = pd.DataFrame(data)

df.to_csv("books.csv", index=False)

print("Data Saved Successfully")