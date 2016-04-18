#!/usr/bin/python

import random as rand
import sys
import matplotlib.pyplot as plt
import math

YEAR_FACT = math.factorial(365)

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
		
def calcP(n):
	if(n>=365):
		return 1
	return 1-calcRec(2,n)
	
def calcRec(i, n):
	if(i>n):
		return 1
	return (366.0-i)/365.0 * calcRec(i+1,n)
	
def checkForCollisions(arr):
	if(len(arr)<=1):
		return False
	for i in range(len(arr)-1):
		cur = arr[i]
		if(cur in arr[i+1:]):
			return True
	return False
	
	
def trialP(arr, n, trials = 100):
	num_col = 0
	if(n<=1):
		return 0
	for t in range(trials):
		r_arr = sublist(arr, n)	#set r_arr to a random sublist of size n
		if(checkForCollisions(r_arr)):
			num_col+=1
	if(n%10==0):
		print str(n)+'%'
	return float(num_col)/trials		
	
def process(fname,size=-1):
	size = int(size)
	data_arr = fileToList(fname)
	if(len(data_arr)<=0):
		return
		
	if(size<0 or size>len(data_arr)):
		size = len(data_arr)
	
	max_sample = 101
	real_p = [calcP(x) for x in range(max_sample)]
	data_p = [trialP(data_arr,x,100) for x in range(max_sample)]
	plt.plot(range(max_sample), real_p, label='Real Probability')
	plt.plot(range(max_sample), data_p, label='Experimental Probability:\n100 Trials per Sample Size')
	plt.legend(loc='best')
	plt.title('Probability of One or More Shared Birthdays')
	plt.xlabel('Sample Size')
	plt.ylabel('Probability of at least One Shared Birthday')
	plt.show()
	
	
if(len(sys.argv)>2):
	process(sys.argv[1],sys.argv[2])
elif(len(sys.argv)>1):
	process(sys.argv[1])
else:
	print "Please provide a data file to read."
