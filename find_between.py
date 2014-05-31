#-*- coding: utf-8 -*-


def find_between( s, first, last ):
    u"""Zwraca łańcuch znaków pomiędzy znakiem początkowym, a końcowym"""	
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
    	return ""

if __name__ == "__main__":
        s = "[Info]"
	print (find_between(s,'[',']'))
