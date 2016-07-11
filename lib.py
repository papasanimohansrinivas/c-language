

dict1={'m':3,'o':2,'n':4,'i':3,'r':2,'a':4}
print dict1
value=int(raw_input('please give a value '))
def key(value):
	list1=[]
	for j in dict1:
		if(value==dict1[j]):
			list1.append(j)
	return list1

print key(value)






	