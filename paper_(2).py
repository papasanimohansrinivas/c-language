list1=[0,1,2,3,4,5,6,7,8,9]
list2=[5,6,7,8,9,10,11,12,13,14]
#list2=[0,1,2,3,4,5,6,7,8,9]
def intersect(list1,list2):
	list3=[]
	for j in list1:
		if j in list1:
			if j in list2:
				list3.append(j)
	return list3
print intersect(list1,list2)
global l
l=intersect(list1,list2)

def union(list1,list2):
	list4=[]
	list4.extend(list1)
	list4.extend(list2)
	for j in list1:
		if j in list1:
			if j in list2:
				list4.remove(j)
	return list4
print union(list1,list2)

def unique(list1,list2):
	list5=[]
	list6=list1[:]
	list7=list2[:]
	for j in list1:
		if j in list1:
			if j in list2:
				list6.remove(j)
				list7.remove(j)
	list5.extend(list6)
	list5.extend(list7)
	return list5	
print unique(list1,list2)
