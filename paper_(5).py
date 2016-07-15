global L
L=[1112,1,2,3,1112,5,3,-3,2,1233,3,-8,8,6]
big=L[0]
def recursion(d):
	global big
	if(d==len(L)):
		return big
	else:
		if(d<len(L)):
			if big<L[d]:
				big=L[d]
	return recursion(d+1)
print recursion(0)