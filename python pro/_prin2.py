def fname(a):
        if 'A'<=a<='Z':
            return True
        else:
            return False
out=filter(fname,'2BC@15$67DEfgh')
print(list(out))        

