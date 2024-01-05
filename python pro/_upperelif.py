char = input('enter a charecter :- ')
if 'A'<= chr <='Z':
    print('it is a uppercase character')
elif 'a'<=char <='z':
    print('it is a lower char')
elif '0' <= char <= '9':
    print('it is a digit')
else:
    print('it is a special charecter')       
