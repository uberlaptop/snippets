#!/usr/bin/env python
# coding: utf-8


menu = {1: 'List Interfaces', 2: 'List ip address of all interfaces', 3: 'Enter a particular interface name'}


#------------ menu options START -----------#

def displayer(opn=0):
	"""
	Will display the menu options.
	"""
	import netifaces
	
	output = None
	
	if (not opn):
		output = '\n'.join([str(k)+': '+v for k,v in menu.items()])
		
	if (opn=='1'):
		output = '\n'.join(netifaces.interfaces())
		
	if (opn=='2'):
		output = '\n'.join(iface+": "+netifaces.ifaddresses(iface).items()[0][1][0]['addr'] for iface in netifaces.interfaces())
	
	if (opn in netifaces.interfaces()):
		output = netifaces.ifaddresses(opn).items()[0][1][0]['addr']
	
	print output
	
	return (output)

#------------ menu options END ------------#

import sys

try:
	argm = sys.argv[1]
except:
	argm = 0

displayer(argm)




