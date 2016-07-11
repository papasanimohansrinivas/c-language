string=raw_input('enter a name ')

x=len(string)
c=0
for x in range(0,x):
	if string[x]==string[-x-1]:
		c=c+1
	else:
		print string, 'is not palindrome'

if c==x:
	print string,'is palindrome'