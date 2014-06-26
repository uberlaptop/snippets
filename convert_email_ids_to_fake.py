#!/usr/bin/env python
# coding: utf-8


#---- Find and converting email ids to fake email ids START -------#

def convert_email_ids(datafile):
	"""
	Find email ids from the given file and convert them into
	fake email ids.
	"""

	res = set()
	els = []
	converted_list = []

	emx = (lambda x: (x.rfind('@')>0) and (x.rfind('.')>0) and (x.rfind('.')<len(x)-1))
		
	for line in open(datafile, 'r'):
		if True in (map(emx, line.split(' '))):
			if (len(line.split(','))>1):
				res.update(filter(emx, line.split(',')))
			elif (len(line.split(' '))>1):
				res.update(filter(emx, line.split(' ')))
			else:
				pass
	
	els = list(res)
        #print "Here els = ", els	
	for n in range(0, len(els)):
		converted_list.append(els[n].strip("''").replace('@', '@sample.'))
	
	#print "Here converted_list = ", converted_list
	return (converted_list)

#---- Find and converting email ids to fake email ids END ---------#

filepath = "/tmp/lcmdb2.sql"

convert_email_ids(filepath)
