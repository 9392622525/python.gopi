a=[]
def add_int(a,i=0):
    if len(a)-1==i:
        return a[i]
    return a[1]+add_int(a,i+1)
out=add_int(a)
print(out)
