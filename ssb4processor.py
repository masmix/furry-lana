#-*- coding: utf-8 -*-
try:
	#sourceFile = open("edi.txt", "rb", 0)
	#targetFile = open("edi.xml", "w", 0)
	#line = sourceFile.readlines()
	#try:
    	with open('edi.txt') as line
		for s in line:
			if s.strip() == '[Dokument]':
				break
		for s in line:
			if s.strip() == '[ZawartoscDokumentu]':
				break
			print s

	#    targetFile.write(s.replace("[","<"))
#	finally:
 #       	sourceFile.close()
#		targetFile.close()

except IOError:
    pass

