#!/usr/bin/python

import random as rand
import sys
import matplotlib.pyplot as plt

from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

def genStick(isRand, size = -1, arr = []):
	if(size<0):
		size = len(arr)
	if(size==0 or (not isRand and len(arr)==0)):
		return []
	if(not isRand and size>len(arr)):
		size == len(arr)
	u_bound = 366
	l_bound = 1
	
	if(not isRand):
		for i in range(len(arr)):
			if(arr[i]<l_bound or arr[i]>u_bound):
				arr.pop(i);
		rand.shuffle(arr)
		arr = arr[:size]
		return sorted(arr)
	else:
		new_arr = []
		for i in range(size):
			new_arr.append(rand.uniform(l_bound,u_bound))
		return sorted(new_arr)
		
def segment(stick):
	prev = 1
	seg_list = []
	for curr in stick:
		seg_list.append(curr-prev)
		prev = curr
	seg_list.append(366-stick[len(stick)-1])
	return seg_list
	
def fileToList(fname):
	try:
		arr = []
		with open(fname,"r") as in_file:
			arr = [float(x.strip('\n')) for x in in_file.readlines()]
		return arr
	except:
		print "Error: could not read file!\n"
		return []

def process(fname,size=-1):
	size = int(size)
	day_arr = fileToList(fname)
	stick = segment(genStick(False,size,day_arr))
	stick_r = segment(genStick(True,size, day_arr))
	
	bins = 50
	if(size<0 or size>len(day_arr)):
		size = len(day_arr)
	
	

	ax1 = plt.subplot(2,1,1)
	plt.hist(stick,bins)
	plt.ylabel('Segment Occurances')
	plt.xlabel('Segment Lengths [days]')
	plt.title(str(size)+' Real Birthdays')
	
	plt.subplot(2,1,2, sharex=ax1, sharey = ax1)
	plt.hist(stick_r,bins)
	plt.ylabel('Segment Occurances')
	plt.xlabel('Segment Lengths [days]')
	plt.title(str(size)+' Random Birthdays')
	
	
	
	plt.show()
	
if(len(sys.argv)>2):
	process(sys.argv[1],sys.argv[2])
elif(len(sys.argv)>1):
	process(sys.argv[1])
else:
	print "Please provide a data file to read."
