#!/usr/bin/env python
# coding: utf-8

import time

start_time = time.strftime("%d-%b-%Y %r")

print "\n#---------- %s - Starting Here --------#\n" % (start_time)

#------ checking and sending email list for writing START -----#

def work_email_list(email_lst, datafile, rep_text):
	"""
	just cheking if the list contains 1 or more email ids
	and calling the loop accordingly.
	"""
	import subprocess
	
	print "Working on the email list\n"
	
	status = True
	
	email_dic = {}
	
	try:
		if (len(email_lst)>1):
			for eml in email_lst:
				email_dic[eml] = eml.replace("@", "@"+rep_text+".")
		else:
			email_dic[email_lst[0]] = email_lst[0].replace("@", "@"+rep_text+".")
		
		print "Formed a Dictionary:\n"
		
		for key in email_dic:
			rep_command = 'sed -i "s/%s/%s/g" %s' % (key, email_dic.get(key), datafile)
			status = subprocess.check_output(rep_command, shell=True)
			print "Replacing Email Id: %s\n" % (key)
			print "With Email Id: %s\n" % (email_dic.get(key))
			print "%s\n" % (status)
	
	except Exception, e:
		status = str(e)
		print "work_email_list: %s" % (status)
	
	return (status)

#------ checking and sending email list for writing START -----#


#---- Find and converting email ids to fake email ids START -------#

def convert_email_ids(datafile, rep_text):
	"""
	Find email ids from the given file and convert them into
	fake email ids.
	"""
	import re
	
	print "Convert email ids function called\n"
	
	rep_status = True
	
	email_lst = []
	
	dlm = ["\|", "\,", " ", "\;", "\:", "\$", "\&", "\#"] 			# delimiters
	
	emx = (lambda x: (x.rfind('@')>0) and (x.rfind('.')>0) and (x.rfind('.')<len(x)-1))
	
	try:	
		for line in open(datafile, 'r'):
			if True in (map(emx, re.split("|".join(dlm), line))):
				email_lst = email_lst + filter(emx, re.split("|".join(dlm), line))
		
		email_lst = [eml.strip("''") for eml in email_lst if not rep_text in eml.strip("''")]
					
		print "Collected Email Ids:"
		print "%s\n" % (email_lst)
		
		if (email_lst):
			rep_status = work_email_list(email_lst, datafile, rep_text)
		else:
			print "No Email list to work with\n"
			pass
	
	except Exception, e:
		rep_status = str(e)
		print "convert_email_ids: %s" % rep_status
	
	return (rep_status)

#---- Find and converting email ids to fake email ids END ---------#



#---- Taking the given parameters and validating START -------#

def main():
	"""
	Takes in the parameters passed by the user and validates the same.
	"""
	import argparse
	import sys
	import os
	
	print "File executed - main function called\n"
	
	
	status = True
	
	try:
		parser = argparse.ArgumentParser()
		
		parser.add_argument('-f', '--filepath', type=str, required=True, help="Complete path of the file.")
		parser.add_argument('-t', '--text', type=str, required=False, default='sample', help="some text to replace the original one with")
		
		args = parser.parse_args().__dict__
		
		print "Filepath: %s\n" % args.get('filepath')
		print "Replace Text: %s\n" % args.get('text')
		
		if (not args.get("filepath")):
			print "No filepath provided.\n"
			sys.exit(-1)
			
		if (not os.path.isfile(args.get("filepath"))):
			print "Incorrect filepath provided.\n"
			sys.exit(-1)
			
		status = convert_email_ids(args.get('filepath'), args.get('text'))         # Calling the email id converter function
		
		end_time = time.strftime("%d-%b-%Y %r")
		print "#------- %s - Finish --------#\n" % (end_time)
	except Exception, e:
		status = str(e)
		print "main: %s" % (status)
	
	return (status)

#---- Taking the given parameters and validating END ----------#


if __name__ == "__main__":
	main()
	
