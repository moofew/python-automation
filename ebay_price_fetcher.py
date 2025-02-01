from bs4 import BeautifulSoup
import requests
import numpy as np
from datetime import datetime

def get_prices(link):
    r = requests.get(link)
    page_parse = BeautifulSoup(r.text, 'html.parser')
    search_results = page_parse.find("ul", {"class":"srp-results"}).find_all("li", {"class":"s-item"})
    item_prices = []

    for result in search_results:
        price_as_text = result.find("span", {"class":"s-item__price"}).text
        if "to" in price_as_text:
            continue
        price = float(price_as_text[1:].replace(",", ""))
        item_prices.append(price)
    return item_prices

def get_average(prices):
    return np.mean(prices)

if __name__ == "__main__":
    link = input("Please enter URL of the ebay search: ")
    item_prices = get_prices(link)
    print("Average Price:", get_average(item_prices))