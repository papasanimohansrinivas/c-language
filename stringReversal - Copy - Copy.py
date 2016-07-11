#name =raw_input('enter a name')

def reversestring(name):
	index=len(name)-1
	output=''
	while(index>=0):
		output+=name[index]
		index-=1
	return output


#result1=reversestring("hello")
#result2=reversestring("california")	
#result3=reversestring("democracy")

#print result1
#print result2
#print result3
