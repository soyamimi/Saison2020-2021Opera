import requests
from bs4 import BeautifulSoup

url= "https://www.operadeparis.fr/programmation-et-billets/saison-20-21/lieux-palais-garnier"
html=requests.get(url)

soup=BeautifulSoup(html.text,'html.parser')
vente= soup.select_one('href.vente')
if(vente) :
    vente=vente.find_parent('div',class_='filter-results-content')
    title=vente.select_one('div > p.show__title').text.strip()
    print(title + 'En vente')
else :

    print('x')
