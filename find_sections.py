#-*- coding: utf-8 -*-
import find_between
import re

def returnKeyValueFromString(string):
	"""Return record key,value from line with '=' separator"""
	record = {}
	name, value = string.partition("=")[::2]
        value = value.rstrip('\r\n')
	#value = value.decode("utf-8")
	record[name] = value
	#print record
	return record


with open('edi.txt') as line:
	for s in line:
            #if s.strip() == '[Dokument]':
	    if re.match("\[",s):
		name = find_between.find_between(s,'[',']')
		#print name
		vars()[name] = {} 			
		#print (vars()[name])
	    else:
		if s == '\r\n':
			pass
		else: vars()[name].update(returnKeyValueFromString(s))




print 'Info dict is"'
print Info 
#print Info['Program']
