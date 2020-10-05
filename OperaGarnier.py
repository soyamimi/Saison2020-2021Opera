import requests
from bs4 import BeautifulSoup
import pandas as pd

url= "https://www.operadeparis.fr/programmation-et-billets/saison-20-21"
html = requests.get(url)

soup= BeautifulSoup(html.text,'html.parser')

genre=soup.select('div > div.FeaturedList__card-image > a > p')
title=soup.select('div > div.FeaturedList__card-image > a > div > p.show__title')
place=soup.select('div > div.FeaturedList__card-content > p.show__place')
date=soup.select('div > div.FeaturedList__card-content > p.show__date')
open=soup.select('div > div.FeaturedList__card-content>p.show__coming') or soup.select('div > div.FeaturedList__card-content> a')


list_piece = []
for item in zip(genre, title, place, date, open):
    list_piece.append(
        {
            'Genre': item[0].text.replace('\n', '').replace('\t', '').replace('  ', ''),
            'Title': item[1].text.replace('\n', '').replace('\t', '').replace('  ', ''),
            'Place': item[2].text.replace('\n', '').replace('\t', '').replace('  ', ''),
            'Date': item[3].text.replace('\n', '').replace('\t', '').replace('  ', ''),
            'Reservation': item[4].text.replace('\n', '').replace('\t', '').replace('  ', '')
        }
    )

pd_data1=pd.DataFrame.from_dict((list_piece))
ndf1 = pd_data1.set_index('Title')
print(list_piece)
print(ndf1)
