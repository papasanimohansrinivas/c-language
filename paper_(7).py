list1=str(raw_input('enter a number ')).split()

list2=[int(h) for h in list1]
""" mean"""
sum1=0
for j in list2:
	sum1+=j

mean=sum1/len(list1)

print sum1

""" mode """

repeated={}
def frequency(h):
	global c
	c=0
	for j in list2:
		if h==j:
			c+=1
	return c

for h in list2:
	repeated[h]=frequency(h)

print repeated

reverse={}
def key(j):
	list3=[]
	for d in repeated.keys():
		if j == repeated[d]:
			list3.append(d)
	return list3

for j in repeated.values():
	reverse[j]=key(j)
k=[h for h in reverse.keys()]
g=max(k)
print 'mode','=',reverse[g]

""" median"""

list2.sort()

print list2
x=(len(list2)/2)
if(x/2%==0):
	print list2[]+list2[]


elif(x%2!=0):
	print list2[x-1/2]


