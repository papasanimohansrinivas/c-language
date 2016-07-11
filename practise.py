input_number=int(raw_input())
total=0
count=0
number=1
while count<input_number:
	if number%2 is 0:
		total+=number
		count+=1
	number+=1
print total