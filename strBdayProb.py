#!/usr/bin/python

import random as rand
import sys
import matplotlib.pyplot as plt
import math

def sublist(arr, size=5000, isRand = True):
	if(size>len(arr)):
		size = len(arr)
	if(size<=0):
		return arr
	shuf = arr[:]
	if(isRand):
		rand.shuffle(shuf)
	return shuf[:size]
	
def fileToList(fname):
	try:
		arr = []
		with open(fname,"r") as in_file:
			arr = [float(x.strip('\n')) for x in in_file.readlines()]
		return arr
	except:
		print "Error: could not read file!"
		return []
	
def checkForCollisions(arr):
	if(len(arr)<=1):
		return False
	val = arr[0]
	for i in range(len(arr)):
		cur = arr[i]
		if(cur not in arr[:i] and cur not in arr[i+1:]):
			return False
	return True
	
	
def trialP(arr, n, trials = 100):
	num_col = 0
	if(n<=1):
		return 0
	for t in range(trials):
		r_arr = sublist(arr, n)	#set r_arr to a random sublist of size n
		if(checkForCollisions(r_arr)):
			num_col+=1
	print float(num_col)/trials
	return float(num_col)/trials		
	
def process(fname,size=-1):
	size = int(size)
	data_arr = fileToList(fname)
	if(len(data_arr)<=0):
		return
		
	if(size<0 or size>len(data_arr)):
		size = len(data_arr)
	
	real_p = [0.0001,.0678,.1887,.2696,.4458,.4999,.5008,.7883,.9334,.9751]
	real_n = [2000,2500,2700,2800,3000,3063,3064,3500,4000,4400]
	data_p = [trialP(data_arr,x,100) for x in real_n]
	plt.plot(real_n, real_p, label='Real Probability')
	plt.plot(real_n, data_p, label='Experimental Probability:\n100 Trials per Sample Size')
	plt.legend(loc='best')
	plt.title('Strong Birthday Problem')
	plt.xlabel('Sample Size')
	plt.ylabel('Probability of Each Person Sharing a Birthday')
	plt.show()
	
	
if(len(sys.argv)>2):
	process(sys.argv[1],sys.argv[2])
elif(len(sys.argv)>1):
	process(sys.argv[1])
else:
	print "Please provide a data file to read."
