original=raw_input()
sub=raw_input()
y=len(sub)
x=len(original)
def findastring(original,sub):
	count=0
	for i in range(0,x):
		if (sub[0]==original[i]):
			if(sub==original[i:i+y]):
				count=count+1
	print count
    

findastring(original,sub)   