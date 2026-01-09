# abc=[1,2,"sakshi","shipra","soni"]
# print(abc)
# # print(abc[-1])
# print(abc[2:4])
# print(abc[4])

#Adding Element(append)
# abc=[1,2,"abc","xyz"]
# abc.append("AIPA")
# print(abc)

#insert method
# abc=[1,2,"abc","xyz"]
# abc.insert(1,"NSTI")
# print(abc)

#creating a list
#Task 1
# fruits=["apple","banana","cherry","mango","orange"]
# print("original list:",fruit)
#Task 2
#Accessing Elements to a list
# first_fruit=fruits[0]
# last_fruit=fruits[-1]
# print("first fruit:",first_fruit)
# print("last fruit:",last_fruit)
#Slicing a list
#Task 3
# sublist-fruits=fruits[:3]
# print("sublist of first three fruits:", sublist_fruits)
# flow control
# Trade=("COPA","EM","FD","DSM","AIPA")
# print("AIPA" in Trade)
# for i in Trade:
#     if i =="EM":
#         continue
#     print(i)
# print("/n EM skkiped")
# print("end of condition")

# x=[1,2,3,4,7]
# # print(max(x))
# print(min(x))
# print(sum(x))
# Average=sum(x)/len(x)
# print(Average)
# z=x.remove(2)
# print(z)
# print(x)

#Python Tuple Task Questions
#Task:1 Creating a Tuple
# x=["Apple","Orange","Banana","Pomogranate","Grapes"]
# print(x)
#Task 2: According Elements in a tuple
# Number=[10,20,30,40,50]
# print(Number[-1])
# print(Number[0])
#Task 3: Slicing a Tuple
# colors=["Red","blue","green","yellow","orange"]
# print(colors[2:5])
#Task 4: Concatenating two Tuples
# tuple1=(1,2,3)
# tuple2=(4,5,6)
# Result=tuple1+tuple2
# print(Result)
#Task 5: Iterating Through a Tuple
# Animals=("cat","Dog","rabbit","elephant")
# for i in Animals:
#     print(i)
#Task 6: Membership Test in a tuple
# Fruits=("mango","apple","cherry")
# if "apple"in Fruits:
#     print("apple is present")
# else:
#     print("apple not found")
#Task 7: Nested Tuples and Accessing Their Elements
# student=("Rahul",(85,90,92))
# print(student[1][1])
#Task 8: Applying Built-in Functions on Tuples
# Numbers=[510,15,20,25]
# print(max[Numbers])
# print(min[Numbers])
# print(length[Numbers])

# y={"AIPA","EM","COPA","DM"}
# x={"CSA","COPA","PA"}
# print(y.union(x))
# print(y.intersection(x))
# print(y.difference(x))

# print(y.issubset(x))

#dictionary

students={"name":"priya","age":"20,","trade":"aipa"}
print(students["age"])
print(students["name"])
# locals()
# globals()
print(students)

#adding new key value
# student=["marks"]=86
# student=["adress"]="gajipur"


#marging dictionary
# x={"name":"shreya","age":"20"}
# y={"trade":"aipa","adress":"prayagraj"}
# x.update(y)
# print(x)
# students={
#     "AIPA":{"name":"Shailesh","age":20,"Trade":"AIPA","Address":"Teliyarganj"},
#     "COPA":{"name":"Raj","age":20,"Trade":"COPA","Address":"Teliyarganj"},
#     "EM":{"name":"Yash","age":20,"Trade":"EM","Address":"Teliyarganj"}
# }
 
# print(students)

#copy dictionary
# students2=students.copy
# print(student2)

#clear dictionary
# students.clear()
# print(students)

#Task
# student={"name":"sakshi","age":"20","Grade":"A"}
# print(student)
# print(student["age":"20"])
# print(student["Grade":"A"])
# Employees=["Sakshi","saloni","saniya"]
# Sector=("IT")
# profile={"Manager","Assistant","Security"}
# Salary={"sakshi":"50000","saloni":"30000","saniya":"20000"}
# print(Employees)
# print(Sector)
# print(profile)
# print(Salary)
# print(Salary["saloni"])
# print(Employees[2])
# std_name=["Priya","Shipra","Shreya","Divyanshi","Komal","Pooja"]
# trade=("CTS-AIPA")
# subject={"Python","Computer Fundamentals","Database","AI","NLP"}
# marks={
#     "Priya":{"Python":70,"Computer Fundamentals":80,"Database":90,"AI":50,"NLP":60},
#     "Shipra":{"Python":78,"Computer Fundamentals":89,"Database":99,"AI":63,"NLP":61},
#     "Shreya":{"Python":70,"Computer Fundamentals":80,"Database":90,"AI":50,"NLP":60},
#     "Divyanshi":{"Python":30,"Computer Fundamentals":20,"Database":50,"AI":60,"NLP":60},
#     "Komal":{"Python":67,"Computer Fundamentals":90,"Database":100,"AI":45,"NLP":99},
#     "Pooja":{"Python":77,"Computer Fundamentals":88,"Database":55,"AI":44,"NLP":33}}
# print(std_name)
# print(trade)
# print(subject)
# print(marks)
# std_name.insert(0,"soni")
# std_name.remove("Priya")
# print(std_name)
# marks["soni"]

#Library
# Library=[
#     {"book_name":"wings of fire","writter":"a.p.j. abdul kalam","year":1999},
#     {"book_name":"the alchemist","writter":"paulo coello","year":1998},
#     {"book name":"harry potter","writter":"j.k. rowlin","year":1997}
# ]
# for book in Library:
#     print(f"{book['book_name']} - {book['writter']} ({book['year']})")
# x=5
# y=2
# print(x//2)
# my_dict={"a":1,"b":2}
# print(my_dict.get("c",5))

#Implemention of extending a list with Another List 

# def add(a,b):
# def sum(a,b):
# def squre(a):
    # return a+b

    # return 8**3 

# print(add(24,65))
# print(sum(40,25))
# print(squre(8))
# def AIPA():
#     print("this is a trade in NSTI")
# AIPA()



