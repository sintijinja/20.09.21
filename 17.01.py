#import requests
#from bs4 import BeautifulSoup

#lapa = requests.get("https://vilanuvidusskola.blogspot.com/")


#soup = BeautifulSoup(lapa.content, 'html.parser')


#print(soup.find_all('p'))

#print(soup.find_all('p')[0].get_text())


import requests
from bs4 import BeautifulSoup

lapa = requests.get("https://vvsprogramm.github.io/A/")


soup = BeautifulSoup(lapa.content, 'html.parser')


#print(soup.find_all('p'))

#print(soup.find_all('p')[0].get_text())


#print(soup.find_all('p')[1].get_text())

print(soup.find_all('p')[2].get_text())



