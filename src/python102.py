# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from bs4 import BeautifulSoup
import urllib


response = urllib.urlopen("http://www.google.com")
doc = response.read()

soup = BeautifulSoup(doc)

for link in soup.find_all('a'):
    print(link.get('href'))