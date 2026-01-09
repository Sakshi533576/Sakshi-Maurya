#write
# x=open("abc.txt","r")
# y=x.read()
# print(y)

# x=open("abc.txt","w")
# x.write("This is new content\n")
# x.write("Welcome tp new code")
# x.close()

# #Append
# x=open("abc.txt","a")
# x.write("Name line added")

#With append
# with open("abc.txt","a")as file:
#    file.write("India is my country\n")
#    file.write("All Indians brother and sister.\n")
# print("Data appended successfully!")
    

#for closing method
# with open("abc.txt","r")as file:
#     print(file.read()

#Remove file
# with open("abc.txt","r")as file:
#     lines=file.readlines()
#     word="Indians brother"
#     with open("abc.txt","w")as file:
#         for line in lines:
#             if word not in line:
#                 file.write(line)

#Remove Index
# remove=1
# with open("abc.txt","r")as file:
#     lines=file.readlines()
# with open("abc.txt","w")as file:
#     for i,line in enumerate(lines):
#         if i!= remove:
#             file.write(line)
    

# import os
# os.mkdir("sakshi.py")
#Rename file
# os.rename("sakshi.py","shruti")
#Remove directry
# os.rmdir("shruti")
#Remove all files
# import shutil
# shutil.rmtree("shruti")
#list all files in folder
# xyz=os.listdir(".")
# print(xyz)

# xyz=os.listdir()
# print(xyz) (".")

#@Get directory
# abc=os.getcwd()
# print(abc)

# os.mkdir("AIPA")
# with open("AIPA/student.txt","w")as file:
#     file.write("""students details:
#                sejal
#                shivali
#                soni""")
#     print("details add")

#Practice
#Create a folder
# os.mkdir("student.py")
# #create inside a folder
# os.makedirs()

# objectn oriented programming
# class student:
#     def __init__(self,name,trade):
#         self.name=name
#         self.trade=trade
# s1=student("sakshi","AIPA")
# s2=student("shipra","AIPA")
# print(s1.name,s1.trade)


# class employee:
#     def __init__(self,employeeid,employeename,salary):
#         self.employeeid=employeeid
#         self.employeename=employeename
#         self.salary=salary
# E1=employee("Ramlaal","001","20000")
# E2-employee("subedaar","002","40000")
# print(E1.name,E2.name)

# class bankaccount:
#     def __init__(self,balance):
#         self.balance=balance
#     def add(self,add):
#         self.balance+=add
#     def withdraw(self,amt):
#         self.balance-=amt
#     def finalamount(self):
#         return self.balance
# acc=bankaccount(500)
# acc.add(50)
# acc.withdraw(100)
# print(acc.finalamount())


# class bankaccount:
#     def __init__(self,balance):
#         self.balance=balance
#     def add(self,add):
#         self.balance+=add
#     def withdraw(self,amt):
#         self.balance-=amt
#     def finalamount(self):
#         return self.balance
# initial=int(input("enter your amount:"))
# deposit=int(input("enter your depositamount:"))
# credit=int(input("enter your creditamount:"))
# acc=bankaccount(initial)
# acc.add(deposit)
# acc.withdraw(credit)
# print(acc.finalamount())
#Normaly print object
# class first:
#     x=70
# obj=first()
# print(obj.x)

# class faculty:
#     #method-1
#     def putdata(self):
#         self.id=int(input("enter faculty id"))
#         self.name=input("enter your name")
#         self.salary=float(input("enter faculty salary"))
#         #method-2
#     def display(self):
#         print("faculty id:",self.id)


#         print("faculty name:",self.name)
#         print("faculty salary",self.salary)
# a=faculty()
# a.putdata()
# a.display()

# access modifiers
#public
# class AIPA:
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print(self.name)
# s=AIPA("sakshi")
# s.display()
# print(s.name)

