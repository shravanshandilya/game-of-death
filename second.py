from bs4 import BeautifulSoup
import requests
import character
characters = []
fil = open("char_data.txt","r")
wri = open("write.txt","w+")
def get_portrayed_by(char):
	#print "getting portrayed by for",char
	url = "http://gameofthrones.wikia.com/wiki/"
       	soup = BeautifulSoup(requests.get(url+char.replace(" ","_")).content,"html.parser")
        results = soup.find_all("div",{"class":"pi-item pi-data pi-item-spacing pi-border-color"})
       	for res in results:
		try:
       			if(res.h3.contents[0] == "Portrayed by"):
				return res.div.contents[0].contents[0]
		except AttributeError:
			return "missed"


for line in fil:
	re = line.split(",")[0].rstrip()
	ans = get_portrayed_by(re)
	if ans==None:
		ans="missed"
	wri.write(re+","+ans+"\n")
