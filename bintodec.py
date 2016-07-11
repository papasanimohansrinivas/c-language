n=raw_input('enter a binary no')
sum=0
i=0
for c in n[::-1]:
	print int(c)
	sum=sum+int(c)*2**i
	i=i+1


print sum