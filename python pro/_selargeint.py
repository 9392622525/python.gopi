a=[1,9,11,23,65,78,43]
out=a[0]
out2=a[0]
for i in a:
     if out<i:
        out=i
for i in a:
    if out2<i and i<out:
        out2=i
print(out2)        