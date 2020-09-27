from bs4 import BeautifulSoup
import requests
import csv
from datetime import date
from datetime import time
from datetime import datetime

from Data_processing import Yes


class Scrapper:

    URL = requests.get(
        "https://www.gembird.rs/distri/3d-filamenti--serveri--pos/3d-filamenti-pla/0/0/0-0"
    ).text
    soup = BeautifulSoup(URL, "lxml")
    today = datetime.now()
    with open("Cena.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # file.write(str(today) + "\n")
        # ime_dela = []
        # cena = []
        for cena1 in soup.find_all("div", class_="product-meta"):
            cena = cena1.find("span", class_="product-price").text
            ime = cena1.find("a", class_="product-name").h2.text

            cena_konacno = cena[0:6]

            writer.writerow([cena_konacno, ime])

    Yes()
