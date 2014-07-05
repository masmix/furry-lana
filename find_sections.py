#-*- coding: utf-8 -*-
import find_between
import re
import peweetest

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
	name = 'Start'
	Start = {"start": "1"}
	with open('edi.txt') as line:
		for s in line:
            		
			print s	#if s.strip() == '[Dokument]':
	    		
			if re.match("\[",s):
				#print (vars()[name])
				#print dir(vars()[name])
				
				#peweetest.pushFieldToDatabase(name,vars()[name])
				name = find_between.find_between(s,'[',']')
				
				#vars()[name] = {} 			
				#print (vars()[name])
				if name == 'Info':
					Info = {}
					current_table = Info
				if name == 'Okres':
					Okres = {}
					current_table = Okres
				if name == 'Dokument':
					Dokument = {}
					current_table = Dokument
				if name == 'ZawartoscDokumentu':
					table_name = 'Paragony' 
					print Dokument
					peweetest.pushFieldToDatabase(table_name,Dokument)
					print 'Push Dokument dict as record to sql database'
					#print Dokument
				if re.match("\[Poz",s):
					poz = {}
					current_table = poz
					print "Start make 'Poz' dict" 
	    		else:
				if s == '\r\n':
					pass
				else: 
					current_table.update(returnKeyValueFromString(s))
					#if Dokument['identyfikatordok']:
					#	docId = Dokument['identyfikatordok']
					#	print docId
			#if s == '[Dokument]/r/n':
			#	documentId = Dokument['IdentyfikatorDok']
		#		print u'Here we are in Dokument dict'
		#		print  documentId
	print 'Info dict is'
	print Dokument['identyfikatordok']
	print Okres
	return Info

if __name__ == "__main__":
	print returnDictFromFile()
	
