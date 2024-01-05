class Employee:
    company = "TESLA"
    CEO ="ELON MUK"
    def insert_member (self,name,age,sal,eid):
        self.name = name
        self.age  = age
        self.sal  = sal
        self.eid  = eid
bhanu = Employee()
bindu = Employee() 
Employee.insert_member(bhanu,'bhanu',22,50000,'tes01')       
Employee.insert_member(bindu,'bindu',21,45000,'tes02')