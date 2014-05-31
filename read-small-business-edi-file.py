#-*- coding: utf-8 -*-

def findNumberOfRowWithThisChain(chain):
	u"""Return number of row in file where is chain """
try:                                                             
    sourceFile = open("edi.txt", "rb", 0)
    targetFile = open("edi.xml", "a", 0)
    line = sourceFile.readlines()			                               
    try:
	for s in line:
		
		targetFile.write(s.replace("[","<"))          
        
	                    
	
	
	
    finally:         
        sourceFile.close()
 	targetFile.close()
 
 
except IOError:                                                  
    pass

return chain


