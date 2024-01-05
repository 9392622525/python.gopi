user= {
    'username':'gopi',
    'password':'g1o2p3i4',
}
username=input('username please..... ')
password=input('password please..... ')
if username != user['username']:
    print('username is invalid')
else:
    print('username is valid')
if password != user['password']:
   print('password is incorrect')
else:
    print('password is valid')
