s=raw_input()
i=raw_input()
y=len(i)
g=len(s)

k=i[y-1]
h=int(i[0:y-2])
	

def mutation(s,h,k):
	if(h<g):
		s=s[:h]+"k"+s[h+1:]
	print s
    
    
mutation(s,h,k) 