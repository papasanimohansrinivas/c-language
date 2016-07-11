n=input('enter a number')
x=input('enter a number')
y=input('enter a number')
def fun(n):
	if (n%2==0):
		print n,'is even'
	elif(n%2!=0):
		print n,'is odd'

fun(n)	

def swap(x,y):
	print x,y
	temp=0
	temp=x
	x=y
	y=temp
	return x,y


#swap(x,y)
print swap(x,y)

