#!/usr/bin/python
char_file = open("char_data.txt","r")
chars = []
char = dict.fromkeys(['name','status','sex','s01','s02','s03','s04','s05','total','alignment','importance'],None)

def how_important_is_this_character(char):
	total = 0
	appearances = 0
	seasons = [char['s01'],char['s02'],char['s03'],char['s04'],char['s05']]
	for season in seasons:
		if season > 0:
			total+=10
			appearances+=season 
		#print season,":",total,":",appearances,"\n"
	return float(float(appearances)/float(total))

def good_or_bad(str):
	table = { "LG":0.9999,"NG":0.8888,"CG":0.7777,"LN":0.6666,"N":0.5555,"CN":0.4444,"LE":0.3333,"NE":0.2222,"CE":0.1111}
	return table[str]




for line in char_file:
	vals = line.rstrip("\n").split(",")
	char['name'] = vals[0]
	char['status'] = vals[1]
	char['sex'] = vals[2]
	char['s01'] = int(vals[3])
	char['s02'] = int(vals[4])
	char['s03'] = int(vals[5])
	char['s04'] = int(vals[6])
	char['s05'] = int(vals[7])
	char['total'] = int(vals[8])
	char['alignment'] = vals[9]
	char['importance'] = how_important_is_this_character(char)
	char['good_or_bad'] = good_or_bad(char['alignment'])
	print char['name'],"#",char['importance'],":",char['good_or_bad'],":",char['importance']*char['good_or_bad'],"\n"
	chars.append(char)
