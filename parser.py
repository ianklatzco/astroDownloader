#!/usr/bin/python

import json

out_data = '{'

with open("raw.txt","r") as in_file:
	dates = [x.strip('\n') for x in in_file.readlines()]
	i = 0
	for cur_date in dates:
		i+=1
		data = cur_date.split()
		day = data[0]
		month = data[1]
		year = data[2]
		time = '--:--'
		if('at' in data):
			time = data[data.index('at')+1][:5]
	
		out_data += '"date_'+str(i)+'":{"day":'+day+',"month":"'+month+'","year":'+year+',"time":"'+time+'"},'
	
out_data = out_data[:len(out_data)-1]
out_data += '}'
out_json = json.loads(out_data)

with open("bday.json","w") as out_file:
	json.dump(out_json,out_file,indent=2)
