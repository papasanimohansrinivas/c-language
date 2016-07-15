list1=[-1,1,1,1,2,3,4,5,5,5,5,5,6,7,7,8,9,8,9,0,12,11,15]
list2=[]
dicy={}
for h in range(0,len(list1)):
    dicy[list1[h]]=0

for h in dicy.keys():
    list2.append(h)

print list2

