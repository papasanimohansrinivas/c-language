s=raw_input('enter a string')
s1=""
x=len(s)
for i in s:
	s1+=s[x-1]
	x-=1

print s1	


