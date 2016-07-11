count=0
for i in range(1,101):
	if(len(str(i))>=2):
		if(int(i)%10==7):
			count+=1
			print i,
		if(int(i)/10==7):
			count+=1
			print i,	
	elif(len(str(i))<2):
		if(i==7):
			count+=1
			print i,

print '\n','number of numbers with digit "7" is ',count
