# writing a program to swap numbers

def swappingNumbers(number1,number2):
	temporary=number1
	number1=number2
	number2=temporary
	print "after swapping:"
	print "number1:",number1
	print "number2:",number2


number1=int(raw_input('enter the first number:'))

number2=int(raw_input('enter the second number:'))
print "before swapping:"
print "number1:",number1
print "number2:",number2
swappingNumbers(number1,number2)

print "global variable:number1",number1
print "global variable:number2",number2

