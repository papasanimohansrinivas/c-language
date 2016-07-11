original=raw_input()
sub=raw_input()
y=len(sub)
def findastring(original,sub):
    for i in original:
        if (sub[1]==i):
            for j in range(i,i+y):