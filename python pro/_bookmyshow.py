def book_my_show():
    print('welcome to book my show')
    name=input('please enter your name:')
    print('select number of seats:')
    print("enter '1' for daimond:200")
    print("enter '2' for gold:150")
    print("enter '3' for silver:100")
selected_seats=[]
num_seats=int(input('enter the number of seats, you want book:-'))
seat_choice=input("enter your choice(1,2,3):")
if seat_choice=='1':
    selected_seats.append(200)
elif seat_choice=='2':
    selected_seats.append(150)
elif seat_choice=='3':
    selected_seats.append(100)
print        



    

