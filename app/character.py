from bs4 import BeautifulSoup
import requests
from random import randint
import math

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

	def do_twitter_analysis(self):
#		print "\nfollowers:",self.twitter_followers,"value:",int(float(self.twitter_followers)/float(self.got_followers)*float(100)),"name:",self.name,"\n"
		return float(self.twitter_followers)/float(self.got_followers)
        	

	
	def __init__(self,init_string,got_followers):
		vals = init_string.split(",")
		#print vals
		self.name = vals[0]
		#print "Creating character",self.name
		self.status = vals[1]
		self.sex = vals[2]
		self.s01 = int(vals[3])
		self.s02 = int(vals[4])
		self.s03 = int(vals[5])
		self.s04 = int(vals[6])
		self.s05 = int(vals[7])
		self.total = int(vals[8])
		self.alignment = vals[9]
		self.age = int(vals[10])
		self.twitter_followers = int(vals[11].rstrip())
		self.got_followers = got_followers
		self.importance = int(self.how_important_is_this_character()*100)
	#	self.popularity = int(self.do_twitter_analysis()*100)
		self.popularity = int(vals[12].rstrip())
		self.good_or_bad = int(self.decode_alignment()*100)


	def get_formatted_name(self):
		return self.name

	def get_popularity(self):
		return self.popularity

	def get_good_or_bad(self):
		return self.good_or_bad

	def get_importance(self):
		return self.importance

	def blow_up_some_shit(self):
		return 0

	def set_twitter_followers(self,followers):
		self.twitter_followers = followers
	
	def get_age(self):
		return int(self.age)


	def get_probabality(self):
		POP_FACTOR = 15
		IMP_FACTOR = 35
		ALI_FACTOR = 40
		AGE_FACTOR = 10
		
		pop_factorised = float((POP_FACTOR*self.popularity)/float(100))
		imp_factorised = float((IMP_FACTOR*self.importance)/float(100))
		ali_factorised = float((ALI_FACTOR*(100-self.good_or_bad))/float(100))
		age_factorised = float((AGE_FACTOR*int(self.age))/float(100))
		result = math.ceil(pop_factorised+imp_factorised+ali_factorised+age_factorised)
		return result;
