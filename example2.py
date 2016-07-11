s=raw_input('enter a string ')

def swapcase(s):
	s1=" "
	s2=" "
	for c in s:
		if(c<='z'and c>='a'):
			s1=s1+c
			print s1
		elif(c<='Z'and c>='A'):
			s2=s2+c
			print s2
	print s1,s2
	return s1,s2
	
swapcase(s)
#print s1,s2				