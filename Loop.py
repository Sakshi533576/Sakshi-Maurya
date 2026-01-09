# for i in range (4,11):
#     print(i)
# Name print
# for i in "SAKSHI":
#     print(i )

#print for Table
# for i in range (1,11):
#     print(9,"x",i,"=",9*i)
# else:
#     print("Table completed")
#for odd
# for i in range (1,11,2):
#     print(i)
# else:
#     print("odd number")

# PRINT FOR EVEN NUM
# for i in range (2,10,2):
#     print(i)
# else:
#     print("even number")
# for i in range(1,10):
#     print(i**2)
# else:
#     print("square")
# Reverse order
# for i in range(10,0,-1):
#     print(i)
#sum of first 10 natural num
# total = sum(range(1,11))
# print(total)
# the factorial of a given number
# num=int(input("enter a number to find its factorial:"))
# factorial = 1
# for i in range(1,num +1):
#     factorial= factorial*i
# print("factorial of",num, "is",factorial)
# while loop
# num=50
# while num>0:
#     print(num)
#     num-=1
# print("loop ends here")
# password= ""
# while password!=("sakshi@123"):
#     password= input("enter your password:")
# print("login successful")

# apple = 10
# while apple>0:
#     print("eat apple:",apple)
#     apple-=1
#     print("finish")
# Added import time
# import time
# money=0
# while money<100000:
#     money+=50
#     print("added money",money)
#     time.sleep(1)
# print("contribute done",10000)

# using both forloop or whileloop
# classname=1
# while classname<11:
#     print("class:",classname)
#     for i in range(1,11):
#         print(i,end=" ")
        
#     print("\n Attendence Done")
#     classname +=1
# print("exit")

# votelistname = 0
# while votelistname<1000:
#     print("vote:",votelistname)
#     for i in range(1,11):
#         print(i,end=" ")
#     print("\n Votting done")
#     votelistname+=1
# print("Thankyou")

# loop from 1 to 10
# for i in range (1,11):
#     if i ==6:
#         continue
#     else:
        
#      print (i,end=" ")


# for round in range (1,4):
#     print("Round:",round)
#     count=3
#     while count>0:
#         print("countdown:",count)
#         count-=1

#     print("Round compeleted!")
#     print("next round")
#Num=3 table
# for i in range (1,11):
#      print(3,"x",i,"=",3*i) 
# else:
#      print("Table completed")

# for i in range (1,11):
#      print(2,"x",i,"=",2*i) 
# else:
#      print("Table completed")

# for i in range (1,11):
#      print(4,"x",i,"=",4*i) 
# else:
#      print("Table completed")

# Round=1
# while Round<=3:
#     print("Round",Round,end=" ")
#     for i in range (Round):
#         print("*",end=" ")
#     print()
#     Round+=1

# Day=1
# while Day<=3:
#     print("Day",Day,end=" ")
#     for i in range(Day):
#         print("Morning,Afternoon,Evening",end=" ")
#     print()

#     Day+=1

# User=1
# OriginalBalance={1:1000,2:5000,3:6000,4:8000}
# while User<=3:
#     print("User:",User)
#     balance=10000
#     for i in range(1,4):
#         amount=int(input("enter your amount:"))
#         if amount<=balance:
#             balance=balance-amount
#             print("Remaining Balance:",)
#         else:
#             print("Insufficient Balance")
#     print("User:",User,"Transanction completed")
#     User+=1

# User=1
# OriginalBalance={1:1000,2:5000,3:6000,4:8000}
# while User<=3:
#     print("User:",User)
#     balance=10000
#     for i in range(1,4):
#         amount=int(input("enter your amount:"))
#         if amount<=balance:
#             balance=balance+amount
#             print("Remaining Balance:",)
#         # else:
#         #     print("Insufficient Balance")
#     print("User:",User,"Transanction completed")
#     User+=1
    
# customer=1
# while customer<=2:
#     print("customer:",customer)
#     total=0
#     for i in range(1,3):
#         amount=int(input("enter your amount:"))
#         total=total+amount
#     print("total bill:",total)
#     print("Next customer")
#     customer+=1

# Lo
# 
# 
# an Amount
# customer=1
# while customer<=3:
#     print("customer:",customer)
#     LoanAmount=int(input("enter your loan Amount:"))
#     rate=int(input("enter your rate:"))
#     year=int(input("enter your year:"))
#     for i in range(year):
#         amount=LoanAmount*(rate/100)
#         LoanAmount=LoanAmount+amount
#     print("Loan Amount:",LoanAmount)
#     print("Next Customer")
#     customer+=1

# student=1
# while student<=3:
   
#     print("student:",student)
#     total=0
#     for i in range(1,6):
#         Marks=int(input("enter your marks:"))
#         total=total+Marks
#         Average=total/5
#     print("Total",total)
#     print("Average:",Average)
#     print("Next student")
#     student+=1


# x="py"
# y="thon"
# print("py" + "thon")
# x=7 
# y=3

# for i in range (1,11):
#     if i ==6:
#         continue
#     print(i)

# for i in range (1,11):
#     if i ==5:
#         continue
#     print(i)


# for i in range(1,10):
#    if i==4:
#       continue
#    if i ==5:
#       continue
#    print(i)

# for i in range(1,5):
#     if i==3:
#         pass
#     print(i)

# for i in range(1,10):
#     if i==4:
#         continue
#     if i==5:
#         continue
#     if i==8:
#         break
#     print(i)
    # Emloyees salary entry
# Employees=1
# while Employees<5:
#     print("Employees:",Employees)
#     Day=int(input("enter day:"))
#     Income=int(input("enter you perday income:"))
#     for i in range(Day):
#         Salary=Day * Income
#         Total=Salary
#     print("Total:",Total)
#     Employees+=1
#
# x = 5
# while x > 0:
#     x -= 2
my_tuple = (1, [2, 3], 4)
my_tuple[1].append(5)
print(my_tuple)