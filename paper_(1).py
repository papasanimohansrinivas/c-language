def length(list1):
	if len(list1)>=1:
		if(list1[0]==list1[-1]):
			print True
		else:
			print False
	else:
		print False

length([1,2,3,3,4,5,5,1])