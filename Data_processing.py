import numpy as np
import pandas as pd
import matplotlib as plt
import csv


class Yes:

    with open("Cena.csv", "r") as file:
        read = csv.reader(file)

        for taking_price in read:

            whole_price = taking_price[0:1]

            test = whole_price[0]

            converting = np.array(test)

            num = np.transpose(converting)

            percent = float(num) * 0.2

            print(percent)
