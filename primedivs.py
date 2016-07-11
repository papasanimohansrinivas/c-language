


def primedivs(n):
	count=0
	s=""
	for i in range(1,n):
		if(isprime(i)==1):
			if(n%i==0):
				s=s+str(i)
	return s