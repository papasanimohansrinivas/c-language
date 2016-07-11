n=input('enter an integer')
root=0
count=0
n1=0
n2=0
for pwr in range(1,7):
	for root in range(1,n):
		if(root**pwr==n):
			n1=root
			n2=pwr
			count=count+1


if(count>0):
	print 'root,pwr','=',n1,n2
else:
	print 'given number doesnt have any root and pwr'
