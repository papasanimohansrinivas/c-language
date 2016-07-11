n=input('enter a number ')

from isprime import isprime

def primedivs(n):
	count=0
	for i in range(1,n+1):
		if(isprime(i)==1):
			if(n%i==0):
				print i

primedivs(n)