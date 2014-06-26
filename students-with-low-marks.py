#!/usr/bin/env python
# coding: utf-8

#----- Students With Low Marks Start ------#

def stns_with_low_marks(stnfile):
	"""
	Finding no. of students with total less than 100.
	"""

	swlm = 0
	kvp = {}
	slst = []

	fd = open(stnfile, "r")
	opt = fd.read()
	fd.close()

	slst = opt.split("\n")
	slst.pop()

	for stn in slst:
		st = stn.split("|")
		if (not st[0] in kvp.keys()):
			kvp[st[0]] = {}
			kvp[st[0]][st[1]] = int(st[2])
		else:
			kvp[st[0]][st[1]] = int(st[2])

	for k in kvp.keys():
		kvp[k]['total'] = sum(kvp[k].values())
		if (kvp[k]['total'] < 100):
			swlm = swlm +1
	
	#print swlm
	return (swlm)

#----------- Students With Low Marks END ----------------#


filepath = "/tmp/output.txt"

stns_with_low_marks(filepath)	
