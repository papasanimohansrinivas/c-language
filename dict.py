string=raw_input('enter a string')
dict1={}
dict3={}

def frequency(i):
	count=0
	string1=string[:]
	for c in string1:
		if(i==c):
			count+=1
	return count
	
def Dict(string):
	for i in string:
		dict1[i]=frequency(i)
	print dict1

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
	
Dict(string)
revdic(dict1)


