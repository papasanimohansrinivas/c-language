tup=(1,2,3)
3 in tup

t1=(1,2,3)
t2=(1,2,3)
#for i in (0,)

cmp(t1,t2)
max(t1)
val=input()
other_val=input()
def cmp_to_symbol(val,other_val):
	"returns the symbol representing the relationship between two values"

	return '=><'[cmp(val,other_val)]

print cmp_to_symbol(val,other_val)
