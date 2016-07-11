num=input('enter a number to check whether it is prime or not ')
count1=0

for i in range(1,num+1):
	if (num%i==0):
		count1=count1+1
	
if (count1>2):
	print str(num), 'is not prime'
else:
	print str(num), 'is prime'



	