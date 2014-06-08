#-*- coding: utf-8 -*-
import find_between
import re

def returnKeyValueFromString(string):
	"""Return record key,value from line with string contain '=' separator"""
	record = {}
	name, value = string.partition("=")[::2]
        name = name.lower()
	value = value.rstrip('\r\n')
	value = value.decode("windows-1250")
	value = value.encode("utf-8")
	record[name] = value
	#print record
	return record

def returnDictFromFile():
	"""Return Info dict from edi.txt file"""
	Info = {}
	Okres = {}
	Dokument = {}
	Dokument['identyfikatordok']=0
	with open('edi.txt') as line:
		for s in line:
            		#if s.strip() == '[Dokument]':
	    		if re.match("\[",s):
				name = find_between.find_between(s,'[',']')
				#print name
				vars()[name] = {} 			
				#print (vars()[name])
				if name == 'Dokument':
                                	print u'Here we are in Dokument dict'
				if name == 'ZawartoscDokumentu':
					print 'Push Dokument dict as record to sql database'
				if re.match("\[Poz",s):
					print "Start make 'Poz' dict" 
	    		else:
				if s == '\r\n':
					pass
				else: 
					vars()[name].update(returnKeyValueFromString(s))
					if Dokument['identyfikatordok']:
						docId = Dokument['identyfikatordok']
			if s == '[Dokument]/r/n':
				documentId = Dokument['IdentyfikatorDok']
				print u'Here we are in Dokument dict'
				print  documentId
	print 'Info dict is'
	print Dokument['identyfikatordok']
	print Okres
	return Info

if __name__ == "__main__":
	print returnDictFromFile()
	
