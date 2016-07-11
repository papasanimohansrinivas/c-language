text=raw_input('enter a text')
word=raw_input('enter a word')
n1=len(text)
n2=len(word)
s=""
def replace(text,word):
	for i in range(0,n1):
		if(word[0]==text[i]):
			if(word==text[i:i+n2]):
				print text[i:i+n2]
				print i,



	return text

replace(text,word)
print replace(text,word)					