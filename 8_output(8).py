
dict1={'m':3,'o':2,'n':4,'i':3,'r':2,'a':4}
#dict1={'m': 2, 'b': 1, 'r': 2, 'e': 3}
dict3={}

def key(value):
	list2=[]
	for j in dict1:
		if(value==dict1[j]):
			list2.append(j)			
	return list2


for value in dict1.values():
	dict3[value]=key(value)
	

for key in dict3:
	print key,dict3[key]
