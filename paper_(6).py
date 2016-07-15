list1=raw_input('enter the numbers').split()

list2=[int(list1[h]) for h in range(0,len(list1))]

g=max(list2)
list2.remove(g)
print max(list2)