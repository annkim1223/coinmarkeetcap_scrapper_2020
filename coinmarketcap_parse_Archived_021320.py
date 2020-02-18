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
		# currency_supply = currency_rows.find("td", {"class":"cmc-table__cell--sort-by__circulating-supply"}).find("div").text.replace(" *","") 
		# we loop all the following code. 
		# print(currency_name)
		# print(currency_price)
		# print(currency_marketcap)
		# print(curency_supply)

		df = df.append({  # df=data frame ( = put argumet, { = list of stuff
				'time':scraping_time,
				'name':currency_name,
				'price':currency_price,
				'markecap':currency_marketcap,
				'supply': currency_supply 

			}, ignore_index=True)
	# except:
	# 	pass

	# print (df)

df.to_csv("parsed_files/coinmarketcap_dataset.csv")

# Python coinmarketcap_parse(new).py
"""
By doing so, you can do multiple rows by using code for one row in the loop function
When you print them, we can the list of name, price market cap, supply.
Catch is using "find_all" and using "loop" function.


Now, you have the text data you got from python. Now, we want to put it in CSV file. In csv file, you need to put "" to be able to indivate it is the column. 

Also, you import os and make a new folder to store the out put of out file.
"""



"""

2/6/2020
try to lean beautilful soup by looking at the documentation. 
Also, each website has different html structure so you need to use different code
for each website. You can practice it by repeating the code and looking at the html directly. 
But you can also inspect in the website. 


"""