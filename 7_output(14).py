a=[1,2,3,4,5,6]
b=[7,8,9,10,11]

def listconcat(n):
	List=[]
	t=len(n)
	if(t%2==0):
		List.append(n[(t-1)/2])
		List.append(n[(t-1)/2+1])
	else:
		List.append(n[t/2])

	return List

listconcat(a)
listconcat(b)	

print listconcat(a)+listconcat(b)
#print listconcat(b)



