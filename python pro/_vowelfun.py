def index_value(a):
    out=[]
    i=0
    for i in range(0,len(a)):
        if a[i] in 'aeiouAEIOU':
            out=out+[i]
        i+=1
    return out
out=index_value("happy new year")
print(out)
        