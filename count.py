#i should go to beD but alas, this is just too much fun
with open('daysSetNoTimes.txt', 'r') as infile:
    dates = [x.strip() for x in infile.readlines()]
    datesList = []
    for x in xrange(1,365):
        datesList.append(dates.count(str(x)))
        print str(x) + ':' + str(dates.count(str(x)))
    print( 'Largest collision: ' + str(max(datesList)) + ' : paste output into text file and cmd F to find the date')
    print("#lazycoderislazy")
