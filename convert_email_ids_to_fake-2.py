#!/usr/bin/env python
# coding: utf-8


#-------- replace text in the given file START -------#

def replace_file_data(datafile, orig_text, rep_text):
	"""
	Replaces the given text in the file with other data.
	"""
	status = False
	
	try:
		fd = open(datafile, "r+")
		status = True
	except:
		status = False

	try:
		if (status):
			lines = fd.readlines()
			fd.seek(0)
			fd.truncate()
			for line in lines:
				if orig_text in line:
					line = line.replace(orig_text, rep_text)
				fd.write(line)
			
			fd.close()
	except:
		status = False

	return (status)

#-------- replace text in the given file END  -------#


#------ checking and sending email list for writing START -----#

def work_email_list(email_lst, datafile):
	"""
	just cheking if the list contains 1 or more email ids
	and calling the loop accordingly.
	"""
	status = True
	
	try:
		if (len(email_lst)>1):
			for eml in email_lst:
				rep_id = eml.replace("@", "@sample.")
				replace_file_data(datafile, eml, rep_id)
		else:
			rep_id = email_lst[0].replace("@", "@sample.")
			replace_file_data(datafile, email_lst[0], rep_id)
	except:
		status = False

	return (status)

#------ checking and sending email list for writing START -----#


#---- Find and converting email ids to fake email ids START -------#

def convert_email_ids(datafile):
	"""
	Find email ids from the given file and convert them into
	fake email ids.
	"""

	rep_status = False
	
	emx = (lambda x: (x.rfind('@')>0) and (x.rfind('.')>0) and (x.rfind('.')<len(x)-1))
		
	for line in open(datafile, 'r'):
		if True in (map(emx, line.split(' '))):
			if (len(line.split(','))>1):
				email_lst = filter(emx, line.split(','))
				rep_status = work_email_list(email_lst, datafile)
			elif (len(line.split(' '))>1):
				email_lst = filter(emx, line.split(' '))
				rep_status = work_email_list(email_lst, datafile)
			else:
				pass
	
	return (rep_status)

#---- Find and converting email ids to fake email ids END ---------#

filepath = "/tmp/lcmdb4.sql"

convert_email_ids(filepath)
