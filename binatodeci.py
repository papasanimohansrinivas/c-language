n=raw_input('enter a binary no')
sum=0
x=len(n)
for i in range(1,x):
	for c in n[::-1]:
		sum=sum+int(c)*2**i


print sum