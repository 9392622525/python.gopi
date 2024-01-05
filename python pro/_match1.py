i=int(input('enter op1'))
j=int(input('enter op2'))
operator=input('enter operator')
match operator:
    case '+':
        print(i+j)
    case '-':
        print(i-j)
    case '*':
        print(i*j)
    case '/':
        print(i/j) 
    case '**':
        print(i%j)     
    case _:
        print('check operator')
        
        