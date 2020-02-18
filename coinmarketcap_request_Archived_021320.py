###Amin's file

import urllib.request
import time
import datetime
import os    #allows working with folders in python


if not os.path.exists("html_files"):
    os.mkdir("html_files")

for i in range(5):
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time_stamp)
	f = open("html_files/coinmarketcap" + current_time_stamp + ".html", "wb") 
	response = urllib.request.urlopen('https://coinmarketcap.com/')
	html = response.read()#saving the text part of the page in this variable
	f.write(html)#making sure that the file name will be different everytime that we save the file.
	f.close()
	time.sleep(5)#the time is in seconds and increase the number to avoid website blockage



#w here means that we want to write it. b means binary.
#we usually need to have the open command in the beginning of the programm



