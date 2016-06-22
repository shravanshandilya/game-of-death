#!/usr/bin/python
from bs4 import BeautifulSoup
import requests

base_url = "http://gameofthrones.wikia.com/wiki/"
char_file = open("char_data.txt","r")
for char in char_file:
	char = char.split(",")[0].replace(" ","_")
	soup = BeautifulSoup(requests.get(base_url+char).content,"html.parser")
	results = soup.find_all("div",{"class":"pi-item pi-data pi-item-spacing pi-border-color"})
	for res in results:
		try:
			if res.h3.contents[0] == "Age":
				print char,":",res.div.contents[0],"\n"
		except AttributeError:
			print char," missing"
