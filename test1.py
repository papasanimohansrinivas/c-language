x=input('enter a number to find its sqaure root')

epsilon=input('set epsilon')
step=epsilon**3

numofguesses=0
check=0.0

while(abs(ans**2-x))>=epsilon:
	while(ans<x):
		numguesses=numguesses+1
		ans=ans+step