# from http://docs.python-guide.org/en/latest/scenarios/scrape/
from lxml import html
import requests
import time

#links = open("links.txt","a")
dates = open("dates.txt","a")

start_time = time.time() #start counting

#set first page
nextPage = "http://www.astro.com/wiki/astro-databank/index.php?title=Special:AllPages&from=1943+Frankford+Junction+derailment"
pageNumber = 1

while nextPage:
#for x in xrange(1,2):
    #get and store webpage in a class
    page = requests.get(nextPage)
    #html.fromstring parses page.content (is a string) into tree, which is stored in a standard lxml class (a tree)
    tree = html.fromstring(page.content)
    #collect next page, store as string
    nextPage = tree.xpath('//*[@id="mw-content-text"]/div/a[2]/@href')
    nextPage = ('http://www.astro.com'+''.join(nextPage))

    #select links, put in a list
    pagePaths = tree.xpath('//*[@id="mw-content-text"]/ul/li[*]/a/@href')
    #this is a list comprehension
    pagePaths = ['http://www.astro.com{0}'.format(i) for i in pagePaths]
    pagePathLengthString = str(len(pagePaths))

    #pull birthdate from each page
    length = len(pagePaths)
    for i,length in enumerate(pagePaths):
        datePage = requests.get(pagePaths[i])
        dateTree = html.fromstring(datePage.content)
        birthdate = dateTree.xpath('//*[@id="mw-content-text"]/table//td/b[contains(.,"born on")]/../../td[2]/text()')
        dates.write(''.join(birthdate).encode('utf8'))
        print('Processed birthdate '+str(i)+'/'+pagePathLengthString+' on page '+str(pageNumber))
    pageNumber += 1


elapsed_time = time.time() - start_time
print (str(elapsed_time/60)+" minutes elapsed")
print('\a\a\a\a\a\a')

# pageNested = requests.get(pagePaths[i])
# treeNested = html.fromstring(pageNested.content)


# length = len(pagePaths)
# for i,length in enumerate(pagePaths):
#     pageNested = requests.get(pagePaths[i])
#     treeNested = html.fromstring(pageNested.content)

#     songPathNext = tree.xpath('//*[@id="audio1"]/@src')
#     links.write(songPathNext[0]+'\n')

# for x in y === for index,x in enumerate y
