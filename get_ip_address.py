#!/usr/bin/env
# coding: utf-8


#--------- The get_ip function START --------#

def get_ip(iface=False):
	"""
	returns the ipaddress of the given interface, the ip address is returned
	in a dictionary {interface: ipaddress}, if no interface is given, then 
	it returns the ip addresses of all the available interfaces in a dictionary.
	"""
	try:
		import netifaces
		status = {}
	except:
		iface = "error"
		status[iface] = "Kindly install python netifaces"
		print status[iface]
		return (status)
	
	if (iface):
		iface = iface.strip()

	if (iface) and (iface not in netifaces.interfaces()):
		status[iface] = "Invalid Interface"
		print status[iface]
		return (status)
	
	if (iface) and (iface in netifaces.interfaces()):
		try:
			status[iface] = netifaces.ifaddresses(iface)[2][0]['addr']
		except:
			status[iface] = None
		print status[iface]
		return (status)

	if (not iface):
		for ix in netifaces.interfaces():
			try:
				status[ix] = netifaces.ifaddresses(ix)[2][0]['addr']
			except:
				status[ix] = None
		print status
		return (status)
	
	print status[iface]
	return (status)

#---------- The get_ip function END --------#


#----------------- command line START here ------------------------#

import sys
try:
	iface = sys.argv[1]
except:
	iface = False

get_ip(iface)

#-------------------------------------------------------#
