from bs4 import BeautifulSoup
import requests
import character
characters = []

def get_got_followers(char = "GoT"):
	print "Doing twitter analysis on",char
	url = "https://twitter.com/search?f=users&q="
	account_url="https://twitter.com"
       	soup = BeautifulSoup(requests.get(url+char.replace(" ","%20")).content,"html.parser")
        results = soup.find_all("div",{"class":"ProfileCard  js-actionable-user"})
       	followers = 0
       	handle = ""
       	for res in results:
               	handle = res.a['href'].encode("utf-8")
		print handle
               	another_soup = BeautifulSoup(requests.get(account_url+handle).content,"html.parser")
               	val = another_soup.find("span",{"class":"ProfileNav-value"})
               	if "K" in str(val):
                       	followers+=int(float(str(val.contents[0].split("K")[0])))*1000
                       	print handle,followers
               	else:
                       	followers+=int(str(val.contents[0].replace(",","")))
                       	print handle,followers
       	print char,":",followers

print get_got_followers("GoT")
print get_got_followers("Game of Thrones")
print get_got_followers("game of thrones")
	
