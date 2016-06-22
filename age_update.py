char_file = open("char_data_latest.txt","r")
update_file = open("char_data_latest_with_age_update.txt","w+")
for c in char_file:
	res = c.split(",")
	writ = c[0:len(c)-3]+str(int(res[10])+2)
	print writ
	update_file.write(writ+"\n")
