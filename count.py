#i should go to be but alas, this is just too much fun
with open('daysSetNoTimes.txt', 'r') as infile:
    dates = [x.strip() for x in infile.readlines()]
    for x in xrange(1,365):
        print str(x) + ':' + str(dates.count(str(x)))
