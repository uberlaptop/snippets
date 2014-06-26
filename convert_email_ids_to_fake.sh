#!/bin/bash

start_time=$(date '+%d-%b-%Y %r');

echo -e "\n#------------- ${start_time} - Starting Here -----------#\n"

filepath=$1

text=$2

#--------------------- validating filepath -------------------------#

if [ ! ${filepath} ]
	then 
	echo -e "\n#--- No Filepath Provided ----#\n"
	exit -1;
fi

check_path=$(/bin/ls ${filepath})

if [ ! ${check_path} ]
	then
	echo -e "\n#---- Invalid Filepath Provided ----#\n"
	exit -1;
fi

#---------------------------------------------------------------------#


#----------------------validating replacement text -------------------#

if [ ! ${text} ]
	then
	echo -e "\n#---- No Replacement Text Provided ----#\n" 
	echo -e "\n#---- Setting Replacement Text as 'sample' ----#\n"
	text="sample";
fi

#---------------------------------------------------------------------#


echo -e "Filepath = ${filepath}\n"

echo -e "Text = ${text}\n"

#------------------- Getting all the email id's ------------------------#

echo -e "#---- Executing the Grep command to search for all email ids in the given file ----#\n"

email_lst=$(/bin/grep -E -o "\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b" ${filepath} | grep -v "${text}")

#---------------------------------------------------------------------#

if [ ! ${email_lst} ]
	then
	echo -e "\n#---- No Email List To Work With ------#\n"
	exit -1;
fi

echo -e "#---- Email Id List ----#\n"
echo -e "${email_lst}\n"
echo -e "#-----------------------#\n\n"

#------------------ Replacing each and every email id ----------------------#

for eml in ${email_lst}
	do
	replaced=$(/bin/echo -e "${eml}" | grep -w "${text}")
	echo -e "Replacing Email Id: ${eml}\n"
	domain=$(/bin/echo -e "${eml}" | cut -d'@' -f2)
	epart=$(/bin/echo -e "${eml}" | cut -d'@' -f1)
	new_eml="${epart}@${text}.${domain}";
	echo -e "With Email Id: ${new_eml}"
	replace=$(/bin/sed -i "s/${eml}/${new_eml}/g" ${filepath})
	echo -e "Done \n"
done

#--------------------------------------------------------------------------#

end_time=$(date '+%d-%b-%Y %r');

echo -e "\n#----------------- ${end_time} - Finish --------------------#\n"

exit 0;
