# import pandas as pd 
# import requests
# from bs4 import BeautifulSoup

# res = requests.get()
# soup = BeautifulSoup(res.content,'lxml')
# print(soup)
# table = soup.find('table', id='cart_summary')
# df = pd.read_html(str(table))
# print(df[1].to_json(orient='records'))

import urllib.request 

webUrl = urllib.request.urlopen("https://www.strongflex.eu/en/order")