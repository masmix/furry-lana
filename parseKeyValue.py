record = {}
with open("edi.txt") as myfile:
    for line in myfile:
        name, value = line.partition("=")[::2]
	record[name] = value
print (record)
	
#        myvars[name.strip()] = float(var)
#names = type("Names", [object], myvars)

#print names.var1
