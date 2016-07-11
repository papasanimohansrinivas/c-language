y=float(raw_input('enter a number'))
epsilon =0.01
guess=y/2.0

while abs(guess*guess-y)>=epsilon:
	guess=guess-(((guess**2)-y)/(2*guess))
	print (guess)
	print 'Square root of',y,'is about ',guess