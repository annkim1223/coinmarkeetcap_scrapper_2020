#02/13/2020 I couldn't get the csv so I just typed

import urllib.request
import time
import os
import pandas as pd

if not os.path.exists("deep_link_html_files"):
	os.mkdir("deep_link_html_files")

#we now want to read csv file (import pandas as pd)

df = pd.read_csv("parsed_files/coinmarketcap_dataset.csv")

#print(df)

for link in df['link']:
	filename = link.replace("/","").replace("currencies","")
	if os.path.exists("deep_link_html/" + filename + ".html", "wb"):
		print(filename + " exist")
	else: print("Downloading:" + filename)
		# print(filename)
		f = open("deep_link_html/" + filename + ".htm.temp", "wb")
		#we save this to different file name so that they don't overwrite (last time we used only date but now currency name as well.)
		#when you are doing it and link is the name of currency, it is better to use link because it filters the characters that are not allowed as name of file. 
		response = urllib.request.urlopen(('https://coinmarketcap.com' + link)
		html = response.read()
		f.write(html)
		f.close()
		#response is not the html yet but html object. By putting html - we make it to html
		#as if we requested to one link before, we are doing it to many many links by for loop.
		#find the actual link and add the part that is not unique
		os.rename("deep_link_html/" + filename + ".html.temp", "deep_link_html/" + filename + ".html")
		#this code makes the file 
		time.sleep(20)
		#time.sleep() is very important because you can break the website by doing it per 0.0000001 sec without time.sleep


"""
What if the program stops?
(any kind of interuption such as keyboard interruption, website down, and programs on your computer)
To prepare for it, you want to 
(1) add a number to your file name. so that you can track where you stopped. 
However, if the progrma kept downloading when the website is down, it is useless. 
(2) When you are downloading it, check whether the file exists or not.
Use code 'if not os.path.exists():' and if else statement.
However, it has some problem too. What if the file still exists even though it doesn't have any contents.
(3) now when you creat a file, you can creat temp file f = open("deep_link_html/" + filename + ".htm.temp", "wb")
then, change the file name.temp to the original file name once downloading is done. (os.rename()) 
Then you can check if the file exists or not easily.


"""


