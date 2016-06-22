from bs4 import BeautifulSoup
import requests

class character:
	def how_important_is_this_character(self):
		total = 0
	        appearances = 0
        	seasons = [self.s01,self.s02,self.s03,self.s04,self.s05]
        	for season in seasons:
                	if season > 0:
                        	total+=10
                        	appearances+=season
                	#print season,":",total,":",appearances,"\n"
        	return float(float(appearances)/float(total))

	def decode_alignment(self):
		table = { "LG":0.9999,"NG":0.8888,"CG":0.7777,"LN":0.6666,"N":0.5555,"CN":0.4444,"LE":0.3333,"NE":0.2222,"CE":0.1111}
		return table[self.alignment.rstrip()]

	def do_twiter_analysis(self,got_followers):
		soup = BeautifulSoup(requests.get(url+self.name.replace(" ","%20")).content,"html.parser")
	        results = soup.find_all("div",{"class":"ProfileCard  js-actionable-user"})
        	followers = 0
        	handle = ""
        	for res in results:
                	handle = res.a['href'].encode("utf-8")
                	another_soup = BeautifulSoup(requests.get(account_url+handle).content,"html.parser")
                	val = another_soup.find("span",{"class":"ProfileNav-value"})
                	if "K" in str(val):
                        	followers+=int(float(str(val.contents[0].split("K")[0])))*1000
                       		#print handle,followers
                	else:
                        	followers+=int(str(val.contents[0].replace(",","")))
                        	#print handle,followers
		return float(follower/self.got_followers)
        	
	
	def __init__(self,init_string,got_followers):
		vals = init_string.split(",")
		self.name = vals[0]
		print "Creating character",self.name
		self.status = vals[1]
		self.sex = vals[2]
		self.s01 = int(vals[3])
		self.s02 = int(vals[4])
		self.s03 = int(vals[5])
		self.s04 = int(vals[6])
		self.s05 = int(vals[7])
		self.total = int(vals[8])
		self.alignment = vals[9]
		self.importance = 30
		#self.popularity = self.do_twitter_analysis()
		self.popularity = 10
		self.good_or_bad = 20
		self.got_followers = got_followers


	def get_formatted_name(self):
		return self.name.replace("_"," ")

	def popularity(self):
		return self.popularity

	def good_or_bad(self):
		return self.good_or_bad

	def importance(self):
		return self.importance

	def blow_up_some_shit(self):
		return 0
