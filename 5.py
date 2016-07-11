text=raw_input('enter a text')
word=raw_input('enter a word')
n1=len(text)
n2=len(word)

def replace(text,word):
	s=""
	count=0
	for i in range(0,n1):
			if word in text[i:i+n2]:
				s+=n2*'*'
				count+=1
			elif(count<2):
				s+=text[:i]
			else:
				s+=text[i:]
	return s

print replace(text,word)					