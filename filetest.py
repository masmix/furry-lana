#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import sys

def fileread(inputfile):
	u"""Read input file """
	try:
    		with io.open(inputfile, "r", encoding="windows-1250") as f:
        		for line in f:
            			print line,

	except (IOError, OSError):
    		print >> sys.stderr, "Plik nie mógł zostać odczytany."
    		sys.exit(1)

def howManyRows(inputfile):
	u"""Return number of rows in input file"""
	
	try:
		rowNumber=0
		with io.open(inputfile, "r", encoding="windows-1250") as f:
                        for line in f:
        	            rowNumber+=1,
			    #print rowNumber		
        except (IOError, OSError):
                print >> sys.stderr, "Plik nie mógł zostać odczytany."
                sys.exit(1)
	return rowNumber

if __name__ == '__main__':
    file = "edi.txt"
    fileread(file)
    x = howManyRows(file)
    #print x 

