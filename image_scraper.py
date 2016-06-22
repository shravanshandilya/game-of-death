#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
base_url = "http://gameofthrones.wikia.com/wiki/"
chars = open("char_data.txt","r")
for line in chars:
	try:
		soup = BeautifulSoup(requests.get(base_url+str(line.split(",")[0].replace(" ","_"))).content,"html.parser")
		result = soup.find("figure",{"class":"pi-item pi-image"})
		image_link = result.a.img['src']
		print line.split(",")[0]
		r_img = requests.get(image_link) 
		f=open("app/static/images/"+line.split(",")[0].replace(" ","_")+'.jpg','wb')
		f.write(r_img.content) 
		f.close()
	except AttributeError:
		print line.split(",")[0],"--> Missing"
