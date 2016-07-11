string=raw_input('enter a string ')

def stringreverse(string):
	x=len(string)
	new=''
	for i in range(x-1,-1,-1):
		new+=string[i]
	#print new
	return new

#def printstr(new):
#print new 

#string2=

print stringreverse(string)