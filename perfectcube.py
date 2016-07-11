n=input('give a number to test it is perfect cube or not ')
count=0
for i in range(1,n):
	if(i**3==n):
		count=count+1


if(count==1):
	print 'given no is perfect cube'
else:
	print'given no is not perfect cube'
