#python -m pip install BeautifulSoup4
#python -m pip uninstall BeautifulSoup4
#python -m pip install BeautifulSoup
#python -m pip uninstall BeautifulSoup
from bs4 import BeautifulSoup
import os
import pandas as pd
import glob

if not os.path.exists("parse_files"):
	os.mkdir("parsed_files")

df = pd.DataFrame()

for one_file_name in glob.glob("html_files/*.html"):
	print("parsing: ",one_file_name)
	#f = open("html_files/coinmarketcap20200204153935.html", "r")
	scraping_time = os.path.basename(one_file_name)
	f = open(one_file_name, "r")
	soup = BeautifulSoup(f.read(), 'html.parser')
	f.close()

	currencies_table = soup.find("tbody")

	currency_rows = currencies_table.find_all("tr")
	# try:

	for r in currency_rows:
		currency_price = r.find("td", {"class":"cmc-table__cell--sort-by__price"}).find("a").text.replace(",","").replace("$","") # ?? Why not replace in csv file?
		currency_name = r.find("td", {"class":"cmc-table__cell--sort-by__name"}).find("a", {"class":"cmc-link"}).text
		currency_marketcap = r.find("td", {"class":"cmc-table__cell--sort-by__market-cap"}).find("div").text
		currency_supply = r.find("td",{"class":"cmc-table__cell--sort-by__circulating-supply"}).find("div").text.replace(" *","").replace("$","")
		currency_link= r.find("a", {"class":"cmc-link"})["href"]
		# this finds links. #################????????????????????Doesn't work
		#02/13/2020
	
		# print(currency_name)
		# print(currency_price)
		# print(currency_marketcap)
		# print(curency_supply)

		df = df.append({  # df=data frame ( = put argumet, { = list of stuff
				'time':scraping_time,
				'name':currency_name,
				'price':currency_price,
				'markecap':currency_marketcap,
				'supply': currency_supply,
				'link':currency_link

			}, ignore_index=True)
	# except:
	# 	pass

	# print (df)

df.to_csv("parsed_files/coinmarketcap_dataset.csv")





"""
02/13/2020

We will see the rank of the hyperlink. 
[inspect] in the website on the hyperlink.
Go to parse file

----------------------
Form the ranks using the direct rank after 'href="..."
<a href="/currencies/bitcoin/" title="Bitcoin" class="cmc-link">Bitcoin</a>
<atribute - "link" title ="name" class ="">Bitoin </atributes>
The rank is in atributes. 
First we need to finnd atribute to find the rank. 
currency_link in the code

"""
