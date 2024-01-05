a=input('enter a statement:-')
i=0
out=''
while i< len(a):
    if'0'<=a[1]<='9':
        out=out+a[1]
    i+=1
print(out)        