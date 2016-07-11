from math import sqrt
List=[1,2,3,4,5,6,7,8,9,]

def squareroot(n):
	return sqrt(n)

def fun1(List,squareroot):
	
	x=len(List)
	for i in range(0,x):
		List[i]=(squareroot(List[i]))

	return List	
	

print fun1(List,squareroot)




