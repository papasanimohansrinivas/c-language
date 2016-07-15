global L
L=[1,2,3,5,6,]
global d
d=0
global big
big=L[d]
def recursion(d):
	#big=L[d]
	if(d<len(L)):
		if big<L[d+1]:
			big=L[d+1]
		else:
			big=L[d]
	else:
		return big
	return recursion(d+1)
print recursion(d)


	
	