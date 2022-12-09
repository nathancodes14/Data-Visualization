import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
import requests
from bs4 import BeautifulSoup

#dataframe = pd.read_csv('dataset.csv')
f = open("Dataset.csv", "r")
line = f.readline()
for i in range(2,32):            
    line = f.readline()
    lines = line.split(",")
    zipcode = lines[1][:-1]
    url = ("https://data.census.gov/cedsci/profile/ZCTA5_" + zipcode + "?g=860XX00US" + zipcode)
    print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(page.status_code)
    print(soup.prettify)
    name = (soup.find(class_="aqua-button"))
    print(name)

f.close()
