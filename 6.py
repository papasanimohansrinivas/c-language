string=raw_input('enter a string')
char=raw_input('enter a character')
count=0
def no_of_times(char,string):
	for i in string:
		if(i==char):
			count=count+1
	return count


print no_of_times(char,string)
