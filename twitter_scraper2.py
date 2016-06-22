from bs4 import BeautifulSoup
import requests
import math

final_file = open("char_data.txt","r")
final_final_file = open("shit.txt","w+")
characters = []
results = []
got_relative = []
max_relative = []
final_point = []
maxi = 0.0
def get_followers(char = "GoT"):
	url = "https://www.google.co.in/search?as_q="
       	soup = BeautifulSoup(requests.get(url+char.replace(" ","+")).content,"html.parser")
	res  = soup.find_all("div",{"id":"resultStats"})
	return int(res[0].contents[0].encode("utf-8").split(" ")[1].replace(",",""))

got = get_followers("game of thrones")
char_file = open("write.txt","r")
for line in char_file:
	res = line.split(",")
#	print res
#	if(res[0]!="Jon Snow" and res[0]!="Arya Stark"):
#		val = get_followers(res[0]+" game of thrones")
#	else:
#		if(res[0]=="Jon Snow"):
#			val = get_followers(res[0]+" game of thrones kit harrington")
#		elif(res[0]=="Arya Stark"):
#			val = get_followers(res[0]+" game of thrones maisie williams")
	query = res[0]+" "+res[1]+" game of thrones"
	if(res[0]=="Sansa Stark"):
		query = res[0]+" game of thrones"
	val = get_followers(query)
	characters.append(res[0])
	results.append(val)
	if(val > maxi):
		maxi = val
	got_rela = float(float(val)/float(got))*10000
	got_relative.append(got_rela)
#	print query,":",val,"%",got_rela,"##",maxi,"\n"	


for i in results:
	max_relative.append((float(i)/float(maxi))*100)


for i in range(0,len(characters)):
	final_point.append(math.ceil((got_relative[i]+max_relative[i])/2))
#	print "###",final_point[i],"##",characters[i],":",got_relative[i],":",max_relative[i]
	test= final_file.readline().rstrip()+","+str(int(final_point[i]))
	final_final_file.write(test+"\n")
