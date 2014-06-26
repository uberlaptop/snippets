#!/usr/bin/env python
# coding: utf-8

#-------- url shortener START ---------#

def snipit(longurl=False):
	"""
	A simple little command line shortener,
	made using the is.gd API.
	"""
	
	import urllib2
	
	output = {}
	
	shortener = "http://is.gd/create.php?format=simple&url="
	
	if (longurl):
		longurl = longurl.strip()
		req = urllib2.urlopen(shortener+longurl)		
		output[longurl] = req.read()
	else:
		output[longurl] = None
	
	print output[longurl]
	return (output)
	
#------- url shortener END ----------#


import sys
original_url = sys.argv[1]

snipit(original_url)

