#ian klatzco and abhishek banerjee

import time
import datetime

at = 'at'
greg = "greg."
longForm  = "Jul."
parsedDates = []
parsedDatesTimes = []
datesTimes = []
datesNoTimes = []
date = ''
datesListWithTimes = []
datesListWithNoTimes = []
i=1

with open("dates.txt","r") as in_file:
    dates = [x.strip() for x in in_file.readlines()]

    # parse time vs no time
    for x in dates:
        if (at in x):
            datesTimes.append(x)
        datesNoTimes.append(x)




    for x in datesTimes:
        # parse gregorian cases
        try:
            if  (longForm in x): # string of form 15 January 1432 Jul.Cal. (24 Jan 1432 greg.) at 03:33
                date = x.split()
                date = date[4][1:]+' '+date[5]+ ' ' + date[6]+ ' ' + date[8]+ ' ' + date[9]
            elif(greg in x):     # string of form 21 August 1643 (greg.) at 07:15
                date = x.split()
                date = date[0] + ' ' + date[1]+ ' ' + date[2]+ ' ' + date[4]+ ' ' + date[5]
            else:
                date = x.split()
                date = date[0] + ' ' + date[1]+ ' ' + date[2]+ ' ' + date[3]+ ' ' + date[4]

            try:
                try:
                    dateObject = time.strptime(date,"%d %B %Y at %H:%M")
                except ValueError:
                    dateObject = time.strptime(date,"%d %b %Y at %H:%M")
            except ValueError:
                dateObject = time.strptime(date,"%d %B %Y at %H:%M:%S")

            if ((dateObject[0] % 4 == 0) and (dateObject[7] >= 60)):
                datesListWithTimes.append(dateObject[7]-1 + float(dateObject[3])/24 + float(dateObject[4])/24/60)
            else:
                datesListWithTimes.append(dateObject[7] + float(dateObject[3])/24 + float(dateObject[4])/24/60)

        except:
            print 'failed to parse a date #'+str(i)
            i += 1
            pass



    for x in datesNoTimes:
        #parse gregorian cases
        try:
            if  (longForm in x):
                date = x.split()
                date = date[4][1:]+' '+date[5]+ ' ' + date[6]
            elif(greg in x):
                date = x.split()
                date = date[0] + ' ' + date[1]+ ' ' + date[2]
            else:
                date = x.split()
                date = date[0] + ' ' + date[1]+ ' ' + date[2]

            try:
                dateObject = time.strptime(date,"%d %B %Y")
            except ValueError:
                dateObject = time.strptime(date,"%d %b %Y")

            if ((dateObject[0] % 4 == 0) and (dateObject[7] >= 60)):
                datesListWithNoTimes.append(dateObject[7]-1)
            else:
                datesListWithNoTimes.append(dateObject[7])
        except:
            print 'failed: date #'+str(i)
            i += 1
            pass

    #write to files
    write_file = open("daysSetTimes.txt","w")
    for x in datesListWithTimes:
        write_file.write(str(x)+'\n')
    write_file.close()

    write_file = open("daysSetNoTimes.txt","w")
    for x in datesListWithNoTimes:
        write_file.write(str(x)+'\n')
    write_file.close()
