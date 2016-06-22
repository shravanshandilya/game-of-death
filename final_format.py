char_file = open("char_data_latest_with_age_update.txt","r")
twitter_file = open("twitter.txt","r")
final_file = open("final_file.txt","w+")
char = []
twitter = []

for line in char_file:
	char.append(line)

for lin in twitter_file:
	twitter.append(lin)

for i in range(0,len(char)):
	stri = char[i].rstrip()+","+twitter[i].split(",")[1]+"\n"
	final_file.write(stri)
	print stri
