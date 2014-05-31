#-*- coding: utf-8 -*-

#CounterOfDocumens=0

def findNumber(chain):
	u"""Return number of row in file where is chain """
	try:                                                             
    		sourceFile = open("edi.txt", "rb", 0)
    		targetFile = open("edi.xml", "a", 0)
    		line = sourceFile.readlines()		                         
    		
		try:
			#CounterOfDocuments=0
			for s in line:
				print counterOfDocuments
				targetFile.write(s.replace("[","<"))          
                        # print chain in line  
				if "Rejestr=Paragony" in s:
		                   print s
				   couterOfDocuments=CounterOfDocuments+1
			print "Test 1"		     
	
	
	
 		finally:         
        		sourceFile.close()
 			targetFile.close()
			#print counterOfDocuments
			return chain 
			
 
	except IOError:                                                  
    		pass

if __name__ == "__main__":
    testChain = "Kodowanie"
    print (findNumber(testChain))	


