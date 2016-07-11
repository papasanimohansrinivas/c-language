n=input('enter a number to check whether it is prime or not ')
count=0
for x in range(1,n+1):
	if n%x==0:
		count=count+1
	if count>2:
		print 'given number is not prime '
		break
	if count<=2:
		print 'given number is prime'