a=6
out=0
for i in range(1,a):
    if a%i==0:
        out=out+i
if out==a:
    print('perfect number')
else:
    print('not perfect number')           
