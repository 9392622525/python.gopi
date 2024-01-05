seats=int(input('enter a seats'))
option=int(input('enter a option here'))
match option:
    case 1:
        print('daimond class')
        amt=seats*200
    case 2:
        print('golden class')
        amt=seats*150
    case 3:
        print('silver class')   
        amt=seats*100
    case _:
        print('invalid option')
        amt=None
print(amt)         
       