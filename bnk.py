userinput=raw_input('enter  a string')

t=list(userinput)

for i in t:
	print i,
meals=['rice','pappu','sambar','papad','yellow rice']
j=0
userinput=raw_input('do you want to know what is in meals ?')
if (userinput=='yes' or userinput=='YES'):
	for i in meals:
		print j*' '+i
		j+=1
elif(userinput=='no' or userinput=='NO'):
	pass



