dict1={'m':3,'o':2,'n':4,'i':3,'r':2,'a':4}

dict3={}

def key(value):
	list2=[]
	for j in dict1:
		if(value==dict1[j]):
			list2.append(j)			
	return list2

def revdic(dict1):
	for value in dict1.values():
		dict3[value]=key(value)
	
	print dict3

revdic(dict1)