#private
# class AIPA:
#     def __init__(self,name,tools):
#         self.name=name
#         self._tools=tools
#     def uses(self):
#         print(self._tools)
# T=AIPA("Sakshi","Almiraa")
# T.uses()
# print(T._tools,T.name)

#Protected access
# class AIPA:
#     def __init__(self,name,tools,register):
#         self.name=name
#         self._tools=tools
#         self.__register=register
#     def classregister(self):
#         print(self.__register)
# R=AIPA("Anamika","Almiraah","CR")
# print(R.name,R._tools,R._AIPA__register)
    
# class student:
#     def __init__(self,name,roll_no,marks):
#         self.name=name
#         self._roll_no=roll_no
#         self.__marks=marks
#     def display_public(self):
#         print(self.name)
#     def display_protected(self):
#         print(self._roll_no)
#     def display_private(self):
#         print(self.__marks) 
# s=student("sakshi",234,70)
# s.display_public()
# s.display_protected()
# s.display_private() 

#Inheritance
# class grandfather:
#     def house(self):
#         print("this is grandfather's house")
# class father(grandfather):
#     def car(self):
#         print("this is father's car")
# class son(father):
#     def bike(self):
#         print("this is son's bike")
#1.
# abc=son()
# abc.bike()
# abc.car()
# abc.house()

#2.
# xyz=son()
# xyz.bike()

# xyz.car()
# xyz.house()
# abc=father()
# abc.car()
# abc.house()

# class NSTI:
#     def campus(self):
#         print("This is NSTI campus.")
# class Trade(NSTI):
#     def teacher(self):
#         print("There are 40 staff.")
# class student(Trade):
#     def student(self):
#         print("There are 560 students.")
# pqr=student()
# pqr.student()
# pqr.teacher()
# pqr.campus()

# class Hotel:
#     def Manager(self):
#         print("This is paradice place.")
# class facality(Hotel):
#     def management(self):
#         print("Here is good management system.")
# class Treatment(facality):
#     def charge(self):
#         print("Nihshulk seva prapt kare.")
# abc=Treatment()
# abc.charge()
# abc.management()
# abc.Manager()

#Polyophism
# class police:
#     def work(self):
#         print("control low and order.")
# class doctor:
#     def work(self):
#         print("Treatment of patient.")
# class teacher:
#     def work(self):
#         print("Teach students.")
# xyz=[police(),doctor(),teacher()]
# for i in xyz:
#     # print(i.work)
#     i.work()

#Encpsulation
# class Student:
#     def __init__(self, name, marks):
#         self.name=name
#         self.__marks=marks
# #private
#     def get_marks(self):
#         return self.__marks
#     def set_marks(self,marks):
#         if marks >=0:
#             self.__marks=marks
# s=Student("Sakshi",20)
# print(s.get_marks())
# s.get_marks(20)
# print(s.get_marks())

# class BankAccount:
#     def __init__(self,name ,balance):
#         self.name=name
#         self.__balance=balance
#     def add_amount(self,amount):
#         self.__balance+=amount

#     def withdraw(self,amount):
#         if amount<=self.__balance:
#             self.__balance -=amount
#     def show_balance(self):
#         return self.__balance
# x=BankAccount("Sakshi",1500)
# x.add_amount(100)
# x.withdraw(500)
# print(x.show_balance())

class Tranjuction:
    def __init__(self,pin,balance):
        self.__pin=pin
        self.__balance=balance
    def check_balance(self,pin):
        if pin == self.__pin:
            return self.__balance
        else:
            return "Incorrect pin"
        
x=Tranjuction(1500,1498)
print(x.check_balance(1300))

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.__salary=salary
#         if salary > 0:
#             self.__salary = salary
#         else:
#             print("invailid salary amount")
#     def display_name(self):
#         print("Employee name:",self.name)
#     def update_salary(self, amount):
#         if amount > 0:
#             self.__salary+=amount
#             print("salary updated successful")
#         else:
            


   