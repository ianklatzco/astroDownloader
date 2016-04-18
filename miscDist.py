#!/usr/bin/python

import random as rand
import sys
import matplotlib.pyplot as plt

def sublist(arr, size=5000, isRand = True):
	if(size>len(arr)):
		size = len(arr)
	if(size<=0):
		return arr
	if(isRand):
		arr = rand.shuffle(arr)
	return arr[:size]
	
def getMinMax(arr):
	tblsz = int(max(arr))
	tbl = [0 for x in range(tblsz)]
	for i in arr:
		tbl[int(i)-1]+=1
	return ((tbl.index(min(tbl))+1, min(tbl)),(tbl.index(max(tbl))+1,max(tbl)))
	
def fileToList(fname):
	try:
		arr = []
		with open(fname,"r") as in_file:
			arr = [float(x.strip('\n')) for x in in_file.readlines()]
		return arr
	except:
		print "Error: could not read file!"
		return []

def process(fname,size=-1):
	size = int(size)
	data_arr = fileToList(fname)
	if(len(data_arr)<=0):
		return
	
	bins = int(max(data_arr))
	units = 'Year'
	if(bins<=12):
		units = 'Month'
	elif(bins<=366):
		units = 'Day'
	
	bins = range(bins+2)
	bins[:] = [x-0.5 for x in bins]
	
	data_arr = sublist(data_arr,size)
	
	if(size<0 or size>len(data_arr)):
		size = len(data_arr)
	
	plt.hist(data_arr,bins)
	plt.ylabel('Number of Occurances')
	plt.xlabel(''+units+'s')
	plt.title('Distribution of '+units+'s of '+str(size)+' Real Birthdays')
	plt.xlim(plt.xlim()[0]/2,plt.xlim()[1]+plt.xlim()[0]/2)
	
	plt.show()
	
	print getMinMax(data_arr)
	
if(len(sys.argv)>2):
	process(sys.argv[1],sys.argv[2])
elif(len(sys.argv)>1):
	process(sys.argv[1])
else:
	print "Please provide a data file to read."
