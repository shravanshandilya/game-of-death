#!/usr/bin/python
char_file = open("char_data.txt","r")
chars = []
char = dict.fromkeys(['name','status','sex','s01','s02','s03','s04','s05','total','alignment'],None)
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
	chars.append(char)
	print char,"\n"
print len(chars)
