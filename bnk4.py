string=raw_input('enter a string')
dict1={}

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

	return dict1

dict2=dict1
print Dict(string)






