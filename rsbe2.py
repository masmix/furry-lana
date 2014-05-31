#-*- coding: utf-8 -*-
try:
                                                             
	sourceFile = open("edi.txt", "rb", 0)
	targetFile = open("edi.xml", "w", 0)
	line = sourceFile.readlines()		                         
 	counterOfDocuments = 0
	numberOfRow=0	

	for s in line:
		numberOfRow+=1
		#print counterOfDocuments
		#targetFile.write(s.replace("[","<"))          
                if "[Dokument]" in s:
			#print s
			counterOfDocuments+=+1
			#print "Test 1"		     
	print numberOfRow
	print counterOfDocuments
	
	
finally:         
        		sourceFile.close()
 			targetFile.close()
		#print counterOfDocuments
		 
		 
            



