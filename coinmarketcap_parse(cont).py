from bs4 import BeautifulSoup

f = open("html_files/coinmarketcap20200", "r")
soup = BeautifulSoup(f.read(), 'html.parser')

