#!/usr/bin/env python
# coding: utf-8

# I came across this little challenge. i was given a recursive list like this one :
# [1, 2, 3, [4, 5], 6, 7, [8, [9], [10]], 11, 12, [13, [14, [15]]], 16]
# and i was suppose to convert this into a single list or a string, like this:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# or like this
# '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16'

# i found a little quick and easy way to do this.
# if anybody finds the method correct, feel free to correct me

x = [1, 2, 3, [4, 5], 6, 7, [8, [9], [10]], 11, 12, [13, [14, [15]]], 16]

print x

print "\n"

y = x.__str__().replace('[', '').replace(']', '')

print y

print "\n"

# when you print y, you'll get:
# '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16'

z = x.__str__().replace('[', '').replace(']', '').split(', ')

print "converted to a single list \n"
print z

print "\n"

# when you print z, yo'll get:
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
# now there's one big mistake in this, 
# the data type of the values got changed.
# the integers became string, so changing them back to integers

for p in range(len(z)): z[p] = int(z[p])

print "converted the values to integer data types \n"

print z

print "\n"

# now when you print z, you'll get
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

