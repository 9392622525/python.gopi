import random
out=[]
while len(out)<6:
    out+=[chr(random.randint(65,90))]
    out+=[chr(random.randint(97,122))]
    out+=[str(random.randint(0,9))]
random.shuffle(out)
out2 =""
for i in out:
    out2+=i
print(out2)    
