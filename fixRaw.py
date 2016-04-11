out_dates = ''

with open("raw.txt","r") as in_file:
	dates = [x.strip('\n') for x in in_file.readlines()]
	prev = ''
	for date in dates:
		if(date != prev):
			out_dates+=date+'\n'
		prev = date
		
with open("trimmed_raw.txt","w") as out_file:
	out_file.write(out_dates)
