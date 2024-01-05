import csv 
# with open ('mca.csv','w',newline='')as csvfile:
#     data=csv.writer(csvfile)
#     data.writerow(['id','name','mobile','email'])
#     data2=[
#         [1,'jhon',8964789012,'john@example.com'],
#         [2,'alex',8964789678,'alex@example.com'],
#         [3,'rolex',8964789887,'Meenakshi'],
#     ]
#       data.writerows(data2)
# with open('mca.csv','r') as csvfile:
#     fieldnames =['id','name','mobile','email']     
#     data = csv.DictWriter(csvfile,fieldnames)
#     data.writeheader()
#     rows=[
#         {'id':1,'name':'priya','mobile':9876554334,'email':'p@gamail.com'},
#         {'name':'jhanu','id':2,'email':'j@gmail.com','mobile':7824781754},
#     ]    
#     data.writerows(rows)
# with open('mca1.csv','r') as csvfile:
#     data=csv.DictReader(csvfile)
#     for row in data:
#         print(row['name'])