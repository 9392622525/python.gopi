st=input('255.255.255.0')
temp=st.split('.')
if len(temp)==4:
    for i in temp:
        if i.isnumeric():
            out='yes'
        else:
            out='no'
            break
    
      