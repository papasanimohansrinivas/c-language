#n=input('enter a number ')

def isprime(x):
	count=0
	for i in range(1,x+1):
		if(x%i==0):
			count+=1	
	if(count==2):
		return 1
	elif(count>2):
		return 0