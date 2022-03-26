from bs4 import BeautifulSoup

import requests

html = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/360/novohamburgo-rs").content

soup = BeautifulSoup(html, 'html.parser')

#print(soup.prettify())

temperatura = soup.find("span", class_="-gray-light")
temperaturaMinima = soup.find(id="min-temp-1")
temperaturaMaxima = soup.find(id="max-temp-1")

print(temperaturaMinima.string)
print(temperaturaMaxima.string)