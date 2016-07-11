string=raw_input()
newString=''
x=len(string)

for i in range(0,x):
    if(string[i]==string[i+1]):
        pass
    else:
        newString+=string[i]
        
print newString