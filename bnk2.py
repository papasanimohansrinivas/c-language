string=raw_input('enter a string')
list1=list(string)
list2=list1[:]


def frequency(c):
	List2=[]
	x=0
	list1=list(string)
	for i in list1:
		if(i==c):
			x+=1
	return x

def list3(string):
	list3=[]
	list4=[]
	for i in string:
		list3.append(i)
		frequency(i)
		list4.append(frequency(i))

	return list4	


list5=(list3(string))
dict1=zip(list1,list5)
dict1=dict(dict1)
print dict1


