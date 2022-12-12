from collections import OrderedDict
import csv

import requests
from bs4 import BeautifulSoup


URL = "https://www.countries-ofthe-world.com/capitals-of-the-world.html"


def main():
    countries = []
    fieldnames = ["id", "country", "capital"]

    res = requests.get(URL)

    soup = BeautifulSoup(res.content, 'html.parser')

    n = 1
    for tr in soup.find_all('tr'):
        
        tds = tr.find_all('td')

        if len(tds) < 2:
            continue

        country_name = tds[0].get_text()
        capital_city = tds[1].get_text()

        country_name = country_name.split('(')[0].strip()
        capital_city = capital_city.split('(')[0].strip()

        print(f"{country_name.ljust(36)} {capital_city}")

        country = OrderedDict({
            "id": n,
            "country": country_name,
            "capital": capital_city
        })

        n += 1

        countries.append(country)

    
    with open("countries.csv", 'w', encoding='UTF8', newline='') as file:

        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter='|')
        writer.writeheader()
        writer.writerows(countries)


if __name__ == "__main__":
    main()