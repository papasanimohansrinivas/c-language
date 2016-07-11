n=input('say how many prime you want to add ')

count=0
sum=0
x=0
while(count<n):
	for i in range(1,x):
		if(x%i!=0):
			count=count+1
			sum=sum+x
	x=x+1


print sum
