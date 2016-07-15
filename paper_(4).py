list1=str(raw_input('enter numbers ')).split()

list2=[int(h) for h in list1]

h=max(list2)
k=min(list2)
list2.remove(h)
list2.remove(k)
sum1=0
for g in list2:
	sum1+=g
print sum1
