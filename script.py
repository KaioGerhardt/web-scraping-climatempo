# -*- coding: utf-8 -*-
import sys
from bs4 import BeautifulSoup
import requests

html = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/360/novohamburgo-rs").content

soup = BeautifulSoup(html, 'html.parser')
temperaturaMinima = soup.find(id="min-temp-1")
temperaturaMaxima = soup.find(id="max-temp-1")

print("""
=====================================\n     TEMPERATURA EM NOVO HAMBURGO\n=====================================""")
print(f"Temperatura Minima: {temperaturaMinima.string[:-1]}")
print(f"Temperatura Maxima: {temperaturaMaxima.string[:-1]}")