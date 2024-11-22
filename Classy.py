# # # import myModule
# # # print(myModule.greet("Mayowa"))
# # # print(myModule.pi)


# # # from mypackage import module1
# # # print(module1.firstmodule())


# # # from mypackage import module2
# # # print(module2.secondmodule())


# # # from myModule import greet,pi
# # # print(greet("Samson"))
# # # print(pi)

# # # import myModule as mm
# # # print(mm.greet("Mujeeb"))


# # import requests

# # from data_processing.file_reader import read_data
# # from data_processing.web_fetcher import fetch_user_data

# # data = read_data('data.txt')

# # web_data = fetch_user_data()

# # print("Data from file: ")
# # for name,age in data:
# #     print(f"\t- {name} ({age} years old)")
# # print("\nData from web: ")
# # print("\t-"+", ".join(web_data))

# # # def main():
# # #     data = read_data('data.txt')

# # #     user_data = fetch_user_data()

# # #     print("Data from file:")
# # #     for name, age in data:
# # #         print(f"{name}: {age}")

# # #     print("\nUser data from web:")
# # #     for user in user_data:
# # #         print(user)

# # # if __name__=="__main__":
# # #     main()


# # # def read_data():
# # #     with open('data.txt','r') as file:
# # #         print(file.readlines())
              

# # # import requests

# # # from data_processing.file_reader import read_data
# # # # with open("data.txt","r") as file:
# # # #     print(file.readlines())


# # # # print(read_data('data.txt'))

# # # Replacing multiple space with a single space
# # import re
# # text = "This  is  a test"
# # pattern = r"\s+"
# # new_test = re.sub(pattern," ",text)
# # print("New text:",new_test)

# # import re
# # file_path = "reviews.txt"
# # email_pattern = r"[a-zA-Z0-9_.+-]@[a-zA-Z0-9-.]+"
# # phone_pattern = r"\+\d{1,2} \d{3} \d{3} \d{4}"
# # with open(file_path, 'r') as reviews_file:
# #     for line in reviews_file:
# #         emails = re.findall(email_pattern, line)
# #         phones = re.findall(phone_pattern, line)
# #     print(reviews_file.readlines())


# 1+1

# 2*6

# 3/1

# 3-4

# (90*7)/2

# Mod/ Mod Operators

# 7 % 2 # Return only the remainder

# a = 3.25

# import time

# start_time  = time.time()
# print(a)
# end_time  = time.time()
# print(start_time-end_time)

# a%1

# a//1

# 8 + 5*9+1

# 8**1

# 8**12

# Variable Assignment


# a = 10

# a

# a = 5

# print("a")

# a

# a = a+a

# a

# type(a)

# my_income = 5000


# My_Tax_rate = 0.5

# Total = my_income * My_Tax_rate

# Total

# Strings


# "Hi, how are you"

# "I'm fine and you?"

# print('Hello world')
# print("Hi World")

# print('Hello \nworld')  # \n will bring the next character down

# print('Hello \t world')

# len("I am")   # len is used to find the length of character

# len("I am happy")

# mystring = "Hello Baby"

# mystring

# mystring[0]

# mystring[-1]

# mystring = "abcdefghijk"

# mystring

# mystring

# mystring[-1]

# mystring[1:]

# mystring[-2:]

# mystring[5:]

# mystring

# mystring[:3]

# mystring[:-1]

# mystring

# mystring[1:5]

# mystring[3:9]

# mystring[::-1]

# mystring[::1]

# mystring[2]

# mystring[::4]

# mystring[::2]

# mystring[2:7:2]

# mystring

#  mystring[::-1]

# mystring[::3]

# String Properties and Method


# Immutability

# name = "Mayowa"

# name[0] ="H"  #Sring is immutable that is it cannot change


# name = "Mayowa"

# name

# I want to replace the first letter "M" with  "B"

# last_name_part = name[1:]

# last_name_part

# First_letter = "B"

# First_letter

# New_Name =First_letter + last_name_part  # Concart with "+"

# New_Name

# name = "Hello World"

# name + " it is a beautiful morning"

# x = name + " it is a beautiful morning"

# print(x)

# x

# "2" + "3"

# 2+3

# x *10

# "z"*10

# "a"*10

# x = "Enjoyment Galore"

# x.upper()

# x.lower()

# x = "enjoyment galore"

# Upper_E = x[1]

# print(Upper_E)


# x.split()

# x = "Hi, this is a string"

# x

# x.split("i")

# print("This is a string {}".format("Inserted"))

# Formatting with the string.format()

# print("The {} {} {} ".format("Fox","Quick","Brown"))

# print("The {0} {0} {0} ".format("Fox","Quick","Brown"))

# print("The {1} {2} {0} ".format("Fox","Quick","Brown"))

# print("The {q} {b} {f} ".format(f ="Fox",q= "Quick",b= "Brown"))  #more readable

# float formatting

# result = 100/700

# result

# result

# print("The result of the calculation is {r} ".format(r=result))

# float formatting follows "{values:width.precisionf}"

# print("The result of the calculation is {r:1.3f} ".format(r=result))    #The "1" means the width 3 means decimal places

# Name = "Mayowa"

# print("Hello, my name is {}".format(Name))

# print(f"Hello, my name is {Name}")

# Name = "Mayowa"
# Age = 23

# print(f"{Name} is {Age} years old")

# Lists

# My_List = [1,2,3]

# My_List

# My_List = ["Mayowa",100,100.23]

# len(My_List)

# My_List = ["One","Two","Three"]

# My_List[0]

# My_List[2]

# My_List[::]

# My_List[-1]

# My_List[2:]

# My_List[::]

# My_List  

# Another_List =["Four","Five","Six"]

# My_List + Another_List

# My_List_New =My_List + Another_List

# My_List_New

# My_List_New[0]="ONE"    # Replaced One with ONE

# My_List_New

# My_List_New.append("Seven")     #Added new list "Seven"

# My_List_New

# My_List_New.append("Eight")

# My_List_New

# My_List_New.pop()   #Pop is used to remove

# My_list = My_List_New.pop()

# My_list

# My_List_New

# My_List_New.pop(3)

# My_List_New

# New_List = ["a","x","q","u"]

# New_List.sort()

# New_List =[33,3,445,67,23,5,9]

# New_List.sort(reverse=True)
# New_List

# list = ["one","two","three","Four","Five","Six"]

# list.append("Seven")

# list


# new_list = [0,21,23,4,1,3]
# new_list.pop()

# new_list

# new_list.sort(reverse=True)

# new_list

# new_list.extend([30])

# new_list

# new_list.insert(0,39)

# new_list

# new_list.insert(3,39)

# new_list

# new_list.count(30)

# new_list.index(30)

# new_list.pop(0)

# new_list

# new_list.remove(1)

# new_list

# new_list.reverse()

# new_list

# new_list.copy()

#                                     Dictionary

# My_Dict = {"key1":"Value1","key2":"Value2","key3":"Value3"}

# My_Dict

# My_Dict["key1"]

# My_Dict["key3"]

# Price_lookup = {"Apple":2.99,"Orange":3.88,"Milk":1.90}

# Price_lookup["Apple"]

# d_new = {"K1":2345,"K2":"Happy","Insertedkey":{"k4":1}}

# d_new

# d_new["K1"]

# d_new["Insertedkey"]

# d_new["Insertedkey"]["k4"]

#  d_new = {"K1":2345,"K2":"Happy","Insertedkey":{"k4":1},"k3":[1,2,3,4]}

# d_new["k3"]

# d_new["k3"][3]

# da = {"key1":["a","b","c"]}

# da

# my_list = da["key1"]

# my_list

# letter = my_list[2]

# letter

# letter.upper()

# Dic ={"one":1,"two":2,"three":3}

# Dic["four"]=4

# Dic

# d ={"key1":["a","b"]}

# d["key2"]=7

# d

# d['key3']={"ama":2}

# d

# d["Key2"]=4

# d

# d ={"key1":["a","b"]}

# d

# d["key1"]=3

# d

# d.keys()

# d.values()

# d.items()

#                             Tuples
                           

# t = 1,2,3,4

# mylist = list(t)

# mylist

# mylist[1]=5

# t = tuple(mylist)

# t

# t[::]

# t[2:]

# t = ("one",1,1,1,1,"two","two","two")

# len(t)

# t.count(1)

# t.count("two")

#                             Set

# my_set = set()

# my_set

# my_set.add(1)

# my_set

# my_set

# my_set.add(2)

# my_set

# my_set.add(2)

# my_set 

# my_list = [1,1,1,1,1,2,2,3,3,3,4,6,"one","two"]

# newlist = set(my_list)

# newlist

#                 Booleans

# True

# False

# 1==1

# 1 >2

# type(200083*3==73)

# type(False)

# b = None

# b

# pwd

# 9//2

# Write_an_article = "I am a boy"   #The article

# print(Write_an_article)

# options = ["yes","No"]

# Question = "Do you want to make any changes in the article? " + options[0]

# print(Question)

# The_replacement= " girl"

# Half_article= "I am a"

# article = Half_article + The_replacement

# print(article)

# S= [0,0,0]

# print(S)

# [0]*3

# list3 = [1,2,[3,4,'hello']]


# list3[2][2]="GoodBye"

# print(list3)

# d = {'k1':{'k2':'hello'}}
# # Grab 'hello'

# d["k1"]["k2"]

#  # Getting a little tricker
# d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

# #Grab hello

# d["k1"]

# d["k1"][0]

# d["k1"][0]["nest_key"]

# d["k1"][0]["nest_key"][1][0]

# d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
# # Grab Hello

# d["k1"]

# d["k1"][2]

# d["k1"][2]["k2"]

# d["k1"][2]["k2"][1]

# d["k1"][2]["k2"][1]["tough"]

# d["k1"][2]["k2"][1]["tough"][2]

# d["k1"][2]["k2"][1]["tough"][2][0]

# list5 = [1,2,2,33,4,4,11,22,3,3,2]

# set(list5)

#             Comparation Operation

# 1<2

# 2<3

# 1==1

# 2==2

# 1<2<3

# 100 ==1 and 10*2

# 10==1 or 4==4

# not(10==1 or 4==4)

# Control flow Python Statement if, elif, else statement

# if True:
#     print("It's True")

# Hunger = True
# if Hunger:
#     print("Feed ME")
# else:
#     print("I'm not hungry")

# Student = False
# if Student:
#     print("Good Boy")
# else:
#     print("Bad Boy")

# Student = "Tom"

# if Student == "Mayowa":
#     print("Close")
# elif Student == "Bayo":
#     print("Good")
# elif Student == "Tom":
#     print("Not Okay")
# else:
#     print("false_Info")


# Article = "I am a boy"

# if Article == "I am a boy":
#     print("True")
# elif Article == "I am a girl":
#     print("False")
# else: 
#     print("No info")

# Name = "Ana"

# if Name == "Dan":
#     print("Hello Dan")
# elif Name == "Mayowa":
#     print("Hello Mayowa")
# elif Name == "Tom":
#     print("Hello Tom")
# else:
#     print("What is your name?")

# article = input("enter your article here: ")
# print("do u wish to change a word? ")
# res = input("enter 'yes' if you want to make a change and 'no' if u don't: ")
# if res == "yes":
#     old_word = input("which word would you like to change? ")
#     new_word = input("which word would you like to replace the old word with? ")
#     print(article.replace(old_word,new_word))
    
# else:
#     print(article)

# name  = ["ade", "tunde"]  #don't repeat yourself
# # name.append("femi")
# # name.append("tola")
# # name.append("lanre")
# new_name = ["femi", "tola", "lanre"]
# for i in new_name:
#     name.append(i)
# name

# questions = ["1.what is science", "2. what is your name"]
# options = ["a. yryry/n b.hdhdhdh", "a.djdjdj"]
# answer = ["a", "b"]


# Article = input("Enter your article here: ")
# print("Do you want to make any changes in the article? ")
# res = input("enter 'yes if you want to make a change and 'no' if you don't want to: ")
# if res = "Yes":
#     old_word = input("Which word would you like to change? ")
#     new_word = input("Which word would you like to replace the old word with? ")
# print(Article.replace(old_word,new_word))
# else:
#     print(Article)
    

# Article = input("Enter your article here: ")
# print("Do you want to make any changes in the article? ")
# res = input("enter 'yes' if you want to make a change and 'no' if u don't: ")
# if res == "yes":
#     old_word = input("Which word would you like to change? ")
#     new_word = input("Which word would you like to replace the old word with? ")
#     print(Article.replace(old_word,new_word))
# else:
#     print(Article)

# Article =input("Enter your article here: ")
# print("Do you want to make any changes? ")
# res = input("enter 'yes' if you want to make a change and 'no' if you dont want to make a change: ")
# if res == "yes":
#     old_word = input("which word would you like to change? ")
#     new_word = input("which word would you replace the old word with? ")
#     print(Article.replace(old_word,new_word))
# else:
#     print(Article)

# Names = ["Mayowa","Timi","Sola"]
# New_Name = ["Dan","Boye","Bose"]
# for i in New_Name:
#     Names.append(i)
#     print(Names)


# name  = ["ade", "tunde"]  #don't repeat yourself
# # name.append("femi")
# # name.append("tola")
# # name.append("lanre")
# new_name = ["femi", "tola", "lanre"]
# for i in new_name:
#     name.append(i)
# name

#  My_List = [1,2,3,4,5,6,7,8,9,10]

# for num in My_List:
#     print("Hello")

# for num in My_List:
#     if num %2 == 0:
#         print(num)

# for num in My_List:
#     if num %2 == 1:
#         print(num)

# for num in My_List:
#     if num %2 ==1:
#         print(num)
#     else:
#         print(f"The even number is {num}")

# questions = ["1.what is science", "2. what is your name"]
# options = ["a. yryry/n b.hdhdhdh", "a.djdjdj"]
# answer = ["a", "b"]


# a = 5
# a += 1
# a = a + 1

#    # Define the questions, options, and the correct answers as seperate lists
# questions = ["What is 2+3?","What is 7-2?","What is 5*3?","What is 12/4?","What is 9+6?"]
# options =[ ["A. 4","B. 5"],["A. 5","B. 1"],["A. 15","B. 8"],["A. 3","B. 5"],["A. 10","B. 15"]]
# answer =["B","A","A","A","B"]
# # Initialize score 
# score = 0
# # Loop through each question 
# for question in range(len(questions)):
#     print(questions[question])
#     for option in options[question]:
#         print(option)
#     user_answer = input("Please enter the letter of your answer: ").strip().upper()
#     #Check if the answer is correct
#     if user_answer == answer[question]:
#         print("correct")
#     else:
#         print("wrong")
#     if user_answer == answer[question]:
#         score += 5
# print(f"\nYour final score is: {score} out of {25}")

# for loop

# mylist = [1,2,3,4,5,6,7,8,9,10]

# mylist = [1,2,3,4,5,6,7,8,9,10]
# list_sum = 0
# for name in mylist:
#     list_sum = list_sum + name

#     print(list_sum)

# My_letter = ("Hello Wordld")
# for new in My_letter:
#     print(new)

# for new in "Hello World":
#     print(new)

# for new in "Hello World":
#     print("Cool")

# tup = (1,2,3,4)
# for item in tup:
#     print(item)

# mylist = [(1,2),(3,4),(5,6),(7,8)]
# len(mylist)

# mylist = [(1,2),(3,4),(5,6),(7,8)]
# for item in mylist:
#     print(item)

# #Tuples unpacking
# mylist = [(1,2),(3,4),(5,6),(7,8)]
# for a,b in mylist:
#     print(a)
#     print(b)

# mylist = [(1,2,3),(4,5,6),(7,8,9)]
# for new in mylist:
#     print(new)

# mylist = [(1,2,3),(4,5,6),(7,8,9)]
# for a,b,c in mylist:
#     print(a)

# d = {"k1":1,"k2":2,"K3":3}
# for item in d.keys():
#     print(item)

# d = {"k1":1,"k2":2,"K3":3}
# for item in d.values():
#     print(item)

# d = {"k1":1,"k2":2,"K3":3}
# for item in d.items():
#     print(item)

# x = 0
# while x < 8:
#     print(f"The current value of x is {x}")
#     x = x+1 #or x += 1
# else:
#     print("X is not less than 5")

# x = 50
# while x < 5:
#     print(f"The current value of x is {x}")
#     x = x+1 #or x += 1
# else:
#     print("X is not less than 5")

# Break, Continue, Pass

# #Pass
# mylist = [1,2,3,4,5]
# for item in mylist:
#     # Comment
#     pass
# print("end of my script")

# #Continue
# mystring = "Sammy"
# for i in mystring:
#     if i == "a":
#         continue
#     print(i)

# mystring = ("Sammy")
# for i in mystring:
#     print(i)
    

# # break
# #Continue
# mystring = "Sammy"
# for i in mystring:
#     if i == "a":
#         continue
#     print(i)

# x = 0
# while x < 5:
#     if x==2:
#         break
#     print(x)
#     x += 1

# Useful Operator
# Range

# for list in range(10):
#     print(list)

# for number in range(3,10):
#     print(number)

# for number in range(2,10,2):
#     print(number)

# range(0,11,2)

#    # Define the questions, options, and the correct answers as seperate lists
# questions = ["What is 2+3?","What is 7-2?","What is 5*3?","What is 12/4?","What is 9+6?"]
# options =[ ["A. 4","B. 5"],["A. 5","B. 1"],["A. 15","B. 8"],["A. 3","B. 5"],["A. 10","B. 15"]]
# answer =["B","A","A","A","B"]
# # Initialize score 
# score = 0
# # Loop through each question 
# for question in range(len(questions)):
#     print(questions[question])
#     for option in options[question]:
#         print(option)
#     user_answer = input("Please enter the letter of your answer: ").strip().upper()
#     #Check if the answer is correct
#     if user_answer == answer[question]:
#         print("correct")
#     else:
#         print("wrong")
#     if user_answer == answer[question]:
#         score += 5
# print(f"\nYour final score is: {score} out of {25}")

#    # Define the questions, options, and the correct answers as seperate lists
# questions = ["What is 2+3?","What is 7-2?","What is 5*3?","What is 12/4?","What is 9+6?"]
# options =[ ["A. 4","B. 5"],["A. 5","B. 1"],["A. 15","B. 8"],["A. 3","B. 5"],["A. 10","B. 15"]]
# answer =["B","A","A","A","B"]
# # Initialize score 
# score = 0
# # Loop through each question 
# for question in range(len(questions)):
#     print(questions[question])
# for option in options[question]:
#         print(option)

# questions = ["What is 2+3?","What is 7-2?","What is 5*3?","What is 12/4?","What is 9+6?"]
# options =[ ["A. 4","B. 5"],["A. 5","B. 1"],["A. 15","B. 8"],["A. 3","B. 5"],["A. 10","B. 15"]]
# answer =["B","A","A","A","B"]
# # Initialize score 
# score = 0
# # Loop through each question 
# for question in range(len(questions)):
#     print(questions[question])
#     for option in options[question]:
#         print(option)
#     user_answer = input("Please enter the letter of your answer: ").strip().upper()
#     #Check if the answer is correct
#     if user_answer == answer[question]:
#         print("correct")
#     else:
#         print("wrong")
# # if user_answer == answer[question]:
# #         score += 5
# # print(f"\nYour final score is: {score} out of {25}")

# questions = ["What is 2+3?","What is 7-2?","What is 5*3?","What is 12/4?","What is 9+6?"]
# options =[ ["A. 4","B. 5"],["A. 5","B. 1"],["A. 15","B. 8"],["A. 3","B. 5"],["A. 10","B. 15"]]
# answer =["B","A","A","A","B"]
# # Initialize score 
# score = 0
# # Loop through each question 
# for question in range(len(questions)):
#     print(questions[question])
#     for option in options[question]:
#         print(option)
#     user_answer =input(f"Please enter the letter of your answer: ").strip().upper()
#     if user_answer == answer[question]:
#         print("correct")
#     else:
#         print("wrong")
#     if user_answer == answer[question]:
#         score += 5
# print(f"\nYour final score is: {score} out of {25}")


# #    # Define the questions, options, and the correct answers as seperate lists
# # questions = ["What is 2+3?","What is 7-2?","What is 5*3?","What is 12/4?","What is 9+6?"]
# # options =[ ["A. 4","B. 5"],["A. 5","B. 1"],["A. 15","B. 8"],["A. 3","B. 5"],["A. 10","B. 15"]]
# # answer =["B","A","A","A","B"]
# # # Initialize score 
# # score = 0
# # # Loop through each question 
# # for question in range(len(questions)):
# #     print(questions[question])
# #     for option in options[question]:
# #         print(option)
# #     user_answer = input("Please enter the letter of your answer: ").strip().upper()
# #     #Check if the answer is correct
# #     if user_answer == answer[question]:
# #         print("correct")
# #     else:
# #         print("wrong")
# #     if user_answer == answer[question]:
# #         score += 5
# # print(f"\nYour final score is: {score} out of {25}")

# # Write a program that will ask the user to supply 2 digit values and the program will add the values together
# Number1 = [1,2,3,4,5,6,7,8,9,0]
# Number2 = [1,2,3,4,5,6,7,8,9,0]
# for num1 in Number1:
#     print(num1)
# for num2 in Number2:
#         print(num2)
#         User_Instruction1 = input(f"Supply your first number: ")
#         User_Instruction2= input(f"Supply your second number: ")
#         print("The answer is: num1+num2")

# import random
# Number1 = [1,2,3,4,5,6,7,8,9,0]
# Number2 = [1,2,3,4,5,6,7,8,9,0]

# first_Value = random.choice(Number1)
# second_Value = random.choice(Number2)

# sum = first_Value + second_Value

# print(f" First number picked: {first_Value}")
# print(f" Second number picked: {second_Value}")
# print(f" sum of {first_Value} and {second_Value} is: {sum}")

# # import random
# # Number1 = [1,2,3,4,5,6,7,8,9,0]
# # Number2 = [1,2,3,4,5,6,7,8,9,0]
# # for first_number in Number1:
# #     print(first_number)
# # User_Instruction = input(f"Pick your first number: ")
# # for second_number in Number2:
# #     print(second_number)
# # User_Instruction2 = input(f"Pick your Second number: ")
# # Sum_of_Numbers = int(User_Instruction) + int(User_Instruction2)
# # print(Sum_of_Numbers)
# # print(f" sum of {User_Instruction} and {User_Instruction2} is: {Sum_of_Numbers}")
# User_Instruction2 = input(f"Enter your digit number: ")
# if len(User_Instruction2)==2:
#     print(int(User_Instruction2[0]) + int(User_Instruction2[1]))
# # User_Instruction2 = input(f"Enter three digit number: ")
# elif len(User_Instruction2)==3:
#     print(int(User_Instruction2[0]) + int(User_Instruction2[1])+ int(User_Instruction2[2]))
# # User_Instruction2 = input(f"Enter four digit number: ")
# elif len(User_Instruction2)==4:
#     print(int(User_Instruction2[0]) + int(User_Instruction2[1])+ int(User_Instruction2[2])+ int(User_Instruction2[3]))
# else:
#     print("Error")
    
    
    
# # print(int(User_Instruction2[0]) + int(User_Instruction2[1]))

# # User_Instruction3 = input(f"Enter a three digit number: ")
# # print(int(User_Instruction3[0]) + int(User_Instruction3[1])+ int(User_Instruction3[2]))
# # User_Instruction3 = input(f"Enter a four digit number: ")
# # print(int(User_Instruction3[0]) + int(User_Instruction3[1])+ int(User_Instruction3[2])+ int(User_Instruction3[3]))


# for num in range(5,10,2):
#     print(num)

# list(range(5,10,2))

# #                ennumerate
                

# index_count = 0
# for letter in "abcde":
#     print(f"At index {index_count} the letter is {letter}")
#     index_count += 1

# index_count = 0
# word = "abcde"
# for letter in word:
#     print(word[index_count])
#     index_count += 1

# word = "abcde"
# for item in enumerate(word):
#     print(item)


# word = "abcde"
# for index,letter in enumerate(word):
#     print(index)
#     print(letter)
#     print("\n")


#                 Zip Function

# mylist1 = [1,2,3,4]
# mylist2 = ["a","b","c","d"]
# mylist3 = [100,2,2,2]
# for item in zip(mylist1,mylist2,mylist3):
#     print(item)

# mylist1 = [1,2,3,4]
# mylist2 = ["a","b","c","d"]
# mylist3 = [100,2,2,2]
# for a,b,c in zip(mylist1,mylist2,mylist3):
#     print(b)

# list(zip(mylist1,mylist2,mylist3))

# 2 in [1,2,3]

# "x" in ["x","c","a"]

# "Mayowa " in ["Mayowa is a boy"]

# "mykey" in {"mykey":23}

# d = {"mykey":23}
# 23 in d.values()

# My_List = [1,2,3,4,5]
# max(My_List)
# min(My_List)

# max(My_List)

# from random import shuffle

# My_List = [1,2,3,4,5,6,7,8,9,10]

# shuffle(My_List)

# My_List

# from random import randint

# randint(0,100)

# randint(0,100)

# mynum = randint(1,199)

# mynum

# mynum



# input("Enter my number here: ")

# result = input("What is your name?: ")

# result

# result = int(input("Enter my number here: "))

# print(result)

# type(result)

#                         List Comprehension

# mystring = "hellllloo"

# mylist = []
# for letter in mystring:
#     if letter not in mylist:
#         mylist.append(letter)

# print(mylist)

# Name = "Mayowa"

# Mylist = []

# for letter in Name:
#     Mylist.append(letter)

# print(Mylist)

# Name = "Mayowa"

# Mylist = [letter for letter in Name]

# Mylist

# Mylist = [x for x in "Tammy"]

# Mylist

# Mylist = [x for x in range(0,11)]

# Mylist

# Mylist = [num**2 for num in range(0,11)] # Square the list

# Mylist

# Mylist = [x for x in range(0,11) if x%2==0] # Find the even

# Mylist

# Mylist = [x for x in range(0,11) if x%2==1] # Find the odd

# Mylist

# Mylist = [x**2 for x in range(0,11) if x%2==1] # Square and Find the odd

# Mylist

# Celcius = [0,10,20,34.5]

# Fahrenheit = [((9/5)*temp+32) for temp in Celcius] # Convert Celcius into Fahrenheit 

# Fahrenheit

# Days = [40,56,90,120] # Convert Days into Month

# Month = [x/30 for x in Days]

# print(Month)

# Result = [x if x%2==0 else "ODD" for x in range(0,10)]

# print(Result)

# Result = [x if x%2==1 else "Even" for x in range(0,20)]

# print(Result)

# Mylist = []
# for x in [1,2]:
#     for y in [10,20]:
#         Mylist.append(x*y)
      

# Mylist

# # Nested Loop

# Mylist =[]
# for x in [1,2,3,4,5]:
#     for y in [1,100,1000,10000,100000]:
#         Mylist.append(x*y)

# print(Mylist,end = "")

# Mylist = [x*y for x in [2,4,6] for y in [1,10,100]]

# Mylist

# loc = 'Bank'

# if loc == 'Auto Shop':
#     print('Welcome to the Auto Shop!')
# elif loc == 'Bank':
#     print('Welcome to the bank!')
# else:
#     print('Where are you?')

# list1 = [1,2,3,4,5,6,7,8,9]


# list_sum = 0 

# for num in list1:
#     list_sum = list_sum + num

# print(list_sum)

# list_sum = 4

# for num in list1:
#     list_sum = list_sum + num

# print(list_sum)

# x = 0

# while x < 10:
#     print('x is currently: ',x)
#     print(' x is still less than 10, adding 1 to x')
#     x+=1

# x = 5

# while x <= 5:
#     print('x is currently: ',x)
#     print(' x is still less than 10, adding 1 to x')
#     x+=1
    
# else:
#     print('All Done!')

# x = 0

# while x < 10:
#     print('x is currently: ',x)
#     print(' x is still less than 10, adding 1 to x')
#     x+=1
#     if x==3:
#         print('x==3')
#     else:
#         print('continuing...')
#         continue

# x = 0

# while x < 10:
#     print('x is currently: ',x)
#     print(' x is still less than 10, adding 1 to x')
#     x+=1
#     if x==3:
#         print('Breaking because x==3')
#         break
#     else:
#         print('continuing...')
#         continue

# index_count = 0

# for letter in 'abcde':
#     print(f"At index {index_count} the letter is {letter}")
#     index_count += 1

# index_count = 0
# for letter in "abcde":
#     print(f"At index {index_count} the letter is {letter}")
#     index_count += 1

# for i,item in enumerate("abcde"):
#     print(f"At index {i} the letter is {item}")

# for i,letter in enumerate('abcde'):
#     print("At index {} the letter is {}".format(i,letter))

# mylist1 = [1,2,3,4]
# mylist2 = ["a","b","c","d"]

# NewList = list(zip(mylist1,mylist2))

# print(NewList)

# mylist1 = [1,2,3,4]
# mylist2 = ["a","b","c","d"]

# for item1,item2 in NewList:
#     print(f"The index {item1} has alphabet {item2}")

# "x" not in "Ma,yow,ax"

# mylist1 = [1,2,3,4]

# from random import shuffle

# shuffle(mylist1)

# mylist1

# mylist1

# from random import randint
# randint(0,22)

# randint(1,2)

# lst = [x for x in range(11)]

# lst

# lst = [ x**2 for x in [x**2 for x in range(11)]]
# lst

#                                 Test

# st = 'Print only the words that start with s in this sentence'

# for new in st.split():
#     if new[0] =="s":
#         print(new)

# #1 
# for test in st:
#     if test[0] == "s":
#         print(test)
    

# for test in st.split():
#     if test[0] == "s":
#         print(test)


# st = "This is the best meal that I ever tasted in a while"

# for new in st:
#     if new[0] =="s":
#         print(new.split())

# for item in st.split():
#     if item[0]=="T":
#         print(item)

# Use range to print all the even numbers from 0 to 10

# # for even in range(11):
# #     if even %2 ==0:
# #         print(even)
        
        
# even = list(range(11))
# for may in even:
#     if may%2==0:
#         print(may)
        


# list = range(1,50)

# list

# print(list)

# list = [x for x in range(0,11) if x%2==0]


# print(list)



# #**Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.**
# list = [x for x in range(50) if x%3 ==0]
# print(list)

# #**Go through the string below and if the length of a word is even print "even!"**
# st = 'Print every word in this sentence that has an even number of letters'
# for list in st.split():
#     if len(list)%2==0:
#         print(list)
        
    

# # ____
# # #**Write a program that prints the integers from 1 to 100. 
# # But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". 
# # For numbers which are multiples of both three and five print "FizzBuzz".**

# for num in range(1,101):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)

# # # x = range(100)

# # for num in range(1,101):
# #     if num % 3 == 0 and num % 5 == 0:
# #         print("FizzBuzz")
# #     elif num % 3 == 0:
# #         print("Fizz")
# #     elif num % 5 == 0:
# #         print("Buzz")
# #     else:
# #         print(num)
# for x in range(1,101):
#     if x%3 ==0:
#         print("Fizz")
#     elif x%5 ==0:
#         print("Buzz")
#     elif x%3 == 0 and x%5 == 0:
#         print("FizzBuzz")
#     else:
#         print(x)
    
    
# #     print("FizzBuzz")
# # Result = [x if x%2==1 else "Even" for x in range(0,20)]

# lis = [x if x%3 ==1 else "fizz" for x in range(0,100)]

# lis

# st = 'Create a list of the first letters of every word in this string'

# [word[0] for word in st.split()]



# print(st)

# # # #**Write a program that prints the integers from 1 to 100. 
# # # But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". 
# # # For numbers which are multiples of both three and five print "FizzBuzz".**
# # for x in range (0,100):
# #     if x%3==0:
# #         print("Fizz")
# #     if x%5==0:
# #         print("Buzz")
# #     if x%3==0 & x%5==0:
# #         print("FizzBuzz")

# for x in range (1,101):
#     if x%3==0 and x%5==0:
#         print("FizzBuzz")
#     elif x%5 ==0:
#         print("Buzz")
#     elif x%3 ==0:
#         print("Fizz")
#     else:
#         print(x)

# # st = 'Create a list of the first letters of every word in this string'
# [x[0] for x in st.split()]

# The Challenge:

# Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

# 1. If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
# 2. On a player's first turn, if their guess is
#  * within 10 of the number, return "WARM!"
#  * further than 10 away from the number, return "COLD!"
# 3. On all subsequent turns, if a guess is 
#  * closer to the number than the previous guess return "WARMER!"
#  * farther from the number than the previous guess, return "COLDER!"
# 4. When the player's guess equals the number, tell them they've guessed correctly *and* how many guesses it took!

# Mylist =[1,2,3]

# Mylist.insert(0,199)

# Mylist.sort(reverse=True)

# Mylist

# def say_hello():
#     print("Hello")
#     print("How")
#     print("are")
#     print("You")

# say_hello()

# def say_hello(name):
#     print(f"Hello {name}")

# say_hello("Jose")

# def babiala(name):
#     print(f"The name of the boy is {name}")

# babiala("Mayowa")

#  def print_result(a,b):
#         print(a+b)

# def return_result(a,b):
#     return a+b

# result = print_result(2,3)

# result

# return_result(2,4)

# returnn = return_result(2,4)

# returnn

# def return_result(a,b):
#     return a+b

# return_result(2,1)

# def returnn(a,b):
#     return a+b

# returnn (3,1)

# def even_check(number):
#     result =number %2==0
#     return result
   

# even_check(20)

# def check_even_list(num_list):
#     for number in num_list:
#         if number % 2==0:
#             return True
#         else:
#             pass

# check_even_list([1,1,1,123])

# check_even_list([22,1,1,123])

#  check_even_list([22,1,1,12,3])

# # # "Mayowa","Tomiwa","Tayo","Tolani"
# # def check_name_list("Mayowa","Tomiwa","Tayo","Tolani"):
# #     for name in naame:
# #         if name[0]="T":
# #             return True
# #         else:
# #             pass
        

# check_even_list([2,1,2,3,0])

# def check_even_list(num_list):   # I want to know if it's true or false
#     for number in num_list:
#         if number % 2==0:
#             return True
#         else:
#             pass
#     return False # The return is in indentation with the for loop

# check_even_list([3,1,7,9])

# def check_odd_list(numlist):
#     for number in numlist:
#         if number %2==1:
#             return True
#         else:
#             pass
#     return False

# check_odd_list([2,4,6,8])

# def check_even_number(newlist):
# # Checking for even number
#     even_number = []
#     for number in newlist:
#         if number%2==0:
#             even_number.append(number)
#         else:
#             pass
        
#     return even_number
            

# check_even_number([1,11,5,2,4,5])

# def check_odd_number(newlist):
#     odd_number =[]
#     for num in newlist:
#         if num%2==1:
#             odd_number.append(num)
#         else:
#             pass
#     return odd_number

# check_odd_number([1,2,3,45,65,])




# contact = []
# for i in range(10):
#     name = input(f"What is your name {i+1}?: ")
#     phone = input(f"{name} phone number: ")
#     contact.append({"name":name,"phone":phone})

# name = []
# phone = []

# while True:
#     print("1. Display Contact")
#     print("2. Add Contact")
#     print("3. Delete contact")
#     print("4. Search Contact")
#     print("5. Exist")
    
#     choice =input("What is your choice: ")
#     if choice =="1":
#         print("Contact List: ")
#         for i in range(len(name)):
#             print(f"{i+1}. {name[i]}-{phone[i]}")
#         print()  
    
#     elif choice =="2":
#         print("Add Contact: ")
#         add_name = input("What is the name: ")
#         add_phone =input("What is the phone: ")
#         name.append(add_name)
#         phone.append(add_phone)
#         print(f"contact {add_name} added \n")
        
#     elif choice =="3":
#         print("Delete Contact: ")
#         Delete_name = input("what name do you want to delete?: ")
#         if Delete_name in name:
#             index = name.index(Delete_name)
#             name.remove(Delete_name)
#             phone.pop(index)
#             print(f"contact {Delete_name} deleted \n")
#         else:
#             print(f"contact {Delete_name} not found \n")
            
#     elif choice =="4":
#         print("Search Contact")
#         Search_name =input("What contact are you looking for?: ")
#         if Search_name in name:
#             index = name.index(Search_name)
#             print(f"Result: contact {name[index]} and phone number {phone[index]} \n")
#         else:
#             print(f" contact {Search_name} not found!!! /n")
            
#     elif choice =="5":
#         print("Existing........")
#         break
#     else:
#         print("Invalid Choice \n")
            
       






# Tuples Unpacking

# Stock_Prices = [("APPL",200),("gOOG",300),("Mcst",500)]

# Stock_Prices = [("APPL",200),("gOOG",300),("Mcst",500)]
# for key,value in Stock_Prices:
#     print(value) 

# Stock_Prices = [("APPL",200),("gOOG",300),("Mcst",500)]
# for key,value in Stock_Prices:
#     print(value+(0.5*value))

# #write a program that accepts numbers from user in a comma separated format, and prints the highest
# res = []
# user = input("Enter your numbers, just separate with comma : " )
# for a in user.split(","):
#     res.append(a)
# print(res)



# highest = 0
# for i in res:
#     i = int(i)
#     if i>highest:
#         highest = i
# print(highest)

# def sumi(a,b):
#     return a + b

# sumi(2,7)

# Stock_Prices = [("APPL",200),("gOOG",300),("Mcst",500)]
# for key,value in Stock_Prices:
#     print(key) 

# Work_hours = [("Abby",100),("Billy",400),("Castle",800)]

# Work_hours = [("Abby",100),("Billy",400),("Castle",800)]

# def employer_details(Work_hours):
#     Current_Hours = 0
#     Employee_name = ""
    
#     for Name,Hours in Work_hours:
#         if Hours > Current_Hours:
#             Current_Hours = Hours
#             Employee_name = Name
#         else:
#             pass
#     return (Employee_name,Current_Hours)
        


# employer_details(Work_hours)

# Student_Information = [("Mayowa",16),("Bayo",21),("Lateef", 17),("Salam",43)]
# # def Std_info(Student_Information):
# #     Current_Age = 0
# #     Student_Name = " "
    
# #     for Student,Age in Student_Information:
# #         if Age > Current_Age:
# #             Current_Age = Age
# #             Student_Name = Student
# #         else:
# #             pass
        
# #         return (Student_Name,Age)
        

# Std_info(Student_Information)

# Student_Information = [("Mayowa",16),("Bayo",21),("Lateef", 17),("Salam",43)]
# def Std_info(Student_Information):
#     Current_Age = 0
#     Student_Name = " "
    
#     for Student,Age in Student_Information:
#         if Age > Current_Age:
#             Current_Age = Age
#             Student_Name = Student
#         else:
#             pass
        
#     return (Student_Name,Current_Age)

# Std_info(Student_Information)

# Interaction between python function

# example = [1,2,3,4,5,6,7,8]

# from random import shuffle

# shuffle(example)

# list(example)



# example.sort(reverse=True)

# example

# resul = shuffle(example) 

# resul

# def shuffle_list(mylist):
#     shuffle(mylist)
#     return mylist

# result = shuffle_list(example)

# result

#  Age = [20,7,38,90,28,11,90]

# def age_name(mylist):
#     shuffle(mylist)
#     return mylist
    

# result = age_name(Age)

# result

# mylist = ["","O",""]

# shuffle_list(mylist)

# def player_guess():
#     guess = ""
#     while guess not in ["0","1","2"]:
        
#         guess = input("Pick a number: 0,1 or 2")
#     return int(guess)

# player_guess()

# def player_guess():
#     guess = ""
#     while guess not in ["0","1","2"]:
        
#         guess = input("Pick a number 0,1 or 2: ")
#     return int(guess)
    

# player_guess()

# myindex = player_guess()

# myindex

# def check_guess(mylist,guess):
#     if mylist[guess] == "O":
#         print("Correct")
#     else:
#         print("Wrong Guess")
#         print(mylist)

# # Initial list
# mylist = ["","O",""]
# # Shuffle List
# Mixedup_List = shuffle_list(mylist)
# # User Guess
# guess = player_guess()
# # Check Guess
# check_guess(Mixedup_List,guess)


# # First_Values = {}
# # Second_Values = {}
# First_Value = input("Provide 51 values: ")
# # Second_Value = input("Provide 5 values: ")
# while True:
#     print("1. Intersection")
#     print("2. Union")
#     print("3. Difference")
    
#     choice = input("What is your choice?: ")
#     if choice == 1:
#         print(set(First_Value))
# #     elif choice ==2:
# #         print(set(Second_Value))
        
    

    


# First_Value = input("Provide 51 values: ")
# Second_Value = input("Provide 5 values: ")
# while True:
#     print("1. Intersection")
#     print("2. Union")
#     print("3. Difference")
    
#     choice = input("What is your choice?: ")
#     if choice == 1:
#         num = set(First_Value)
#         print(num)


# First_Value =[]
# Second_Value = []

# while True:
#     print("1. Intersection")
#     print("2. Union")
#     print("3. Difference")
#     choice = input("Pick a number: ")
#     if choice=="1":
#         First_Value = input("Provide 5 values: ")
#         Second_Value = input("Provide 5 values: ")
#         FV = set(First_Value)
#         print(FV)
#         SV = set(Second_Value)
#         print(SV)
#         Intersection = FV & SV
#         print(sorted(Intersection))
#     elif choice=="2":
#         First_Value = input("Provide 5 values: ")
#         Second_Value = input("Provide 5 values: ")
#         FV = set(First_Value)
#         print(FV)
#         SV = set(Second_Value)
#         print(SV)
#         Union = FV.union(SV)
#         print(sorted(Union))
#     elif choice=="3":
#         First_Value = input("Provide 5 values: ")
#         Second_Value = input("Provide 5 values: ")
#         FV = set(First_Value)
#         print(FV)
#         SV = set(Second_Value)
#         print(SV)
#         Difference = FV-SV
#         print(Difference)
    
        
    



# def myfunc(a,b):
#     # return 5% of the sum of a and b
#     return sum((a,b))*0.05



# def myfunc(a,b):
#     # return 5% of the sum of a and b
#     return sum((a,b))*0.05
# print(myfunc(40,60))

# def myfunc(a,b):
#     # return 5% of the sum of a and b
#     return sum((a,b))*0.05

# myfunc(10,20)

# def newtrick(y,z):
#     return sum((y,z))*0.05

# newtrick(2,3)

# def myfunc(a,b,c=0):
#     return sum((a,b,c))*0.05

# myfunc(1,2,)

# def myfunc(*args):
#     return sum(args)*0.05

# myfunc(1,2,3,4,5)

# def myfunc(*args):
#     return sum(args)

# myfunc(1,2,233,3)

# def myfunc(*args):
#     for item in args:
#         print(item)

# myfunc(7,2,3,4,45)

# def myfunc(**Kwargs):
#     print(Kwargs)
#     if 'fruit' in Kwargs:
#         print('My first of choice is {}'.format(Kwargs['fruit']))
#     else:
#         print("I did not find any fruit here")

# myfunc(fruit='apple',Veggie='Lettuce')

# def myfunc(*args,**kwargs):
#     print(args)
#     print(kwargs)
#     print("I would like {} bags of {}".format(args[0],kwargs['food']))

# myfunc(10,20,30,fruit ='banana',food = 'Rice')%

# Questions

# #Q1 Write a function that returns the lesser of two given numbers if
# #both numbers are even, but returns the greater if one or both numbers are odd
# #    lesser_of_two_evens(2,4) --> 2
# #    lesser_of_two_evens(2,5) --> 5

# def lesser_of_two_evens(a,b):
#     if a%2==0 and b%2==0:
#         # Both Numbers are even
#         if a<b:
#             result = a
#         else:
#             result = b
#     else:
#         # One or both are odd
#         if a>b:
#             result = a
#         else:
#             result = b
#     return result

#  lesser_of_two_evens(4,2)

#    lesser_of_two_evens(2,5)

#    lesser_of_two_evens(7,5)

# or 

# # def lesser_of_two_evens(a,b):
# #     if a%2 ==0 and b%2==0:
# #         if a<b:
# #             return min(a,b)
# #     else:
# #         return max(a,b)

# def lesser_of_two_evens(a,b):
#     if a%2==0 and b%2==0:
#         return min(a,b)
#     else:
#         return max(a,b)

#  lesser_of_two_evens(4,2)

#    lesser_of_two_evens(7,5)

# #  Q2 Write a function takes a two-word string and returns True if both words begin with same letter
# #     animal_crackers('Levelheaded Llama') --> True
# #     animal_crackers('Crazy Kangaroo') --> False

# def animal_crackers(text):
#     wordlist = text.split()
#     print(wordlist)
    
#     firstword = wordlist[0]
#     secondword = wordlist[1]
    
#     return firstword[0]==secondword[0]


# animal_crackers('Levelheaded Llama')


# animal_crackers('Crazy Kangaroo')

# #  Given two integers, return True if the sum of the integers is 20 *or* if one of the integers is 20. If not, return False

# def makes_twenty(n1,n2):
#     if n1+n2 ==20:
#         return True
#     elif n1 == 20:
#         return True
#     elif n2 == 20:
#         return True
#     else:
#         return False
    

# makes_twenty(20,10) 
  

# makes_twenty(12,8) 


# makes_twenty(2,3)

# # Write a function that capitalizes the first and fourth letters of a name
# #    old_macdonald('macdonald') --> MacDonald
# # Note: `'macdonald'.capitalize()` returns `'Macdonald'`

# def old_macdonald(name):
#     First_Letter = name[0]
#     InBetweeen = name[1:3]
#     FourthLetter = name[3]
#     Rest = name[4:]
    
#     return First_Letter.upper()+InBetweeen+FourthLetter.upper()+Rest



# old_macdonald("macdonald")

# def old_letter(name):
#     firstpart = name[:3]
# #     return firstpart.capitalize()
#     secondpart = name[3:]
# #     return ()
#     return firstpart.capitalize()+secondpart.capitalize()

# old_letter("mayowa")

# #  Given a sentence, return a sentence with the words reversed
# # master_yoda('I am home') --> 'home am I'
# #     master_yoda('We are ready') --> 'ready are We'

# # def master_yoda(text):
# #     wordlist = text.split()
# # #     reverse_wordlist = text[::-1]
# # #     return reverse_wordlist
# #     return wordliist

# def master_yoda(text):
#     wordlist = text.split()
#     reverse_wordlist = wordlist[::-1]
#     return " ".join(reverse_wordlist)

# master_yoda('I am home')

# master_yoda('We are ready')

# mylist = ["a","b","c","d"]

# "".join(mylist)

# # Given an integer n, return True if n is within 10 of either 100 or 200

# def almost_there(n):
#     return (abs(100-n)<=10) or (abs(200-n)<=10)


# almost_there(104)

# almost_there(150)

# almost_there(209)

# # Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# #     has_33([1, 3, 3]) → True
# #     has_33([1, 3, 1, 3]) → False
# #     has_33([3, 1, 3]) → False

# def has_33(nums):
#     for i in range(0,len(nums)-1):
#         if nums[i]==3 and nums[i+1]==3:
#             return True
#     else:
#         return False

#  has_33([1, 3, 3])

# has_33([1, 3, 1, 3])

# has_33([3, 1, 3])

# def has_33(nums):
#     for i in range (0,len(nums)-1):
#         if nums[i:i+2] == [4,4]:
#             return True
#     else:
#         return False
        

# has_33([3, 1, 3])

# has_33([3, 4, 4])

# # Given a string, return a string where for every character in the original there are three characters

# #     paper_doll('Hello') --> 'HHHeeellllllooo'
# #     paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

# def paper_doll(text):
#     result = ""
#     for char in text:
#         result += char+char+char
#         return result
    

# paper_doll('Hello')

# # import random

# # def generate_account_number():
# #     return random.randint(1000000000,999999999)
# # def setup_account():
# #     name = input("Enter your account name: ")
# #     pin = "0000"
    
# #     account_number = generate_account_number()
# #     print(f"\n Account created successfully! \n Account Name: {name} \n Account Mumber: {account_number} \n PIN: {pin}")
# #     return name, account_number, pin
    
# # # Initialize the user balance
# # balance = 0.0 

# # def check_balance():
# #     print(f"Your current balance is:${balance:.2f}")

# # def deposit(amount):
# #     global balance
# #     balance = balance + amount
# #     print(f"${amount:.2f} has been deposited. New balance: ${balance:.2f}")
# # def withdraw(amount):
# #     global balance
# #     if amount>balance:
# #         print("Insufficient funds.")
# #     elif amount >0:
# #         balance = balance-amount
# #         print(f"${amount:.2f} has been withdrawn. New Balance: ${balance:.2f}")
# #     else:
# #         print("You can only withdraw a positive amount.")
# # def bank_app():
# #     while True:
# #         entered_pin = input("Enter your PIN to access your account: ")
# #         if entered_pin != pin:
# #             print("Incorrect PIN. Please try again.")
# #             continue
# #         print(f"\nWelcome, {name} (Account Number: {account_number})!")
# #         print("1. Check Balance")
# #         print("2. Deposit Money")
# #         print("3. Withdraw Money")
# #         print("4. Exit")
        
# #         choice = input("Choose an option (1-4): ")

# #         if choice == "1":
# #             check_balance()
# #         elif choice == "2":
# #             amount = float(input("Enter amount to deposit: $"))
# #             deposit(amount)
# #         elif choice == "3":
# #             amount = float(input("Enter amount to withdraw: $"))
# #             withdraw(amount)
# #         elif choice == "4":
# #             print("Thank you for using the bank app. Goodbye!")
# #             break
# #         else:
# #             print("Invalid choice. Please try again.")

# # # Run the bank app
# # bank_app()
        
        
    
            

# # def bank_app():
# #     while True:
# #         entered_pin = input("Enter your PIN to access your account: ")
# #         if entered_pin != pin:
# #             print("Incorrect PIN. Please try again.")
        
        
# #         print(f"\nWelcome, {name} (Account Number: {account_number})!")
# #         print("\n Welcome to the bank app!")
# #         print("1. Check Balance")
# #         print("2. Deposit Money")
# #         print("3. Withdraw Money")
# #         print("4. Exit")
        
# #         choice = input("Choose an option (1,4): ")
        
# #         if choice == "1":
# #             check_balance()
# #         elif choice =="2":
# #             amount = float(input("Enter amount to deposit: $"))
# #             deposit(amount)
# #         elif choice =="3":
# #             amount = float(input("Enter amount to withdraw: $"))
# #             withdraw(amount)
# #         elif choice =="4":
# #             print("Thank you for using the bank app. Goodbye!")
# #             break
# #         else:
# #             print("Invalid choice. Please try again.")
            




# import random

# # Function to generate a random account number
# def generate_account_number():
#     return random.randint(1000000000, 9999999999)  # 10-digit account number

# # Function to set up a new account
# def setup_account():
#     name = input("Enter your account name: ")
#     pin = "0000"  # Default PIN

#     account_number = generate_account_number()
#     print(f"\nAccount created successfully!\nAccount Name: {name}\nAccount Number: {account_number}\nDefault PIN: {pin}\n")
#     return name, account_number, pin

# # Initialize the user's balance
# balance = 0.0  # starting balance

# def check_balance():
#     print(f"Your current balance is: ${balance:.2f}")

# def deposit(amount):
#     global balance
#     if amount > 0:
#         balance += amount
#         print(f"${amount:.2f} has been deposited. New balance: ${balance:.2f}")
#     else:
#         print("You can only deposit a positive amount.")

# def withdraw(amount):
#     global balance
#     if amount > balance:
#         print("Insufficient funds.")
#     elif amount > 0:
#         balance -= amount
#         print(f"${amount:.2f} has been withdrawn. New balance: ${balance:.2f}")
#     else:
#         print("You can only withdraw a positive amount.")

# def bank_app():
#     name, account_number, pin = setup_account()
    
#     while True:
#         entered_pin = input("Enter your PIN to access your account: ")
#         if entered_pin != pin:
#             print("Incorrect PIN. Please try again.")
#             continue
        
#         print(f"\nWelcome, {name} (Account Number: {account_number})!")
#         print("1. Check Balance")
#         print("2. Deposit Money")
#         print("3. Withdraw Money")
#         print("4. Exit")
        
#         choice = input("Choose an option (1-4): ")

#         if choice == "1":
#             check_balance()
#         elif choice == "2":
#             amount = float(input("Enter amount to deposit: $"))
#             deposit(amount)
#         elif choice == "3":
#             amount = float(input("Enter amount to withdraw: $"))
#             withdraw(amount)
#         elif choice == "4":
#             print("Thank you for using the bank app. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# # Run the bank app
# bank_app()


# # import random

# # def generate_account_number():
# #     return random.randint(1000000000,999999999)
# # def setup_account():
# #     name = input("Enter your account name: ")
# #     pin = "0000"
    
# #     account_number = generate_account_number()
# #     print(f"\n Account created successfully! \n Account Name: {name} \n Account Mumber: {account_number} \n PIN: {pin}")
# #     return name, account_number, pin
    
# # # Initialize the user balance
# # balance = 0.0 

# # def check_balance():
# #     print(f"Your current balance is:${balance:.2f}")

# # def deposit(amount):
# #     global balance
# #     balance = balance + amount
# #     print(f"${amount:.2f} has been deposited. New balance: ${balance:.2f}")
# # def withdraw(amount):
# #     global balance
# #     if amount>balance:
# #         print("Insufficient funds.")
# #     elif amount >0:
# #         balance = balance-amount
# #         print(f"${amount:.2f} has been withdrawn. New Balance: ${balance:.2f}")
# #     else:
# #         print("You can only withdraw a positive amount.")
# # def bank_app():
# #     name, account_number, pin = setup_account()
# #     while True:
# #         entered_pin = input("Enter your PIN to access your account: ")
# #         print(f"\nWelcome, {name} (Account Number: {account_number})!")
# #         print("1. Check Balance")
# #         print("2. Deposit Money")
# #         print("3. Withdraw Money")
# #         print("4. Exit")
        
# #         choice = input("Choose an option (1-4): ")

# #         if choice == "1":
# #             check_balance()
# #         elif choice == "2":
# #             amount = float(input("Enter amount to deposit: $"))
# #             deposit(amount)
# #         elif choice == "3":
# #             amount = float(input("Enter amount to withdraw: $"))
# #             withdraw(amount)
# #         elif choice == "4":
# #             print("Thank you for using the bank app. Goodbye!")
# #             break
# #         else:
# #             print("Invalid choice. Please try again.")
# # bank_app()

# # def bank_app():
# #     while True:
# #         print(f"\nWelcome, {name} (Account Number: {account_number})!")
# #         print("1. Check Balance")
# #         print("2. Deposit Money")
# #         print("3. Withdraw Money")
# #         print("4. Exit")
        
# #         choice = input("Choose an option (1-4): ")

# #         if choice == "1":
# #             check_balance()
# #         elif choice == "2":
# #             amount = float(input("Enter amount to deposit: $"))
# #             deposit(amount)
# #         elif choice == "3":
# #             amount = float(input("Enter amount to withdraw: $"))
# #             withdraw(amount)
# #         elif choice == "4":
# #             print("Thank you for using the bank app. Goodbye!")
# #             break
# #         else:
# #             print("Invalid choice. Please try again.")
        

# # bank_app()

# import random
# # Generate a random account number
# def generate_random_account_number():
#     return random.randint(10000000000,99999999999)
# #function to setup a new account
# # def set_up_account():
    
# #     print(f"\nAccount Created Successfully\nAccount Name: {name}\nAccount Number: {account_number}")
# #     return name, account_number,pin

# # Initialize balance 
# balance = 0.00
# def check_balance():
#     print(f"Your Account Balance is: ${balance:.2f}")
# def deposit(Amount):
#     global balance
#     if Amount < 0:
#         print(f"Error!! You cannot deposit a negetive amount")
#     elif Amount > 0:
#         balance = balance + Amount
#         print(f"${Amount:.2f} has been deposited to your account. New Balance: ${balance:.2f}")
# def withdraw(Amount):
#     global balance
#     if Amount > balance:
#         print(f"Insufficiend Funds")
#     elif Amount < balance:
#         balance = balance-Amount
#         print(f"${Amount:.2f} has been withdrawn from your account. New Balance: ${balance:.2f}")
# def bank_app():
#     name = input("Enter your account name: ")
#     pin = "0000"
#     account_number = generate_random_account_number()
    
#     entered_pin = input("Enter your PIN to access your account: ")
#     if entered_pin != pin:
#         print(f"Wrong Password: Input the right Password")
#     else:
#         continue
#         while True:
#             print(f"\n Welcome , {name} \nAccount Number: {account_number}")
#             print("1. Check Balance")
#             print("2. Deposit")
#             print("3. Withdraw")
#             print("4. Exist")

#             choice = input("Please enter your preferred number")
#             if choice == "1":
#                 check_balance()
#             elif choice == "2":
#                 Amount = float(input("How much do you want to deposit?: $"))
#                 deposit(Amount)
#             elif choice == "3":
#                 Amount = float(input("How much do you want to Withdraw?: $"))
#                 withdraw(Amount)
#             elif choice == "4":
#                 print("Thank you for using the bank app. Goodbye!")
#                 break
#             else: 
#                 print("Invalid Choice. Input a correct number")
            
# # set_up_account()
# bank_app()

# def bank_app():
#     name, account_number, pin
#     while True:
#         entered_pin = input("Enter your PIN to access your account: ")
#         if entered_pin != pin:
#             print(f"Wrong Password: Input the right Password")
#         else:
#             continue
#         print(f"\n Welcome , {name} \nAccount Number: {account_number}")
#         print("1. Check Balance")
#         print("2. Deposit")
#         print("3. Withdraw")
#         print("4. Exist")
        
#         choice = input("Please enter your preferred number")
#         if choice == "1":
#             check_balance()
#         elif choice == "2":
#             Amount = float(input("How much do you want to deposit?: $"))
#             deposit(Amount)
#         elif choice == "3":
#             Amount = float(input("How much do you want to Withdraw?: $"))
#             withdraw(Amount)
#         elif choice == "4":
#             print("Thank you for using the bank app. Goodbye!")
#             break
#         else: 
#             print("Invalid Choice. Input a correct number")
            
    

# bank_app()

# # user_input = input("""Please enter what you want to do today:
# # 1. Check balance
# # 2. Deposit
# # 3. Withdraw
# #               """)
# # if user_input == "1":
# #     check_balance()
# # elif user_input == "2":
# #     amount=float(input("How much do you want to deposit"))
# #     deposit(amount)
# # elif user_input == "3":
# #     amount=float(input("How much do you want to deposit"))
# #     withdraw(amount)
# # else:
# #     print("Please input a valid number")

# Name =["Ayomide","Adeola","Abdullahi","Shola","Mayowa","Timi"]
# def Register_User(name, Name):
#     print(f"Account Name: {name}")
#     if name in Name:
#         print("Continue your Transaction")
#     else: 
#         print("Name not registered")
    
# import random
# # Generate a random account number
# def generate_random_account_number():
#     return random.randint(10000000000,99999999999)

# # Initialize balance 
# balance = 0.00
# def check_balance():
#     print(f"Your Account Balance is: ${balance:.2f}")
# # Deposit
# def deposit(Amount):
#     global balance
#     if Amount < 0:
#         print(f"Error!! You cannot deposit a negetive amount")
#     elif Amount > 0:
#         balance = balance + Amount
#         print(f"${Amount:.2f} has been deposited to your account. New Balance: ${balance:.2f}")
# # Withdrawal
# def withdraw(Amount):
#     global balance
#     if Amount > balance:
#         print(f"Insufficiend Funds")
#     elif Amount <= balance:
#         balance = balance-Amount
#         print(f"${Amount:.2f} has been withdrawn from your account. New Balance: ${balance:.2f}")
# def bank_app():
#     name = input("Enter your account name: ")
#     pin = "0000"
#     account_number = generate_random_account_number()
    
#     entered_pin = input("Enter your PIN to access your account: ")
#     if entered_pin != pin:
#         print(f"Wrong Password: Input the right Password")
        
       
        
#     else:
#         while True:
#             print(f"\n Welcome , {name} \nAccount Number: {account_number}")
#             print("1. Check Balance")
#             print("2. Deposit")
#             print("3. Withdraw")
#             print("4. Exist")

#             choice = input("Please enter your preferred number: ")
#             if choice == "1":
#                 check_balance()
#             elif choice == "2":
#                 Amount = float(input("How much do you want to deposit?: $"))
#                 deposit(Amount)
#             elif choice == "3":
#                 Amount = float(input("How much do you want to Withdraw?: $"))
#                 withdraw(Amount)
#             elif choice == "4":
#                 print("Thank you for using the bank app. Goodbye!")
#                 break
#             else: 
#                 print("Invalid Choice. Input a correct number")
            
# # set_up_account()
# bank_app()


# def paper_doll(text):
#     result = ""
#     for char in text:
#         result = result + char*3
#     return result


# paper_doll('Hello')


# paper_doll("mayowa")

# Lambda expressions map & Filter



# def square(num):
#     return num**2


# mylist = [2,4,5,6,7]
# for item in map(square,mylist):
#     print(item)

# list(map(square,mylist))

# without using map

# def cube(num):
#     return num**3
# mylist = [2,4,6,8,9]
# for item in mylist:
#     print(cube(i tem))

# def slicer(mystring):
#     if len(mystring)%2==0:
#         return "Even"
#     else: 
#         return mystring[0]
# names = ["Andy","Mayowa","Timi","Yosola","Tim"]
# # for item in names:
# #     Mayowa =list((slicer(item)))
# #     print(Mayowa)
# list(map(slicer,names))

# def check_even(num):
#     if num%2==0:
#         return num
#     else:
#         return "odd"
# num = [1,2,3,4,5,6,75,34]
# for i in num:
#     print(check_even(i))

# def pick_even(num):
#     return num%2==0
# mylist = [1,2,3,4,5,6,7,8,9]
# list(filter(pick_even,mylist))

# for i in filter(pick_even,mylist):
#     print(i)

# def square(num):
#     return num**2
# print(square(2))

# square = lambda num: num**2

# square(2)

# mylist=[1,2,3,4,5,6,9]
# list(map(lambda num: num**2,mylist))

# mylist = [1,2,289,90,28,29]
# list(filter(lambda num: num%2==0,mylist))

# names = ["Andy","Eve","Sandy"]
# list(map(lambda firstL:firstL[0],names))

# names = ["Andy","Eve","Sandy"]
# list(map(lambda firstL:firstL[::-1],names))

# Nested statement and Scope

# x=26
# def printer():
#         x=3
#         return x
# # print(x)


# print(printer())

# LEGB Rule

# # Local
# lambda num:num**2

# # local
# name = "This is a Global String"
# def greet():
   
#     name = "Sammy"
    
#     def hello():
#         print("Hello " + name)
#     hello()
# greet()

# # Global
# name = "This is a Global String"
# def greet():
#    #Local
# #     name = "Sammy"
    
#     def hello():
#         print("Hello " + name)
#     hello()
# greet()

# # Global
# name = "This is a Global String"
# def greet():
#    #Enclosing
#     name = "Sammy"
    
#     def hello():
#         # Local
#         name = "Mayowa"
#         print("Hello " + name)
#     hello()
# greet()

# x = 50
# def func(x):
#     print(f"X is {x}")
# # Local Reassignment
#     x = 200
#     print(f"I just locally changed x to {x}")

# func(x)

# print(x)
# # Because the reassignment happened in the local scope

# x = 50
# def func():
#     global x
#     print(f"X is {x}")
# # Local Reassignment on a global variable
#     x = "new value"
#     print(f"I just locally changed global x to {x}")

# print(x)

# func()

#  print(x)

# x = 50
# def func():
#     global x
#     print(f"X is {x}")
# # Local Reassignment on a global variable
#     x = "new value"
#     print(f"I just locally changed global x to {x}")

# print(x)

# func()

# print(x)

# x = 50
# def func(x):
#     print(f"X is {x}")
# # Local Reassignment on a global variable
#     x = "new value"
#     print(f"I just locally changed global x to {x}")
#     return x


# x = func(x)

# print(x)

# print(x)

# Method and Function HomeWork Overview

# # Write a function that computes the volume of a sphere given its radius.
# # <p>The volume of a sphere is given as $$\frac{4}{3} πr^3$$</p>

# def vol(rad):
#      return (4/3)*(3.14)*(rad**3)
    

# vol(2)

# def vol(rad):
#     return (4/3)*(3.14)*(rad**3)

# vol(2)

# print("Hello")

# # Write a function that checks whether a number is in a given range (inclusive of high and low)

# def ran_check(num,low,high):
#     if num in range(low,high+1):
#         print(f"{num} is in range {low} and {high}")
#     else: print(f"{num} is not in range {low} and {high}")

# # Check
# ran_check(5,2,7)

# ran_check(29,0,12)

# # for item in range(0,4+1):
# #     print(item)

# # 10 in range(0,4)

# # If you want to return a boolean
# def ran_check(num,low,high):
#     return num in range(low,high+1)

# ran_check(5,2,7)

# ran_check(52,2,7)

# # ____
# # **Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.**

# #     Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# #     Expected Output : 
# #     No. of Upper case characters : 4
# #     No. of Lower case Characters : 33

# # HINT: Two string methods that might prove useful: **.isupper()** and **.islower()**

# # If you feel ambitious, explore the Collections module to solve this problem!

# def up_low(s):
#     Uppercase = 0
#     Lowercase = 0
#     for char in s:
#         if char.isupper():
#             Uppercase += 1
#         elif char.islower():
#             Lowercase +=1
#         else: 
#             pass
#     print(f"Sample String: {s}")
#     print(f"Lowercase Count: {Lowercase}")
#     print(f"Uppercase Count: {Uppercase}")

# s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
# up_low(s)

# # ____
# # **Write a Python function that takes a list and returns a new list with unique elements of the first list.**

# #     Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# #     Unique List : [1, 2, 3, 4, 5]

# def sample_list(s):
#     s = [1,1,1,1,2,2,3,3,3,3,4,5]
#     return list(set(s))

# sample_list(s)

# # ____
# # **Write a Python function to multiply all the numbers in a list.**

# #     Sample List : [1, 2, 3, -4]
# #     Expected Output : -24

# def multiply(numbers): 
#     total = 1
#     for num in numbers:
#         total = total * num
#     return total

# multiply([1,2,3,-4])

# # # ____
# # # **Write a Python function that checks whether a word or phrase is palindrome or not.**

# # # Note: A palindrome is word, phrase, or sequence that reads the same backward as forward,
# # e.g., madam,kayak,racecar, or a phrase "nurses run". 
# # Hint: You may want to check out the .replace() method in a string to help out with dealing with spaces.
# #     Also google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.

# def palindrome(s):
#     s=s.replace(" ","")
#     if s == s[::-1]:
#         return s == s[::-1]
# #         print(s)
    


# palindrome('helll leh')

# palindrome('helleh')

# # Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)**

# #     Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# #     For example : "The quick brown fox jumps over the lazy dog"

# Display Information

# def display_information(row1,row2,row3):
#     print(row1)
#     print(row2)
#     print(row3)

# example_row = [1,2,3,4]
# example_row2 = [3,4,1,42]




# display_information(example_row,example_row2,example_row)

# def display_information(row1,row2,row3):
#     print(row1)
#     print(row2)
#     print(row3)

# row1 = [" "," "," "]
# row2 = [" "," "," "]
# row3 = [" "," "," "]
# row2[1]='x'
# row1[0]='x'
# row3[2]='x'

# display_information(row1,row2,row3)

# Accepting User Input 

# user_age = int(input(f"How old are you?: "))

# print (user_age)

# type(user_age)

# user_age = input(f"How old are you?: ")

# type(user_age)

# user_agge = int(user_age)

# type(user_agge)

# def user_input():
#     choice = input(f"Chose a number from 0-10: ")

# user_input()

# choice = "190"

# chosen = choice.isdigit()

# print(chosen)

# def user_choice():
#     # if the choice from the user is text 
#     choice = "Wrong"
#     acceptance_range = range(0,10)
#     within_range = False
#     # Bringing a while loop to check if the user input is a digit
#     while choice.isdigit() == False or within_range==False:
# #         while choice.isdigit()==False or while
#         # User input
#         choice = input(f"Enter a number from (0-10): ")
#         # Digit Check
#         if choice.isdigit()==False:
#             print(f"Sorry that is not a digit")
#         if choice.isdigit()==True:
#             if int(choice) in acceptance_range:
#                 within_range = True
#             else:
#                 print("Sorry you are not in the range")
#                 within_range = False
#     return int(choice)

# user_choice()

# def user_choice():
#     # if the choice from the user is text 
#     choice = "Wrong"
#     acceptance_range = range(0,10)
#     within_range = False
#     # Bringing a while loop to check if the user input is a digit
#     while choice.isdigit() == False or within_range==False:
# #         while choice.isdigit()==False or while
#         # User input
#         choice = input(f"Enter a number from (0-10): ")
#         # Digit Check
#         if choice.isdigit()==False:
#             print(f"Sorry that is not a digit")
#         if choice.isdigit()==True:
#             if int(choice) in acceptance_range:
#                 within_range = True
#             else:
#                 print("Sorry you are not in the range")
#                 within_range = False
#     return int(choice)
# user_choice()

# Simple User Interaction

# game_list = [1,2,3]


# def display_game(game_list):
#     print(f"Here is the current list")
#     print(game_list)

# display_game(game_list)

# registered_user = {"Muis":{"Account_number":"95995959494","PIN":"9393"}}

# registered_user

# registered_user['Muis']

# registered_user['Muis']['Account_number']

# print(registered_user["Muis"]["PIN"])
# registered_user['Muis']['PIN']="1234"
# print(registered_user["Muis"]["PIN"])

# Name =["Ayomide","Adeola","Abdullahi","Shola","Mayowa","Timi"]
# def Register_User(name, Name):
#     print(f"Account Name: {name}")
#     if name in Name:
#         print("Continue your Transaction")
#     else: 
#         print("Name not registered")
    
# import random
# # Generate a random account number
# def generate_random_account_number():
#     return random.randint(10000000000,99999999999)

# # Initialize balance 
# balance = 0.00
# def check_balance():
#     print(f"Your Account Balance is: ${balance:.2f}")
# # Deposit
# def deposit(Amount):
#     global balance
#     if Amount < 0:
#         print(f"Error!! You cannot deposit a negetive amount")
#     elif Amount > 0:
#         balance = balance + Amount
#         print(f"${Amount:.2f} has been deposited to your account. New Balance: ${balance:.2f}")
# # Withdrawal
# def withdraw(Amount):
#     global balance
#     if Amount > balance:
#         print(f"Insufficiend Funds")
#     elif Amount <= balance:
#         balance = balance-Amount
#         print(f"${Amount:.2f} has been withdrawn from your account. New Balance: ${balance:.2f}")
# def bank_app():
#     name = input("Enter your account name: ")
#     pin = "0000"
#     account_number = generate_random_account_number()
    
#     entered_pin = input("Enter your PIN to access your account: ")
#     if entered_pin != pin:
#         print(f"Wrong Password: Input the right Password")
        
       
        
#     else:
#         while True:
#             print(f"\n Welcome , {name} \nAccount Number: {account_number}")
#             print("1. Check Balance")
#             print("2. Deposit")
#             print("3. Withdraw")
#             print("4. Exist")

#             choice = input("Please enter your preferred number: ")
#             if choice == "1":
#                 check_balance()
#             elif choice == "2":
#                 Amount = float(input("How much do you want to deposit?: $"))
#                 deposit(Amount)
#             elif choice == "3":
#                 Amount = float(input("How much do you want to Withdraw?: $"))
#                 withdraw(Amount)
#             elif choice == "4":
#                 print("Thank you for using the bank app. Goodbye!")
#                 break
#             else: 
#                 print("Invalid Choice. Input a correct number")
            
# # set_up_account()
# bank_app()



# import random

# # List of registered names
# names = ["Ayomide", "Adeola", "Abdullahi", "Shola", "Mayowa", "Timi"]

# # Initialize a dictionary to store user data
# users = {}

# # Function to generate a random account number
# def generate_random_account_number():
#     return random.randint(10000000000, 99999999999)

# # Register users with random account numbers, default PINs, and initial balances
# def register_users():
#     for name in names:
#         account_number = generate_random_account_number()
#         pin = "0000"  # Default PIN for all users
#         balance = 0.00
#         users[name] = {
#             "account_number": account_number,
#             "pin": pin,
#             "balance": balance
#         }

# # Function to check balance of the current user
# def check_balance(user):
#     print(f"Your Account Balance is: ${users[user]['balance']:.2f}")

# # Function to deposit money into the current user's account
# def deposit(user, amount):
#     if amount < 0:
#         print("Error!! You cannot deposit a negative amount")
#     else:
#         users[user]["balance"] += amount
#         print(f"${amount:.2f} has been deposited to your account. New Balance: ${users[user]['balance']:.2f}")

# # Function to withdraw money from the current user's account
# def withdraw(user, amount):
#     if amount > users[user]["balance"]:
#         print("Insufficient Funds")
#     else:
#         users[user]["balance"] -= amount
#         print(f"${amount:.2f} has been withdrawn from your account. New Balance: ${users[user]['balance']:.2f}")

# # Bank app function to interact with a specific user
# def bank_app():
#     # Register users at the start of the app
#     register_users()

#     name = input("Enter your account name: ")

#     # Check if the name is registered
#     if name not in users:
#         print("Name not registered")
#         return

#     # Retrieve user data
#     user_data = users[name]
#     account_number = user_data["account_number"]
#     pin = user_data["pin"]

#     entered_pin = input(f"Enter your PIN to access your account (Account Number: {account_number}): ")

#     if entered_pin != pin:
#         print("Wrong Password: Input the right Password")
#     else:
#         while True:
#             print(f"\nWelcome, {name} \nAccount Number: {account_number}")
#             print("1. Check Balance")
#             print("2. Deposit")
#             print("3. Withdraw")
#             print("4. Exit")

#             choice = input("Please enter your preferred number: ")

#             if choice == "1":
#                 check_balance(name)
#             elif choice == "2":
#                 amount = float(input("How much do you want to deposit?: $"))
#                 deposit(name, amount)
#             elif choice == "3":
#                 amount = float(input("How much do you want to withdraw?: $"))
#                 withdraw(name, amount)
#             elif choice == "4":
#                 print("Thank you for using the bank app. Goodbye!")
#                 break
#             else:
#                 print("Invalid Choice. Input a correct number")

# # Start the banking app
# bank_app()

# bank_app()


# import random

# # Registered users and their data
# users = {
#     "Ayomide": {"pin": "0000", "account_number": None, "balance": 0.00},
#     "Adeola": {"pin": "0000", "account_number": None, "balance": 0.00},
#     "Abdullahi": {"pin": "0000", "account_number": None, "balance": 0.00},
#     "Shola": {"pin": "0000", "account_number": None, "balance": 0.00},
#     "Mayowa": {"pin": "0000", "account_number": None, "balance": 0.00},
#     "Timi": {"pin": "0000", "account_number": None, "balance": 0.00}
# }

# # Generate a random account number
# def generate_random_account_number():
#     return random.randint(10000000000,99999999999)

# # Check balance
# def check_balance(user):
#     print(f"Your Account Balance is: ${users[user]['balance']:.2f}")

# # Depositk
# def deposit(user, Amount):
#     if Amount < 0:
#         print("Error!! You cannot deposit a negative amount")
#     else:
#         users[user]['balance'] += Amount
#         print(f"${Amount:.2f} has been deposited. New Balance: ${users[user]['balance']:.2f}")

# # Withdraw
# def withdraw(user, Amount):
#     if Amount > users[user]['balance']:
#         print("Insufficient Funds")
#     else:
#         users[user]['balance'] -= Amount
#         print(f"${Amount:.2f} has been withdrawn. New Balance: ${users[user]['balance']:.2f}")

# # Bank application
# def bank_app():
#     name = input("Enter your account name: ")
    
#     if name in users:
#         if users[name]['account_number'] is None:
#             users[name]['account_number'] = generate_random_account_number()
#             print(f"Account successfully created for {name}")
    
#         entered_pin = input("Enter your PIN: ")
#         if entered_pin != users[name]['pin']:
#             print("Wrong PIN. Try again.")
#         else:
#             account_number = users[name]['account_number']
#             print(f"\nWelcome, {name}\nAccount Number: {account_number}")
            
#             while True:
#                 print("1. Check Balance")
#                 print("2. Deposit")
#                 print("3. Withdraw")
#                 print("4. Exit")
                
#                 choice = input("Please enter your choice: ")
#                 if choice == "1":
#                     check_balance(name)
#                 elif choice == "2":
#                     Amount = float(input("How much do you want to deposit?: $"))
#                     deposit(name, Amount)
#                 elif choice == "3":
#                     Amount = float(input("How much do you want to withdraw?: $"))
#                     withdraw(name, Amount)
#                 elif choice == "4":
#                     print("Thank you for using the bank app. Goodbye!")
#                     break
#                 else:
#                     print("Invalid choice. Please enter a valid number.")
#     else:
#         print("Name not registered.")

# bank_app()

# bank_app()

# import random
# # registered user and their details
# User = {
#     "Ayomide":{"pin":"0000","account_number":None,"balance":0.00},
#     "Adeola":{"pin":"0000","account_number":None,"balance":0.00},
#     "Abdullah":{"pin"}


# # # # # Article = input("Enter your article here: ")
# # # # # print("Do you want to make any changes in the article? ")
# # # # # res = input("enter 'yes if you want to make a change and 'no' if you don't want to: ").capitalize()
# # # # # if res == "Yes":
# # # # #     old_word = input("Which word would you like to change? ")
# # # # #     new_word = input("Which word would you like to replace the old word with? ")
# # # # #     print(Article.replace(old_word,new_word))
# # # # # else:
# # # # #     print(Article)
# # # # # # Define the questions, options, and the correct answers as seperate lists
# # # # # questions = ["What is 2+3?","What is 7-2?","What is 5*3?","What is 12/4?","What is 9+6?"]
# # # # # options =[ ["A. 4","B. 5"],["A. 5","B. 1"],["A. 15","B. 8"],["A. 3","B. 5"],["A. 10","B. 15"]]
# # # # # answer =["B","A","A","A","B"]
# # # # # # Initialize score 
# # # # # score = 0
# # # # # # Loop through each question 
# # # # # for i in range(len(questions)):
# # # # #     print(questions[i])
# # # # #     for option in options[i]:
# # # # #         print(option)
# # # # #     user_answer = input("Please enter the letter of your answer: ").strip().upper()
# # # # #     #Check if the answer is correct
# # # # #     if user_answer == correct_answer[i]:
# # # # #         score += 5
# # # # # print(f"\nYour final score is: {score} out of {len(questions)*5}")


# # # # # # Define the questions, options, and the correct answers as seperate lists
# # # # # questions = ["What is 2+3?","What is 7-2?","What is 5*3?","What is 12/4?","What is 9+6?"]
# # # # # options =[ ["A. 4","B. 5"],["A. 5","B. 1"],["A. 15","B. 8"],["A. 3","B. 5"],["A. 10","B. 15"]]
# # # # # answer =["B","A","A","A","B"]
# # # # # # Initialize score 
# # # # # score = 0
# # # # # # Loop through each question 
# # # # # for question in range(len(questions)):
# # # # #     print(questions[question])
# # # # #     for option in options[question]:
# # # # #         print(option)
# # # # #     user_answer = input("Please enter the letter of your answer: ").strip().upper()
# # # # #     #Check if the answer is correct
# # # # #     if user_answer == answer[question]:
# # # # #         print("correct")
# # # # #     else:
# # # # #         print("wrong")
# # # # #         score += 5
# # # # # print(f"\nYour final score is: {score} out of {25}")

# # # #    # Define the questions, options, and the correct answers as seperate lists
# # # # questions = ["What is 2+3?","What is 7-2?","What is 5*3?","What is 12/4?","What is 9+6?"]
# # # # options =[ ["A. 4","B. 5"],["A. 5","B. 1"],["A. 15","B. 8"],["A. 3","B. 5"],["A. 10","B. 15"]]
# # # # answer =["B","A","A","A","B"]
# # # # # Initialize score 
# # # # score = 0
# # # # # Loop through each question 
# # # # for question in range(len(questions)):
# # # #     print(questions[question])
# # # #     for option in options[question]:
# # # #         print(option)
# # # #     user_answer = input("Please enter the letter of your answer: ").strip().upper()
# # # #     #Check if the answer is correct
# # # #     if user_answer == answer[question]:
# # # #         print("correct")
# # # #     else:
# # # #         print("wrong")
# # # #     if user_answer == answer[question]:
# # # #         score += 5
# # # # print(f"\nYour final score is: {score} out of {25}")
# # # mylist = [1,2,3,4,5,6,7,8,9,10]
# # # for name in mylist:
# # #     print(name)
# # # # Print Odd Number from the list
# # # mylist = [1,2,3,4,5,6,7,8,9,10]
# # # for name in mylist:
# # #     if name %2 ==0:
# # #         print(name)
# # # mylist = [1,2,3,4,5,6,7,8,9,10]
# # # list_sum = 0
# # # for name in mylist:
# # #     list_sum = list_sum + name

# # #     print(list_sum)

# # questions = ["What is 2+3?","What is 7-2?","What is 5*3?","What is 12/4?","What is 9+6?"]
# # options =[ ["A. 4","B. 5"],["A. 5","B. 1"],["A. 15","B. 8"],["A. 3","B. 5"],["A. 10","B. 15"]]
# # answer =["B","A","A","A","B"]
# # # Initialize score 
# # score = 0
# # # Loop through each question 
# # for question in range(len(questions)):
# #     print(questions[question])
# # for option in range(5):
# #         print(options[option])
# # # user_answer = input("Please enter the letter of your answer: ").strip().upper()
# # #     #Check if the answer is correct
# # # if user_answer == answer[question]:
# # #         print("correct")
# # # else:
# # #         print("wrong")
# # # if user_answer == answer[question]:
# # #         score += 5
# # # print(f"\nYour final score is: {score} out of {25}")


# import random
# # Registered User and their data
# Users = {"Ayomide":{"Pin":"0000","account_number":None,"balance":0},
#          "Adeola":{"Pin":"0000","account_number":None,"balance":0},
#          "Abdullah":{"Pin":"0000","account_number":None,"balance":0},
#          "Shola":{"Pin":"0000","account_number":None,"balance":0},
#          "Mayowa":{"Pin":"0000","account_number":None,"balance":0},
#          "Timi":{"Pin":"0000","account_number":None,"balance":0}
# }
# # Generate Random Account Number
# def Generate_Random_Account_Number():
#     return random.randint(1000000000,9999999999)

# # Check Balance of the User
# def check_balance(user):
#     y = Users[user]["balance"]
#     print(f"Your account balance is: $ {y}")

# #Deposit
# def deposit(user,Amount):
#     if Amount <0:
#         print("Error!!! You cannot deposit a negative amount")
#     else:
#         Users[user]["balance"] = Users[user]["balance"]+Amount
#         y = Users[user]["balance"]
#         print(f"You have successfully deposited ${Amount}. New balance is $ {y}")

# #Withdraw
# def Withdraw(user,Amount):
#     if Amount > Users[user]["balance"]:
#         print(f"Insufficient balance")
#     else:
#         Users[user]["balance"]=Users[user]["balance"]-Amount
#         y = Users[user]["balance"]
#         print(f"{Amount} has successfully been withdrawn. New balance is $ {y}")
    
# # deposit("Mayowa",100000)
# # check_balance("Mayowa")
# # Withdraw("Mayowa",100)
# def bank_app():
#     name = input(f"Input your account name: ")
#     if name in Users:
#         if Users[name]["account_number"] is None:
#             Users[name]["account_number"] = Generate_Random_Account_Number()
#             print(f"Account successfully opened for {name}")

#         entered_pin = input("Enter your pin: ")
#         if entered_pin != Users[name]["Pin"]:
#             print(f"Incorrect PIN. Kindly provide a correct PIN")
#         else:
#             account_number = Users[name]["account_number"]
#             print(f"\nWelcome, {name} \nAccount Number: {account_number}")

#             while True:
#                 print("1. Check Balance")
#                 print("2. Deposit")
#                 print("3. Withdraw")
#                 print("4. Exist")

#                 choice = input(f"Please Enter Your Choice: ")
#                 if choice =="1":
#                     check_balance(name)
#                 elif choice =="2":
#                     Amount = float(input(f"How much do you want to Deposit?: "))
#                     deposit(name,Amount)
#                 elif choice=="3":
#                     Amount = float(input(f"How much do you want to withdraw?: "))
#                     Withdraw(name,Amount)
#                 elif choice =="4":
#                     print(f"Thank you for using the bank app")
#                     break
#                 else:
#                     print(f"Invalid Choice. Please enter a valid number")
#     else: 
#         print(f"Name not registed.")

# bank_app()

# def new_account(name):
#     Users.update{name:{}}

#  # # # Article = input("Enter your article here: ")
# # # # # print("Do you want to make any changes in the article? ")
# # # # # res = input("enter 'yes if you want to make a change and 'no' if you don't want to: ").capitalize()
# # # # # if res == "Yes":
# # # # #     old_word = input("Which word would you like to change? ")
# # # # #     new_word = input("Which word would you like to replace the old word with? ")
# # # # #     print(Article.replace(old_word,new_word))
# # # # # else:
# # # # #     print(Article)
# # # # # # Define the questions, options, and the correct answers as seperate lists
# # # # # questions = ["What is 2+3?","What is 7-2?","What is 5*3?","What is 12/4?","What is 9+6?"]
# # # # # options =[ ["A. 4","B. 5"],["A. 5","B. 1"],["A. 15","B. 8"],["A. 3","B. 5"],["A. 10","B. 15"]]
# # # # # answer =["B","A","A","A","B"]
# # # # # # Initialize score 
# # # # # score = 0
# # # # # # Loop through each question 
# # # # # for i in range(len(questions)):
# # # # #     print(questions[i])
# # # # #     for option in options[i]:
# # # # #         print(option)
# # # # #     user_answer = input("Please enter the letter of your answer: ").strip().upper()
# # # # #     #Check if the answer is correct
# # # # #     if user_answer == correct_answer[i]:
# # # # #         score += 5
# # # # # print(f"\nYour final score is: {score} out of {len(questions)*5}")


# # # # # # Define the questions, options, and the correct answers as seperate lists
# # # # # questions = ["What is 2+3?","What is 7-2?","What is 5*3?","What is 12/4?","What is 9+6?"]
# # # # # options =[ ["A. 4","B. 5"],["A. 5","B. 1"],["A. 15","B. 8"],["A. 3","B. 5"],["A. 10","B. 15"]]
# # # # # answer =["B","A","A","A","B"]
# # # # # # Initialize score 
# # # # # score = 0
# # # # # # Loop through each question 
# # # # # for question in range(len(questions)):
# # # # #     print(questions[question])
# # # # #     for option in options[question]:
# # # # #         print(option)
# # # # #     user_answer = input("Please enter the letter of your answer: ").strip().upper()
# # # # #     #Check if the answer is correct
# # # # #     if user_answer == answer[question]:
# # # # #         print("correct")
# # # # #     else:
# # # # #         print("wrong")
# # # # #         score += 5
# # # # # print(f"\nYour final score is: {score} out of {25}")

# # # #    # Define the questions, options, and the correct answers as seperate lists
# # # # questions = ["What is 2+3?","What is 7-2?","What is 5*3?","What is 12/4?","What is 9+6?"]
# # # # options =[ ["A. 4","B. 5"],["A. 5","B. 1"],["A. 15","B. 8"],["A. 3","B. 5"],["A. 10","B. 15"]]
# # # # answer =["B","A","A","A","B"]
# # # # # Initialize score 
# # # # score = 0
# # # # # Loop through each question 
# # # # for question in range(len(questions)):
# # # #     print(questions[question])
# # # #     for option in options[question]:
# # # #         print(option)
# # # #     user_answer = input("Please enter the letter of your answer: ").strip().upper()
# # # #     #Check if the answer is correct
# # # #     if user_answer == answer[question]:
# # # #         print("correct")
# # # #     else:
# # # #         print("wrong")
# # # #     if user_answer == answer[question]:
# # # #         score += 5
# # # # print(f"\nYour final score is: {score} out of {25}")
# # # mylist = [1,2,3,4,5,6,7,8,9,10]
# # # for name in mylist:
# # #     print(name)
# # # # Print Odd Number from the list
# # # mylist = [1,2,3,4,5,6,7,8,9,10]
# # # for name in mylist:
# # #     if name %2 ==0:
# # #         print(name)
# # # mylist = [1,2,3,4,5,6,7,8,9,10]
# # # list_sum = 0
# # # for name in mylist:
# # #     list_sum = list_sum + name

# # #     print(list_sum)

# # questions = ["What is 2+3?","What is 7-2?","What is 5*3?","What is 12/4?","What is 9+6?"]
# # options =[ ["A. 4","B. 5"],["A. 5","B. 1"],["A. 15","B. 8"],["A. 3","B. 5"],["A. 10","B. 15"]]
# # answer =["B","A","A","A","B"]
# # # Initialize score 
# # score = 0
# # # Loop through each question 
# # for question in range(len(questions)):
# #     print(questions[question])
# # for option in range(5):
# #         print(options[option])
# # # user_answer = input("Please enter the letter of your answer: ").strip().upper()
# # #     #Check if the answer is correct
# # # if user_answer == answer[question]:
# # #         print("correct")
# # # else:
# # #         print("wrong")
# # # if user_answer == answer[question]:
# # #         score += 5
# # # print(f"\nYour final score is: {score} out of {25}")


# import random
# # Registered User and their data
# Users = {"Ayomide":{"Pin":"0000","account_number":None,"balance":0},
#          "Adeola":{"Pin":"0000","account_number":None,"balance":0},
#          "Abdullah":{"Pin":"0000","account_number":None,"balance":0},
#          "Shola":{"Pin":"0000","account_number":None,"balance":0},
#          "Mayowa":{"Pin":"0000","account_number":None,"balance":0},
#          "Timi":{"Pin":"0000","account_number":None,"balance":0}
# }
# # Generate Random Account Number
# def Generate_Random_Account_Number():
#     return random.randint(1000000000,9999999999)

# # Check Balance of the User
# def check_balance(user):
#     y = Users[user]["balance"]
#     print(f"Your account balance is: $ {y}")

# #Deposit
# def deposit(user,Amount):
#     if Amount <0:
#         print("Error!!! You cannot deposit a negative amount")
#     else:
#         Users[user]["balance"] = Users[user]["balance"]+Amount
#         y = Users[user]["balance"]
#         print(f"You have successfully deposited ${Amount}. New balance is $ {y}")

# #Withdraw
# def Withdraw(user,Amount):
#     if Amount > Users[user]["balance"]:
#         print(f"Insufficient balance")
#     else:
#         Users[user]["balance"]=Users[user]["balance"]-Amount
#         y = Users[user]["balance"]
#         print(f"{Amount} has successfully been withdrawn. New balance is $ {y}")
    
# # deposit("Mayowa",100000)
# # check_balance("Mayowa")
# # Withdraw("Mayowa",100)

# # Add New User
# def add_new_user():
#     name = input(f"Enter your name")
# # Check if the user exist
#     if name in Users:
#         print("{name} already exist")
#         return None
# # Create a new user with random account number
#     pin = input("Set your 4 digit pin")
#     account_number = Generate_Random_Account_Number()

#     Users[name]= {"Pin":pin,"account_number":account_number,"balance":0}
#     print(f"You have successfully created account for {name} with account number {account_number}")


# def bank_app():
#     User_type = input(f"Are you a new customer or an existing customer")
#     if User_type == "New Customer":
#         name = add_new_user()
#     name = input(f"Input your account name: ")
#     if name in Users:
#         if Users[name]["account_number"] is None:
#             Users[name]["account_number"] = Generate_Random_Account_Number()
#             print(f"Account successfully opened for {name}")

#         entered_pin = input("Enter your pin: ")
#         if entered_pin != Users[name]["Pin"]:
#             print(f"Incorrect PIN. Kindly provide a correct PIN")
#         else:
#             account_number = Users[name]["account_number"]
#             print(f"\nWelcome, {name} \nAccount Number: {account_number}")

#             while True:
#                 print("1. Check Balance")
#                 print("2. Deposit")
#                 print("3. Withdraw")
#                 print("4. Exist")

#                 choice = input(f"Please Enter Your Choice: ")
#                 if choice =="1":
#                     check_balance(name)
#                 elif choice =="2":
#                     Amount = float(input(f"How much do you want to Deposit?: "))
#                     deposit(name,Amount)
#                 elif choice=="3":
#                     Amount = float(input(f"How much do you want to withdraw?: "))
#                     Withdraw(name,Amount)
#                 elif choice =="4":
#                     print(f"Thank you for using the bank app")
#                     break
#                 else:
#                     print(f"Invalid Choice. Please enter a valid number")
#     else: 
#         print(f"Name not registed.")       
# bank_app()





# import random
# # Registered User and their data
# Users = {"Ayomide":{"Pin":"0000","account_number":None,"balance":0},
#          "Adeola":{"Pin":"0000","account_number":None,"balance":0},
#          "Abdullah":{"Pin":"0000","account_number":None,"balance":0},
#          "Shola":{"Pin":"0000","account_number":None,"balance":0},
#          "Mayowa":{"Pin":"0000","account_number":None,"balance":0},
#          "Timi":{"Pin":"0000","account_number":None,"balance":0}
# }
# # Generate Random Account Number
# def Generate_Random_Account_Number():
#     return random.randint(1000000000,9999999999)

# # Check Balance of the User
# def check_balance(user):
#     y = Users[user]["balance"]
#     print(f"Your account balance is: $ {y}")

# #Deposit
# def deposit(user,Amount):
#     if Amount <0:
#         print("Error!!! You cannot deposit a negative amount")
#     else:
#         Users[user]["balance"] = Users[user]["balance"]+Amount
#         y = Users[user]["balance"]
#         print(f"You have successfully deposited ${Amount}. New balance is $ {y}")

# #Withdraw
# def Withdraw(user,Amount):
#     if Amount > Users[user]["balance"]:
#         print(f"Insufficient balance")
#     else:
#         Users[user]["balance"]=Users[user]["balance"]-Amount
#         y = Users[user]["balance"]
#         print(f"{Amount} has successfully been withdrawn. New balance is $ {y}")
    
# # deposit("Mayowa",100000)
# # check_balance("Mayowa")
# # Withdraw("Mayowa",100)

# # Add New User
# def add_new_user():
#     name = input(f"Enter your name: ")
# # Check if the user exist
#     if name in Users:
#         print("Name already exist")
#         return None
# # Create a new user with random account number
#     pin = input("Set your 4 digit pin: ")
#     account_number = Generate_Random_Account_Number()
# # Create a dictionary to store new user details
#     Users[name]= {"Pin":pin,"account_number":account_number,"balance":0}
#     print(f"You have successfully created account for {name} with account number {account_number}")
#     return name

# #Transaction Menu
# def transaction_menu(name):
#     account_number = Generate_Random_Account_Number()
# #     account_number = Users[name]["account_number"]
# #     y = Generate_Random_Account_Number()
#     print(f"\nWelcome, {name}\nAccount Number: {account_number}")
            
#     while True:
#                 print("1. Check Balance")
#                 print("2. Deposit")
#                 print("3. Withdraw")
#                 print("4. Exit")

#                 choice = input(f"Please Enter Your Choice: ")
#                 if choice =="1":
#                     check_balance(name)
#                 elif choice =="2":
#                     Amount = float(input(f"How much do you want to Deposit?: "))
#                     deposit(name,Amount)
#                 elif choice=="3":
#                     Amount = float(input(f"How much do you want to withdraw?: "))
#                     Withdraw(name,Amount)
#                 elif choice =="4":
#                     print(f"Thank you for using the bank app. \nHave a nice day")
#                     break
#                 else:
#                     print(f"Invalid Choice. Please enter a valid number")

# # Bank Application
# def bank_app():
#     print("Welcome to Mayork Bank App!")
#     print("Are you an existing or new customer?")
#     print("1. Existing Customer")
#     print("2. New User")
    
#     user_type = input("Please enter 1 for existing customer or 2 for new user: ")      
#     if user_type == "1":
#         name = input("Enter your account name: ")
#         if name not in Users:
#             print("Name not registered.")
#             return
#     elif user_type == "2":
#         name = add_new_user()
#         if name is None:
#             return
#     else:
#         print(f"Invalid input.")
#         return
#     # Proceed with PIN validation and transactions for both new and existing users
#     entered_pin = input("Enter your PIN: ")

#     if entered_pin != Users[name]["Pin"]:
#             print("Wrong PIN. Try Again.")
#     else:
#          transaction_menu(name)
# bank_app()













# # Here is the game list 
# game_list = [0,1,2]

# # A function that will display the game_list 0,1,2
# def display_game(game_list):
#     print("Here is the current list: ")
#     print(game_list)

# # Call out the function
# display_game(game_list)

# # Function to pick a position
# def position_choice():
    
#     choice = " "
    
#     while choice not in ["0","1","2"]:
        
#         choice = input("Pick a position (0,1,2): ")
        
#         if choice not in ["0","1","2"]:
#             print("Sorry,  Invalid Choice!")
            
#     return int(choice)

# position_choice()

# def replacement_choice(game_list,position):
    
#     user_placement = input("Type a string to place at a position: ")
    
#     game_list[position] = user_placement 
    
#     return game_list


# replacement_choice(game_list,1)

# def gameon_choice():
    
#     choice = "Wrong"
    
#     while choice not in ["Y","N"]:
        
#         choice = input("Keep Playing (Y or N): ").upper()
        
#         if choice not in ["Y","N"]:
#             print("Sorry,  Invalid Choice! Choose Y or N")
            
#     if choice =="Y":
#         return True
#     else:
#         return False

# gameon_choice()

# game_on = True
# game_list = [0,1,2]

# while game_on:
    
#     display_game(game_list)
    
#     position = position_choice()
    
#     game_list = replacement_choice(game_list,position)
    
#     display_game(game_list)
    
#     game_on = gameon_choice()
    
    





# The Milestone Project TicTok Game

# # # **Step 1: Write a function that can print out a board. Set up your board as a list, 
# # where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.**

# from IPython.display import clear_output

# def display_board(board):
#     print(board[7]+ "|" + board[8] + "|"+ board[9])
#     print(board[4]+ "|" + board[5] + "|"+ board[6])
#     print(board[1]+ "|" + board[2] + "|"+ board[3])

# test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)

# from IPython.display import clear_output

# def display_board(board):
#     clear_output()  # Remember, this only works in jupyter!
    
#     print('   |   |')
#     print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
#     print('   |   |')
#     print('-----------')
#     print('   |   |')
#     print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
#     print('   |   |')
#     print('-----------')
#     print('   |   |')
#     print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
#     print('   |   |')

# test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)

# # **Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. 
# #     Think about using *while* loops to continually ask until you get a correct answer.**

# def player_input():
    
#     marker = ""
    
#     while marker != "X" and marker != "O":
#         marker = input("Player1: Chose X or O: ").upper()
#     if marker == "X":
#         return ("X","O")
#     else:
#         return ("O","X")
        

# player_input()

# player1_marker, player2_marker = player_input()

# player2_marker

# # **Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'),
# #     and a desired position (number 1-9) and assigns it to the board.**

# def place_marker(board, marker, position):
#     board[position] = marker

# # **TEST Step 3:** run the place marker function using test parameters and display the modified board

# place_marker(test_board,'$',8)
# display_board(test_board)













# Object Oriented Program (OOP)

# MyList = [1,2,3,4]

# type(MyList)

# myset = set()

# type(myset)

# class Sample():
#     pass

# my_sample = Sample()

# type(my_sample)

# class Dog():
#     def __init__(self,breed,name,spots):
#         self.breed = breed
#         self.name = name
#         self.spots = spots
        

# my_dog = Dog(breed="Latino",name = "Maxy", spots = False)

# my_dog.spots

# my_dog.name

# my_dog.breed

# class Info():
#     def __init__(self,name,Age,Location,State):
#         self.name = name
#         self.Age = Age
#         self.Location = Location
#         self.State = State

# mylist = Info(name = "Mayowa", Age = 22, Location = "Idi Ape", State = "Oyo State")

# mylist.Age

# mylist.Location

# mylist.name

# class Animal():
    
#     # Class object attributes
#     # Same for any instance of class
    
#     species = "mammal"
#     owner = "Jack"
    
    
#     def __init__(self,name,breed,location):
        
#         # Attributes
#         # We take in arguement
#         # Assign it using self.attributes_name
#         self.name = name
#         self.breed = breed
#         self.location = location
        
        
#     # Operations/Actions ----> Methods
    
#     def bark(self,number):
#         print("Woof! My name {}".format(self.name))
#         print(f"Yuppie!!! My breed is {self.breed} and my number is {number}")
#         print(f"Yo! My location is {self.location}")
    

# y = Animal("Jack","Lab","US")

# y = Animal(name ="Punda",breed= "Local", location = "Ibadan")



# y.breed

# y.location

# y.name

# y.species

# y.owner

# y.bark(1)











# class Circle():
    
#     # CLASS OBJECT ATTRIBUTE
#     pi = 3.14
    
#     def __init__(self,radius=1):
        
#         self.radius = radius
        
#     # METHOD
    
#     def get_circumference(self):
#         return self.radius * self.pi * 2

# my_circle = Circle()

# my_circle.pi

# my_circle.radius

# my_circle.get_circumference()



# class Rectangle():
    
    
#     add = 30  
#     pi = 3.14
    
#     def __init__(self,length,bredth):
        
#         self.length = length
#         self.bredth = bredth
#         self.AArea = self.pi*length**2
        
#     def NewArea(self):
#         return self.pi*self.length**2
        
        
     
    
#     def Area(self):
#         return self.length * self.bredth * self.add
    
    
#     def Perimeter(self):
#         return 2*(self.length+self.bredth)

# my_Area = Rectangle(1,5)

# my_Area.Area()

# my_Area.Perimeter()

# my_Area.Area()



# class Animal():
    
#     def __init__(self):
        
#         print("ANIMAL CREATED")
        
#     def who_am_i(self):
#         print("I am an Animal")
        
#     def eat(self):
#         print("I am eating") 

#   myanimal = Animal()

# myanimal.eat()

# myanimal.who_am_i()

# class Dog(Animal):
    
#     def __init__(self):
#         Animal.__init__(self)
#         print("Dog Created")
        
#     def who_am_i(self):
#         print(  "I am a dog!")
        
#     def eat(self):
#         print("I cannot eat")
        
#     def bark(self):
#         print("Woof")

# mydog = Dog()

# mydog.eat()

# mydog.who_am_i()

# mydog.bark()

  



# Polymorphism

#   class Dog():
        
#         def __init__(self,name):
#             self.name = name
            
#         def speak(self):
#             return self 

# numb = int(input("Please enter the number for the factorial: "))
# x = 1
# while numb>0:
#     x *=numb
#     numb -=1
# print("The factorial is ",x)

# import random

# randoms = random.randint(1,51)
# attempt = 5

# while attempt >0:
#     guess = int(input("Please enter your guess to the random game: "))
#     if guess > randoms:
#         print("Guess is too high, please try again")
#     elif guess < randoms:
#         print("Guess is too low, please try again")
#     else:
#         print("Correct Guess")
#         break
#     attempt -=1
# else:
#     print("Attempt exceeded, number was actually",randoms)



# Write a program that keeps asking the user for a password until they

# correct_password = "Secret"
# password = ""

# while password != correct_password:
#     password = input("Enter the password: ")
    
#     if password == correct_password:
#         print("Correct password")
        
#     else: print("Incorrect Password try again")

# Write a program that takes an integer input from the user and uses a while loop to print a countdown from that number

# number = int(input("Provide a number: "))
# while number>=0:
#     print(number)
#     number -=1

# Write a program that takes an integer n from the user and uses a while loop to print all even numbers from 1 to n

# user = int(input("Please enter your number: "))
# while user >1:
    
#     if user % 2 != 0:
#         user -=1
#         continue
#     print(user)
#     user -=1

# base = int(input("Provide a number for base: "))
# exponent = int(input("Provide a number for exponent: "))

# while base >0:
#     t = base **exponent
    
#     print(t)
#     break
    
    

# write a program that will count the number of vowels in a string

# vowel = ["a","e","i","o","u"]
# myinput = input("Please enter a text: ")
# lens = len(myinput)
# a =0    # Collect the count of vowel

# counter = 0   #Collect the count of the input
# while lens >0:
#     x = myinput[a]
    
#     if x in vowel:
#         counter +=1
#     lens -=1
#     a+=1
# print(counter)
    

# 23rd Ooctober Class

# Write a program that tracks the inventory of items in a store. The user should be able to add or remove items
# and the program should display the current inventory after each operation.
# The program stops when the user decides to exit.
# The current store inventory is ("eggs":40,"fish:200","Bread":343,"yam":2)
# Sample input and output: Enter operation (add/remove/exist): add
        

# inventory = {"eggs":40, "fish":200, "bread":343, "yam":2}

# while True:
#     operate = input("Please type either add/remove/exit for your operation to the dictionary: ")
#     if operate == "add":
#         item = input("Enter item you want to add: ")
        
#         if item in inventory:
#             quantity = int(input("Enter the quantity: "))
#             inventory[item] += quantity
#             print(inventory)
            
#         else: print("Invalid. Please try again later")
            
#     elif operate =="remove":
#         item = input("Which item do you want to remove?: ")
        
            
            
#         if item in inventory:
#             quantity = int(input("Enter the quantity: "))
#             inventory[item] -= quantity
#             print(inventory)
            
#         else: print("Invalid. Please try again")

#     elif operate == "exit":
#         print("Have a nice day 😀")
#         break
#     else: 
#         print("Invalid Selection!!!!!")
      
        

# For Loop Class

# for item in [1,2,3]:
#     print(item)

# cities = ["New york","Abuja","Ibadan","Tokyo","Paris"]

# for item in cities:
#     print(item)

# for item in cities:
#     print(f"City:{item}")

# items = {"guitar","keyboard","drumset","Violin"}
# for item in items:
#     print(item)

# # Dictionary
# # To print the keys
# capitals = {"Lagos":"Ikeja","Ogun":"Abeokuta","Ondo":"Akure","Plateau":"Jos"}
# for y in capitals:
#     print(y)

# # To print Values
# capitals = {"Lagos":"Ikeja","Ogun":"Abeokuta","Ondo":"Akure","Plateau":"Jos"}
# for y in capitals.values():
#     print(y,end=" ")

# # To print the whole dictionary
# capitals = {"Lagos":"Ikeja","Ogun":"Abeokuta","Ondo":"Akure","Plateau":"Jos"}
# for y in capitals.items():
#     print(y)

# capitals = {"Lagos":"Ikeja","Ogun":"Abeokuta","Ondo":"Akure","Plateau":"Jos"}
# for x,y in capitals.items():
#     print(f"Keys: {x}")

#     print(f"Values: {y}")

# mystring = "Python is fun"
# for char in mystring:
#     print(char, end= "")


# mystring = "Python is fun"
# for char in mystring.split():
#     print(char)

# mystring = "Python is fun"
# for char in mystring:
#     print(char)

# for x in cities:
#     if x =="Tokyo":
        
#     break
#         print(x)

# for x in cities:
#     if x =="Tokyo":
#         break
#     print(x)


# cities = ["New york","Abuja","Ibadan","Tokyo","Paris"]

# for y in cities:
#     if y == "Ibadan":
#         continue
#     print(y,end =" , ")

# for x in range(6):
#     print(x)

# enumerate() function

# Fruits = ["apple","banana","cherry"]


# for index, fruit in enumerate(Fruits, start = 0):
#     print(f"{index}: {fruit}")

# for item in enumerate(Fruits):
#     print(item)

# for index in range(len(Fruits)):
#     print(f"{index+1}:{Fruits[index]}")

# Assignment

# Write a program that takes an integer input from the user and uses a loop to calculate the
# sum of its digit. Print the sum

# Number = input("Provide integers: ")
# sum_of_digits = 0
# for i in Number:
#     sum_of_digits += int(i)
    
# print(f"The sum of the digit {Number} is {sum_of_digits}" )
    


# Collect a string from the user and use loops to count the number of vowels and consonants in the string. Print the counts

# Vowels =["a","e","i","o","u"]
# Consonants =["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
# string =input("Input a string: ")
# Vowels_Count = 0
# Consonants_Count = 0

# for i in string:
#     if i in Vowels:
#         Vowels_Count += 1
        
        
#     else:
#         if i in Consonants:
#             Consonants_Count += 1
        
    
# print(f"The Vowels in the word {string} is {Vowels_Count}")
# print(f"The Consonants in the word {string} is {Consonants_Count}")


# Write a program that takes an integer from the user and prints the multiplication table for that number up to 12.

# User_input = int(input("Enter a number: "))

# User_input = input("Enter a number: ")
# multiplication = range(1,13)
# for i in multiplication:
#     x = i*int(User_input)

#     print(f"{i}*{int(User_input)}={x}")
    

# Collect a string from the user and use loop to reverse the string.
# Print the reversed string. Do not reverse the string

# User_String = input("Input a string: ")
# for i in User_String:
#     y = User_String[::-1]
# print(y)

# Write a program that takes a list of numbers (entered as comma seperated values) from the user and removes any
# duplicates values. Print the new list.
# Do not use the set() constructor

# User_Input = input("Enter your numbers: ")
# Unique_List =[]
# for i in User_Input:
#     if i not in Unique_List:
#         Unique_List.append(i)
# print(Unique_List)  
# # y = User_Input.split(",")
# # print(y)



# User_Input = input("Enter your numbers: ")
# Unique_List = []
# for i in User_Input:
#     if i not in Unique_List:
#         Unique_List.append()

# User_Input = input("Enter your numbers: ")
# Unique_List =[]
# for i in User_Input.split(","):
#     if i not in Unique_List:
#         Unique_List.append(i)
# print(Unique_List)  




# adj = ["strong","majestic","playful"]
# animals = ["lion","eagle","python"]

# for a in adj:
#     for b in animals:
#         print(a,b)

# List Comprehention

# adj = ["strong","majestic","playful"]
# animals = ["lion","eagle","python"]

# for a in adj:
#     for b in animals:
#         print(a,b)

# newlist = []
# for y in adj:
#     newlist.append(y)
# print(newlist)

# newlist2 = [x for x in adj if "a" in x]
# print(newlist2)

# newlist3 = [x for x in range(1,19) if x%2==1]
# newlist4 = [x for x in range(1,19) if x%2==0]

# print(newlist3)
# print(newlist4)

# import re

# quote = "There's only one thing I hate more than lying: Skin milk. Which is water that's lying about being milk. -Swanson"

# #To search the positional number of a word
# re.search("milk",quote)

# re.search("milk",quote).group()

# # To find return the string and it appears in a list
# re.findall("milk",quote)

# len(re.findall("milk",quote))

# # to Split the string by the quoted word"
# re.split("milk",quote)

# # To split it by a fullstop
# re.split("\.",quote)

# # To replace the word "I" with "You"
# re.sub("I","You",quote)

# re.sub("milk","berry",quote)

# # To replace Milk with berry and the replacement comes only on the first apperance 
# re.sub("milk","berry",quote, count = 1)

# names = ["Finn Bindeballe","Geir Anders Berge","HappyCodingRobot", "Ron Cromberge", "Sohil"]

# # Find the people with first name and last name only

# import re

# regex = "^\w+ \w+$"
# for name in names:
#     result = re.search(regex,name)
#     if result:
#         print(name)

# regex = "^\w+ \w+$"
# for name in names:
#     result = re.search(regex,name)
#     if result:
#         print(name)

# # <!-- # Write a program that takes an integer input n from the user and prints
# # the first n numbers in the fibonacci sequence. -->
# # # Example:
# # # Input: 10
# # # Output: 0,1,1,2,3,5,8,13,21,34

# User_Input = int(input("Enter a number: "))
# # First two terms
# n1, n2 = 0, 1
# count = 0
# # Check if the number of terms is valid
# if User_Input <=0:
#     print("Please enter a positive number")
# # If there is only one term, return n1
# elif User_Input ==1:
#     print("Fibonacci sequence upto", User_Input, ":")
#     print(n1)
# else:
#     print("Fibonacci Sequence:")
#     while count < User_Input:
#         print(n1, end = " ")
# # #         print(n1,end=" ")
#         nth = n1 + n2
        
# #         #Update Values
#         n1 = n2
#         n2 = nth
#         count +=1
        
# # # print(f"count: {count} ")



# def fibonancci(n):
    
#     if n==1:
#         return 0
    
#     if n==2:+
#         return 1
#     return fibonancci(n-1)+fibonancci(n-2)
# for i in range(1,11):
#     print(fibonancci(i))

# User_Input = int(input("Ener a number: "))
# Output = [0,1]
# if User_Input==1:
#     print(0)
# elif User_Input ==2:
#     print(1)
# elif User_Input <=0:
#     print("Invalid!!! Input a valid positive number")
    
# for i in range(User_Input):
#     if i >2:
#         Output.append()

# language = ["python","java","C++","JS"]
# newlist = ["hello" for x in language]

# newlist2 = [x if x!= "C++" else "C#" for x in language]
# print(newlist2)

# # Set Comprehension example
# newset = {x.upper() for x in language}
# print(newset)

# # Dictionary Comprehention
# newdict = {x: len(x)  for x language}





# # any() - returns true if at least one element in the iterable is true, otherwise false
# #and
# # all() - returns true if all elements in the iterable are true, otherwise false

# number = [1,2,3,4,5]
# y = any([x > 5 for x in number])
# print(y)
# print(type(y))

# # Using all
# z = all([x>1 for x in number])
# print(z)
# print(type(z))

# # Collect a string from the user and only print the word that start with the letter "s"

# Statement = input("Write the word:").lower()
# for i in Statement.split(" "):
#     if i[0]=="s":
#         print(i)
    

# # Password = input("What is your password? ")
# # number = range(0,10)
# # character = ["!","@","#","$","%","^","&","*","()"]
# # for x in Password:
# #     if x in character or x in number or len(x)>=8 or x.upper or x.lower:
# #         print("Strong Password")
        
# #     else: print("Weak Password")


# # Password = input("What is your password? ")
# # character = ["!","@","#","$","%","^","&","*","()"]
# # for x in Password:
# #     if len(x)>=8:
# #         print("true")
# #     elif x.isupper():
# #         print("true")
# #     elif x.islower():
# #         print("true")
# #     elif x.isdigit():
# #         print("true")
# #     elif x in character:
# #         ptint("true")
    


# Password = input("Enter a password: ")
# Character = ".,!@#$%^&*()"
# integer = "1234567890"
# char = "abcdefghijklmnopqrstuvwxyz"
# uchar =char.upper()
# c1 = False
# c2 = False

# x,a,z,e = 0,0,0,0
# if len(Password) >= 8:
#     c1 = True
# for y in Password:
#     if y in char:
#         x+=1
#     elif y in uchar:
#         a+=1
#     elif y in integer:
#         z+=1
#     elif y in Character:
#         e+=1
    
        
# if x >0 and a >0 and z >0 and e >0:
#     c2 = True
# if c1 and c2:
#     print("True")
    
# else:
#     print("False")

# # Fibonacchi sequence
# n = int(input("Enter the stopping number: "))
# print("0,1",end = ",")
# a = 1
# b = 1
# m = 0
# c = 0

# while n -2 > 0:
#     if c % 2 ==0:
#         m+=a
#         a = m
        
#     else:
#         m +=b
#         b = m
        
#     n-=1
#     c +=1
#     print(f"{m}",end =",")



# # #1. Write a program that calculate the average of three floating point numbers, printing the result to the screen


# User_Input1 = float(input("Provide a floating point1: "))
# User_Input2 = float(input("Provide a floating point2: "))
# User_Input3 = float(input("Provide a floating point3: "))

# sum_of_User_Input = User_Input1 + User_Input2 + User_Input3

# if type(User_Input1)==float and type(User_Input2)==float and type(User_Input3)==float:
#     avg = sum_of_User_Input/3
#     print(f"Average of {User_Input1},{User_Input2},{User_Input3} is {avg:.2f}")







# 2. # Write a program that prints out the square of each integer in a sequence of your choosing(Use range)

# for i in range(60):
#     square_Int = i**2
#     print(square_Int)

# #3. Modify your previous program to exclude any number whose square is between 10 and 50

# for i in range(60):
#     square_Int = i**2
    
#     if square_Int not in range(10,51):
#         print(square_Int)

# #4. Write a program to print out all integers that are perfect square less than or equal to 100
# for i in range(1,101):
#     if (i**0.5).is_integer():
#         print(f'{i} is a perfect square')

# # 5. Write a program to print all positive integers less than 300 that are divisible by 3 but not divisible by 2
# for i in range(1,300):
#     if i%3==0 and i%2!=0:
#         print(i)

# # #6. Write a program to test if a positive integer is prime. (Reminder: An integer is a prime if it cannot be divided evenly
# # by all smaller positive integers beginning with 2.)

# 30/October Class on Function


# def greet():
#     print("Hello World")

# greet()

# def secondgreet(name):
#     print("Hello",name)

# secondgreet("Mujeeb")

# def add_number(num1,num2):
#     sum = num1 + num2
#     print("Sum: ",sum)
# add_number(2,3)

# # Parameters Vs Arguments
# # Parameter are like variables listed inside inside the parenthesis in the function defination.













# # # # Default Argument
# # # Functions are allowed to have default argument value.
# # The default argument are used when explicit value are pass to the parameters during function call

# def greet(name, message="Hello"):
#     print(message,name)
    
# greet("Mujeeb")
# greet("Mayowa","Welcome")
    

# # Mutable Default Values
# # Using a mutable default value like a list or dictionary in function definitions can lead to unexpected behavior because
# #the default value is shared across all calls to the function

# our_list = ["Potato","Rice","Beans"]

# def add_item(item,my_list=[]):
#     my_list.append(item)
#     return my_list

# print(add_item(1))
# print(add_item("ball"))
# print(add_item(4))
# print(add_item("yam",our_list))

# type(None)

# def add_itemm(item,my_list=None):
#     if my_list is None:
#         my_list = []
        
#     my_list.append(item)
#     return my_list
# print(add_itemm(1))
# print(add_itemm("ball"))
# print(add_itemm(4))
# print(add_itemm("yam",our_list))

# # Using *args and **kwargs in function
# # these are used for handling arbitrary number of arguments using special symbols

# def add_all(*numbers):
#     return sum(numbers)

# print(add_all(1,2,3,4,45,0))

# # Using Kwargs
# def greet(**words):
#     for key, value in words.items():
#         print(f"{key}:{value}")
#         print(type(words))
# greet(name="john",greeting = "hello")

# # Recursion in Functions
# # Recursion is a tecnique where a function calls itself 
# # to solve smaller instances of the same problem until reaching a base case.

# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     else:
#         return base * power(base, exponent -1)
# print(power(2,3))
# print(power(4,0))
# print(power(4,1))



# # Variable Scope
# # They are 3 main types of variable scope in python
# #1. Local SCope - Variables declared inside a function. They are accessible only within that function

# def fun():
#     m = 10
#     print(m)
# fun()

# # 2. Enclosing (NonLOcal) Scope- They are variables in the local scope of enclosing functions. Accessbile within
# # nesred functions.

# def out():
#     e = 20
#     def inn():
#         print(e)
#     inn()
# out()

# #3. Global Scope or variable - They are variables declared at the top level of a script or module.
# # Accessible throughout the module.

# m = 20
# def man():
#     print(m)
# man()

# age = 39
# def increase_age():
#     global age
#     age +=1

# def out():
#     e = 20
#     def inn():
#         nonlocal e
#         e = 25
#     print(e)
#     inn()
#     print(e)
    
# out()

# # Summary:
# # global: Used to modify global variables inside a function.
# # nonLocal: Used to modify enclosing variables inside nested functions
# # These keywords help control the scope and visibility of variable ensuring the changes are made to the intended variabl.

# #Docstrings

# def sum_numbers(a,b):
#     return a+b
# sum_numbers(2,4)

# def detector(a):
#     if a%2==0:
#         return "True"
#     else: return "False"
# detector(4)

# check = int(input("Enter a number: "))
# prime = False
# if check <=1:
#     pass
# elif check%2==0:
#     pass
# elif check ==2 or check ==3 or check ==5:
#     prime = True
    
# else:    
#     for i in range(3,int(check*0.5)+1,2):
#         if check%i ==0:
#             prime = False
#             break
#         else:
#             prime = True
# if prime == False:
#     print(f"The number {check} is not prime")
# else:
#     print(f"The number {check} is prime")

# # Write a function is_prime(n) that returns True if n is a prime number and false otherwise 



# def lesser_of_two_evens(a,b):

#     if a%2==0 and b%2==0:
#         if a > b:
#             return b
#         elif a ==b:
#             return "Equal"
#         else: return a
    
#     elif a%2==1 or b%2==1:
#         if a > b:
#             return a
#         elif a ==b:
#             return "Equal"
#         else: return b
            


# lesser_of_two_evens(4,4)

# def spy_game(list_of_int):
#     if 

# # Write a function range_check(num,low,high) that accept a string 
# # and calculates the number of uppercase letter and lower case letters

# L_text = "abcdefghijklmnopqrstuvwxyz"
# U_text = L_text.upper()
# def upper_lower(text):
#     a = 0
#     b = 0
#     for i in text:
#         if i in U_text:
#             a +=1
    
#         elif i in L_text:
#             b+=1
#     print(f"The number of Uppercase letter is {a}")
#     print(f"The number of lowercase lettr is {b}")


# upper_lower("EqualLy")

# def unique_list(list_items):
#     new_list = []
#     for i in list_items:
#         if i not in new_list:
#             new_list.append(i)
#     print(new_list)
    


# unique_list([1,2,3,4,5,6,3,4,5,5,2,0,2])       

# [1,2,4,0,0,7,5]

# # Write a function spy_game(list_of_ints) that takes in a list of integers and return True if is contains 007 in order.
# # def spy_game(list_of_int):
# #     new_list = []
# #     for i in list_of_int:
# #         if i ==0:
# #             new_list.append(i)
# #         elif i==7:
# #             new_list.append(i)
# #     if new_list == [0,0,7]:
# #         print("true")
# #     else: print("false")

# def spy_game(list_of_int=[]):
#     list_of_int = (input("What is the number: "))
#     new_list = " "
#     for i in list_of_int:
#         if i ==0:
#             new_list.append(i)
#         elif i ==7:
#             new_list.append(i)
#             print(new_list)
#     if new_list == [0,0,7]:
#         print("true")
#     else: print("false")
            
    
                
# # spy_game()          
    

# def spy_game(list_of_int):
#     list_of_int = (input("What is the number: "))
#     new_list = []
#     print(list_of_int)
#     for i in list_of_int.split(","):
#         if i =="0":
#             new_list.append(i)
#         elif i =="7":
#             new_list.append(i)
#         print(new_list)
#     if ['0','0','7'] == new_list:
#         print("true")
#     else:print("false")
# spy_game([])

# def spy_game(list_of_int):
#     list_of = input("What is the number: ").split(",")
#     new_list = []
# #     print(list_of_int)
#     for i in list_of:
# #         print(int(i))
# #         print(type(int(i)))
#         if int(i) == 0:
#             new_list.append(int(i))
#         elif int(i) ==7:
#             new_list.append(int(i))
#         print(new_list)
#     if [0,0,7] == new_list:
#         print("true")
#     else:print("false")
# spy_game("")

# spy_game([1,2,4,0,0,7,5])

# spy_game([1,0,4,0,7,9,5])

# # Write a function vol(radius) that computes the volume of sphere given its radius
# def vol(radius):
#     return 3.14*radius**4
# vol(2)

# letter2 = " "
# def is_pangram(text):
#     for z in text:
#         global letter2
#         if z == " ":
#             continue
#         elif z in letter2:
#             continue
#         else:
#             letter2 +=z
            
#     if len(letter2) ==26:
#         return True
#     else:
#         return False
    
# e = is_pangram("the quick brown fox jump over the dog") 
# print(e)

# def increment(number,by):
#     return number + by

# result = increment(10,by=1)
# print(result)

# # def multiply(x,y):
# #     a = x * y
# #     print(a)
# # multiply(2,3)

# def multiply(x,y):
#     return x * y
# #     a = x * y
# #     print(a)
# multiply(2,3)

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print(multiply(2,3,4,5))

# def save_user(**user):
#     print(user)
# save_user(id =1 , name = "John", age = 22)  




# Assignment

# # /john.doe@company.com/john.doe@hr.company.com
# # local part: john.doe/john.doe
# # Domain Part: company.com/hr.company.com
# # Domain Name:            /company.com
# # Sub_domain:              /hr
# # Top-Level Domain (TLD): com
# # # Domain Lablels: The individual parts of the domain name seperated by dots. (.), which are company. and com./hr. company. amd com

# text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%'*+-/=?^_{|}~."
# def email_validator(email):
    
# #     Check for exatly one "@" symbol
#     Condition = False
#     result1 = True
#     if email.count("@")==1:
#         pass
#     else: 
#         result1 = False
       
#     # Split the email into local and domain parts
#     local_part, domain_part = email.split("@")
# #     print(local_part)
# # #     # Validate the local part
#     result2 = True
#     if len(local_part) <= 64:
#         pass
#     else: 
#         result2 =False
        
    
#     result3 = True
#     for i in local_part:
#         if i in text:
#             pass
#         else:
#             result3 = False
#             break
            
#     result4 = True  
#     if local_part.endswith(".") or local_part.startswith(".") or ".." in local_part:
#         result4 = False 
#     else:
#         pass
# #     print(result1,result2,result3,result4)
    
    
#     if result1 and result2 and result3 and result4==True:
#         condition = True
    
#     condition1 = False
# #     print(domain_part)
#     text2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-."
#     domain_partt,TLD = domain_part.split(".")
# #     print(domain_part,TLD )
    
#     result5 = True
#     if domain_partt.endswith(".") or domain_partt.startswith(".") or ".." in domain_part:
#         result5 = False
#     else: 
#         pass
    
#     result6 = True
#     if domain_partt.endswith("-") or domain_partt.startswith("-") or "--" in domain_part:
#         result5 = False
    
#     result7 = True
#     if TLD.endswith("-") or TLD.startswith("-"):
#         result7 = False
#     else:
#         pass
    
#     result8 = True
#     if len(domain_partt) > 63 and len(TLD) > 63:
#         result8 = False
    
#     result9 = True
#     if len(TLD) <2:
#         result9 = False
#     else:
#         pass
        
#     result10 = True
#     if len(email)>254:
#         result10 = False
#     else:
#         pass
   
     
# #     print(result5,result6,result7,result8,result9,result10) 
    
#     if result5 and result6 and result7 and result8 and result9 and result10==True:
#         condition1 = True
        
#     if condition and condition1 == True:
#         print("Valid Email")
#     else:
#         print("Invalid Email")


# email_validator("john@gmail.com")
    

# email_validator("john.doe@company.com")

# L_text = "abcdefghijklmnopqrstuvwxyz"
# U_text = L_text.upper()
# print(U_text)



# def add_contact():

#     name = input("Enter contact name: ")
#     phone_number = input("Enter phone number: ")
#     favorite = input("Mark as favorite (y/n): ").lower() == "y"

#     contact = {"name": name,"phone_number": phone_number,"favorite": favorite}


#     phonebook.append(contact)
#     print(f"Contact '{name}' has been added.")

# def view_contacts():
#     # Display all contact in the phone book
#     if not phonebook:
#         print("There are no contacts in the phonebook.")
#         return

#     print("\nList of Contacts:")
    
#     for contact in phonebook:
#         favorite_str = "FAVORITE" if contact["favorite"] else ""
#         print(f"\nName: {contact['name']} ({favorite_str})")
#         print(f"Phone Number: {contact['phone_number']}")

# def update_contact(phone_number):
# # """Updates the information of a contact based on their phone number."""
#     for index, contact in enumerate(phonebook):
#         if contact["phone_number"] == phone_number:
#             new_name = input("Enter new name (or leave blank to keep current): ") or contact["name"]
#             new_phone_number = input("Enter new phone number (or leave blank to keep current): ") or contact["phone_number"]
#             new_favorite = input("Mark as favorite (y/n) [current: {}]: ".format(contact["favorite"])) or contact["favorite"]
#             new_favorite = new_favorite.lower() == "y"

#             phonebook[index] = {"name": new_name,"phone_number": new_phone_number,"favorite": new_favorite}
#             print(f"Contact '{phone_number}' has been updated.")
#             return

#     print(f"Contact with phone number '{phone_number}' not found.")

# def delete_contact(phone_number):
# # """Removes a contact from the phonebook based on their phone number."""
#     for index, contact in enumerate(phonebook):
#         if contact["phone_number"] == phone_number:
#             del phonebook[index]
#             print(f"Contact with phone number '{phone_number}' has been deleted.")
#             return

#     print(f"Contact with phone number '{phone_number}' not found.")

# def search_contact(name):
# # """Searches for a contact by their exact name."""
#     found_contacts = []
#     for contact in phonebook:
#         if contact["name"] == name:
#             found_contacts.append(contact)

#     if found_contacts:
#         print("\nFound Contacts:")
#         for contact in found_contacts:
#             favorite_str = "FAVORITE" if contact["favorite"] else ""
#             print(f"\nName: {contact['name']} ({favorite_str})")
#             print(f"Phone Number: {contact['phone_number']}")
#     else:
#         print(f"No contact found with name '{name}'.")

# def mark_favorite(phone_number):
# # """Marks a contact as a favorite."""
#     for contact in phonebook:
#         if contact["phone_number"] == phone_number:
#             contact["favorite"] = True
#             print(f"Contact '{phone_number}' marked as favorite.")
#             return

#     print(f"Contact with phone number '{phone_number}' not found.")

# def unmark_favorite(phone_number):
# # """Unmarks a contact as a favorite."""
#     for contact in phonebook:
#         if contact["phone_number"] == phone_number:
#             contact["favorite"] = False
#             print(f"Contact '{phone_number}' unmarked as favorite.")
#             return

#     print(f"Contact with phone number '{phone_number}' not found.")


# # Initialize phonebook as an empty list
# phonebook = []

# while True:
#     print("\nPhone Book Menu:")
#     print("1. Add Contact")
#     print("2. View Contacts")
#     print("3. Update Contact")
#     print("4. Delete Contact")
#     print("5. Search Contact")
#     print("6. Mark Favorite")
#     print("7. Unmark Favorite")
#     print("8. Exit")
    
    
    
# choice = input("Enter your choice (1-8): ")
    
#     if choice == '1':
#         add_contact()
#     elif choice == '2':
#         view_contacts()
#     elif choice == '3':
#         phone_number = input("Enter phone number of the contact to update: ")
#         update_contact(phone_number)
#     elif choice == '4':
#         phone_number = input("Enter phone number of the contact to delete: ")
#         delete_contact(phone_number)
#     elif choice == '5':
#         name = input("Enter name of the contact to search: ")
#         search_contact(name)
#     elif choice == '6':
#         phone_number = input("Enter phone number of the contact to mark as favorite: ")
#         mark_favorite(phone_number)
#     elif choice == '7':
#         phone_number = input("Enter phone number of the contact to unmark as favorite: ")
#         unmark_favorite(phone_number)
#     elif choice == '8':
#         print("Exiting phonebook...")
#         break
#     else:
#         print("Invalid choice. Please enter a number between 1 and 8.")






# def addition(num1, num2):
# # """Adds two numbers and returns the result."""
#     return num1 + num2

# def subtraction(num1, num2):
# # """Subtracts the second number from the first and returns the result."""
#     return num1 - num2

# def multiplication(num1, num2):
# # """Multiplies two numbers and returns the result."""
#     return num1 * num2

# def division(num1, num2):
# # """Divides the first number by the second and returns the result.
# # Handles division by zero."""
#     if num2 == 0:
#         print("Error: Division by zero is not allowed.")
#         return None
#     return num1 / num2

# while True:
#     print("\nSelect operation:")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Exit")

#     choice = input("Enter your choice from 1 to 5: ")

#     if choice in ('1', '2', '3', '4'):
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))

#         if choice == '1':
#             result = addition(num1, num2)
#         elif choice == '2':
#             result = subtraction(num1, num2)
#         elif choice == '3':
#             result = multiplication(num1, num2)
#         else:
#             result = division(num1, num2)

# #         if result is not None:
# #             print(f"{num1} {choice} {num2} = {result}")

#     elif choice == '5':
#         print("Exiting calculator...")
#         break
# else:
#     print("Invalid choice. Please enter a number between 1 and 5.")



# # The Librarian
# # Create a simple library management system where user can add, view, update, and delete books in a file named the_librarian.py
# # Requirements:
# #     Each book should have the following attributes
# # Title(string)
# # Author(string)
# # Year of publication(int)
# # ISBN(string)
# # Available(boolean)
# # add_book(): Add a new book to the library.
# # view_books(): Display all the books in the library.
# # update_book(isbn): Update the information of a book given its ISBN.
# # delete_book(isbn): Remove a book from the library using its ISBN.
# # search_book(title): Search for a book by its exact title.
# # borrow_book(isbn): Mark a book as borrowed (not available)
# # return_book(isbn): Mark a book as returned(available)
    
# # User_Interface:
# # USe a loop to display a menu and prompt the user for an action above until they choose to exit.
# # Assume the user always input the correct data types. 

# book_shelves = {
# "Bola beg for food":{"Author":"Wicked","Year of Publication":2001,"ISBN": "ISBN-234563477763","Available": True},
# "John Wick": {"Author":"Tobi","Year of Publication":2011,"ISBN": "ISBN-234542224","Available": True},
# "Micheal Farada":{"Author":"Lion King","Year of Publication":2011,"ISBN": "ISBN-23454223","Available": True},
# "Vampire":{"Author":"Mr White","Year of Publication":2021,"ISBN": "ISBN-2334454223","Available": True},
# "Game of Thrones":{"Author":"Manuel","Year of Publication":2020,"ISBN": "ISBN-23454223","Available": True},}

# def add_book(dic):
#     title = input("Please enter the title of the new book: ")
#     auth = input("What is the name of the author: ")
#     year =input("What is the year of publication?: ")
#     isbn = input("What is the ISBN Number?: ")
#     av = input("Please enter 1 if its available and 0 if its not available: ")
#     if av == "1":
#         ava = True
#     else:
#         ava = False
        
#     dic[title] = {"Author":auth,"Year of Publication":year, "ISBN":isbn, "Available":ava}
    
# def view_books(dic):
#     print(dic)
    
# def update_book(dic,isbn):
#     name = "NewBook"
#     for key,value in dic.items():
#         if value["ISBN"]==isbn:
#             name = key
#     if name = "NewBook":
#         print("Wrong, please isbn number is not available!")
#     else:
#         update = input("Please enter the update operation, please enter either: Author, Year of Publication, ISBN, Available: ")
#         updated_value = input("Please enter the value for it: ")
#         if update == "Year of Publication":
#             updated_value = int(updated_value)
#         elif update == "Available":
#             updated_value = bool(updated_value)
#         dic[name][update] = updated_value
        
# def delete_book(dic,isbn):
#     name = "Newbook"
#     for key,value in dic.items():
#         if value["ISNB"]==isbn:
#             name = key
#             dic.pop(key)
#             break
#     if name== "Newbook":
#         print("Wrong, please isbn number is not available!")
#     else:
#         print("Removed successfully! ")
        
# def search_book(dic,title):
#     if title in dic:
#         print(dic[title])
#     else:
#         print("Title not present, pleasere try")
        
# []            
        
            

# add_book(dic)

# print(book_shelves["Bola beg for food"]["ISBN"])



# y =0
# def exam_wizard(questions):
   
    
# #     Question1 = "What is a noun?"
# #     Answer1="A noun is a name of any person, animal, place or thing"
# #     Keyword1="name","person","animal","place","thing"
#     User_response = input("What is a noun?: ").lower()
#     a =0
#     if "name" in User_response:
#         a+=1
#     if "person" in User_response:
#         a+=1
#     if "animal" in User_response:
#         a+=1
#     if "place" in User_response:
#         a+=1
#     if "thing" in User_response:
#         a+=1
        
# #     global y
# #     y+=a
        
# #     print(y)
        
# #     b = 0    
#     User_response2 = input("What is a verb?: ")
# #     Answers2 = "Verb is an action word or a doing word"
# #     keyword2 = "action" ,"doing", "word"
    
#     if "action" in User_response2:
#         a+=2
#     if "doing" in User_response2:
#         a+=2
#     if "word" in User_response2:
#         a+=1
        
# # #     global y    
# #     y+=a
# #     print(y)
    
# # #     c = 0
#     User_response3 = input("What is data?: ")
# #     Answer= "Data is collection of facts, numbers, measurements, words"
# #     Keywords = "collection","numbers","measurement","words"

#     if "collection" in User_response3:
#         a+=2
#     if "numbers" in User_response3:
#         a+=1
#     if "measurement" in User_response3:
#         a+=1
#     if "words" in User_response3:
#         a+=1
# #     global y    
# #     y+=a
# #     print(y)
        
# # #     d = 0
#     User_response4 = input("What is an adjective?: ")
# #     Answer= "Adjective are words used to modify or describe a noun or pronoun"
# #     Keywords = "modify","noun","pronoun"

#     if "modify" in User_response3:
#         a+=2
#     if "noun" in User_response3:
#         a+=2
#     if "pronoun" in User_response3:
#         a+=1
# # #     global y     
# #     y+=a
# #     print(y)
    
# # #     e=0
#     User_response5 = input("What is an adverb?: ")
# #     Answer= "Adverb is a word or phrase that modifies or qualifies an adjective, verb, or other adverb"
# #     Keywords = "modifies","adjective","verb"

#     if "modifies" in User_response3:
#         a+=2
#     if "adjective" in User_response3:
#         a+=2
#     if "verb" in User_response3:
#         a+=1 
#     global y      
#     y+=a
    
    
#     print(f" Your final score is {y}/25")
    
    
    
    
          
        
        
        
    
        
# #     print(y)
    
# # exam_wizard("User_response")

# exam_wizard("User_response")

# # i = "i am a boy"
# # if "boy" in i:
# #     print("works")



# # def student_name(name):
# #     student = "Sam,Bayo,Bola,Kehinde"
# #     for i in student.split(","):
# #         print(i)

# student_name("student")


# # OOP- object Oriented programming
# # OOP is a programing paradigm that provides a means of structuring programs so that properties and behaviours are bundled into
# # individual objects. for example, an object could represent a person properties like a name, age, and address and behaviors such as
# # walking, talking, breathing, and running. In programming paradigms, objects only represent data. In python, and object oriented
# # programming in general,class names are typically singular. This is because a class represents a blueprint for a single entity or concept,
# # not a collection of entities. Each instance of the class corresponds  to one object of that type.


# Inheritance: Adoption of properties from the parent class into the child class.
# Polymorphism: Creation of many forms from one form.
# Abstraction: Displaying the necessary data and hiding unnecessary data.
# Encapsulation: Securing the info of the class

# # Defining a class in python
# class Employee:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
# #Primitive data structure vs classes

# employees = {
#     "adesina":{"name": "Adesina Oluwafemi","age":34,"position":"Captain","year_joined":2003},
#     "chinedu":{"name": "Chinedu Okeke","age": 35,"position":"Science officer","year_joined":2002},
#     "ifunanya":{"name":"Ifunanya Nkem","age":39,"position":"Chief Medical Officer","year_joined":1997}
# }

# print(employees["ifunanya"]["age"])

# class Employee:
#     def __init__(self,name,age,position,year_joined):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.year_joined=year_joined
    
#     def __str__(self):
#         return f"The employee name {self.name}, {self.age} years, {self.position}, joined in {self.year_joined}"
    
#     def years_of_service(self,current_year):
#         return current_year - self.year_joined
    
# # Creating an employee object
# adesina = Employee("Adesina Oluwafemi",34,"Captain",2003)
# chinedu =  Employee("Chinedu Okeke",35,"Science officer",2002)
# ifunanya =  Employee("Ifunanya Nkem",39,"Chief Medical Officer",1997)

# print(f" adesina year of experience is: {adesina.years_of_service(2024)}")
# print(adesina)
# print(ifunanya)
# print(ifunanya.position)

# # Benefit of using a class over dictionaries
# # 1. Encapsulation:
# # 2. Methods
# # 3. Initialization
# # 4. String representation

# class Dog:
#     def __init__(self,name,colour,breed):
#         self.name = name
#         self.colour = colour
#         self.breed = breed
        
        
#     def __str__(self):
#         return f"The dog named {self.name}, of colour {self.colour} is a {self.breed} type"
    
# Bingo = Dog("Bingo","Red","Husky")
# Jack = Dog("Jack","Black","Pitbull")

# print(Jack)

# # Class Attributes VS Instance Attributes
# # Class attributes have the same value for all class instances, while instance attributes can vary between instances

# class Dog:
#     species = "Canis familiaries"
#     def __init__(self,name,colour,breed):
#         self.name = name
#         self.colour = colour
#         self.breed = breed
        
        
#     def __str__(self):
#         return f"The dog named {self.name} of colour {self.colour} is a {self.breed} type"
    
# Bingo = Dog("Bingo","Red","Husky")
# Jack = Dog("Jack","Black","Pitbull")

# print(Jack.species)
# print(Bingo)


# class Car:
#     BASE_PRICE = 20000
#     Wheel = 4
    
#     def __init__(self,brand,model,colour,year):
#         self.brand = brand
#         self.model=model
#         self.colour=colour
#         self.year=year
#         self.price = self.calculate_price(year)
        
#     def calculate_price(self,year):
#         current_year = 2024
#         age = current_year-year
#         dep = 0.05
#         price1 = self.BASE_PRICE*(1-dep)**age
#         return max(5000,price1)
        
# car1 = Car("Toyota","Camry","Red",2020)
# print(f"{car1.price:.2f}")
        

# # Use the class keyword to declare a class. Then add class_name after it and give a colon to begin data insertions.
# class student:
# # Then call the "__init__" method. This is the constructor method for any class in python
# # We create a student class and then give the properties like name, standard, and roll number to it.
# # USe the self keyword to make sure that the properties are properly bound to the class.
# # There is no use of class declaration if we do not use the self keyword
#     def __init__(self,name,std,roll_no):
#         self.nm = name
#         self.std = std
#         self.rl_no = roll_no
# #There ar two methods inside the class
# # The first one getData() retrieves the instance attributes
# # The second one "setData" enables to change of the values of those attributes
#     def getData(self):
#         print("Student Name: ", self.nm)
#         print("Standard: ", self.std)
#         print("Roll number: ",self.rl_no)
       
#     def setData(self, name, std, roll_no):
#         self.nm = name
#         self.std = std
#         self.rl_no = roll_no
# # We create two objects for this class         
# stud = student("Om","4th","9")
# stud.getData()
# print() #To print a new line in between
# stud_1 = student("Hari","5th",14)
# stud_1.getData()
        

# print()

# class Players:
#     def __init__(self,Jersey_no,Name,Position,Club):
#         self.JN = Jersey_no
#         self.Nm = Name
#         self.Ps = Position
#         self.clb =Club
        
        
#     def getData(self,Jersey_no,Name,Position,Club):
#         print("Jeysey Number: ",self.JN)
#         print("Name: ",self.Nm)
#         print("Position: ",self.Ps)
#         print("Club: ",self.clb)
        
        
#     def 
        
        



# # Assignment

# # Fill in the class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
# # Look up the formulas for finding the distance and the slope of a line


# class Line:
#     def __init__(self,coor1,coor2):
#         self.coor1 = coor1
#         self.coor2 = coor2
    
#     def calculate_slope(self):
#         y1 = self.coor1[1]
#         y2 = self.coor2[1]
#         numerator = y2-y1
#         x1 = self.coor1[0]
#         x2 = self.coor2[0]
#         denominator = x2-x1

    
#         return numerator/denominator
    
#     def calculate_distance(self):
#         y1 = self.coor1[1]
#         y2 = self.coor2[1]
#         num1 = y2-y1
#         x1 = self.coor1[0]
#         x2 = self.coor2[0]
#         num2 = x2-x1
#         inside = num2**2+num1**2
#         return inside**0.5
        
    
# coord1 = (3,2)
# coord2 = (8,10)

# slope = Line(coord1,coord2)
# print(f"The slope of {coord1} and {coord2} is: {slope.calculate_slope()}")

# distance = Line(coord1,coord2)
# print(f"The distance between {coord1} and {coord2} is: {distance.calculate_distance():.2f}")


      




# class Arithemetic:
#     def __init__(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2
        
#     def addition(self):
#         add = self.num1 + self.num2
#         return add
#     def subtraction(self):
#         if self.num1>self.num2:
#             return self.num1-self.num2
#         if self.num2>self.num1:
#             return self.num2-self.num1
        
#     def multiplication(self):
#         product = self.num1*self.num2
#         return product
#     def division(self):
#         if self.num1>self.num2:
#             return self.num1/self.num2
#         if self.num2>self.num1:
#             return self.num2/self.num1
#         else: pass
# num1=5
# num2=10
# Answer = Arithemetic(5,10)
# print(f"The division of {num1} and {num2} is: {Answer.division()}")
# print(f"The addition of {num1} and {num2} is: {Answer.addition()}")
# print(f"The product of {num1} and {num2} is: {Answer.multiplication()}")
# print(f"The Difference of {num1} and {num2} is: {Answer.subtraction()}")            
    
    

# # Inheritance in Class

# class Parent:
#     hair_colour = "brown"
#     location = "Ibadan"
#     name = "Mayowa"
    
# class Child(Parent):
#     hair_colour = "blonde"
    
    
# print(Parent.hair_colour)  
# print(Child.hair_colour)
# print(Child.location)
# print(Child.name)


# class Book:
#     def __init__(self,title,author):
#         self.title = title
#         self.author = author
        
#     def get_description(self):
#         return f"{self.title} by {self.author}"
# class Fiction(Book):
#     def get_description(self,genre = "Fiction"):
#         return f"{super().get_description()}-Genre: {genre}"
# class NonFiction(Book):
#     def get_description(self,genre = "Non-Fiction"):
#         return f"{super().get_description()}-Genre: {genre}"   
# class ScienceFiction(Book):
#     def get_description(self,genre = "Science Fiction"):
#         return f"{super().get_description()}-Genre: {genre}" 
# book2 =NonFiction("Sapien","Yuval Noah")
# print(book2.get_description())



# # The self parameter
# # The self parameter is a reference to the current instance of the class,
# # and is used to access variables that belongs to the class, and is used to access variables that belongs to the class.

# Class Arithemetic:
#     def __init__(this,num1,num2):
#         this.num1 = num1
#         this.num2 = num2
        
#     def Addition(abc):
#         return abc.num1 + abc.num2
    
# num = Arithemetic(1,3)
# print(num.Addition())

# print(isinstance(num,Arithemetic))

# # Magic Dunder Methods in Class- magic dunders are predefined methods in python that start and end with double underscore.
# # They enable custom behavior for build in operations.
# #__init__=initializes object attributes
# #__str__=returns a string representation of the object for debugging ideally a valid python expression
# #__re

# class Person:
#     def __init__(self,name):
#         self.name = name
    
#     def __str__(self):
#         return f"Person named {self.name}"
    
#     def __repr__(self):
#         return f"Person (name={self.name!r})"
    

# class Point:
#     def __init__(self,x,y):
#         self.x =x
#         self.y =y
#     def __add__(self,other):
#         return Point(self.x+other.x,self.y+other.y)
#     def __str__(self):
#         return f"{self.x},{self.y}"
    
# v1 = Point(4,2)
# v2 = Point(5,2)
# result = v1 + v2
# print(result)



# # __len__ return the length of the object, used by len()

# # Polymorphism- The term means "many forms" and in python refers to methods/functions/operation with the same name that can
# # be executed on many objects or classes

#     # polymorphism

# class Painter:
#     def create(self):
#         print("Painter")
# class Musician:
#     def create(self):
#         print("Musician")
# class Artist:
#     def create(self):
#         print("Acing")
        
# misheal = Painter()
# mujeeb = Musician()
# stephen = Artist()

# for i in (misheal,mujeeb,stephen):
#     i.create()

# class Device:
#     def op



# class Dog():
#     def __init__(self,breed):
#         self.breed = breed
        
        

# my_list = Dog(breed="Lab")

# my_list.breed

#  class Dog():
        
#         # Class Object Attributes
#         # Same for any instance of a class
        
#         species = "mammal"
        
#         def __init__(self,breed,name,spots):
#             self.breed = breed
#             self.name = name
#             self.spots = spots
            
#         # 
        
        

# my_list = Dog("Lab","Sammy",False)

# my_list.breed

# my_list.name

# my_list.spots

# my_list.species

#  class Dog():
        
#         # Class Object Attributes
#         # Same for any instance of a class
        
#         species = "mammal"
        
#         def __init__(self,breed,name):
#             self.breed = breed
#             self.name = name
            
            
#         def bark(self,number):
#             print(f" WOOF! My number is {number} My name is {self.name}")
        
        

# my_dog = Dog("Lab","Frankie")

# my_dog.bark(1)

# my_dog.name

# my_dog.breed

# class Circle:
#     pi = 3.14
    
#     def __init__(self,radius=1):
        
#         self.radius=radius
        
#     def Circumference(self):
#         return 2*self.pi*self.radius**2
    

# my_circle = Circle(20)

# my_circle.pi

# my_circle.radius

# my_circle.Circumference()

# class Animal():
    
#     def __init__(self):
#         print("Animal Created")
        
#     def who_am_i(self):
#         print("I am an animal")
        
#     def eat(self):
#         print("I am eating")

# myanimal=Animal()

# myanimal.eat()

# myanimal.who_am_i()

# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         print("Dog Created")
        
#     def who_am_i(self):
#         print("I am a doog")

# mydog = Dog()

# mydog.eat()

# mydog.who_am_i()

# Polymorphism

# class Dog():
#     def __init__(self,name):
#         self.name = name
#     def speak(self):
#         return self.name + " says woof!"

# class Cat():
#     def __init__(self,name):
#         self.name = name
        
#     def speak(self):
#         return self.name + " says meow!"

# niko = Dog("niko")
# felix = Cat("felix")

# print(niko.speak())

# print(felix.speak())

# for i in [niko,felix]:
#     print(i.speak())

# class Animal:
    
#     def __init__(self,name):
#         self.name = name
        
        
#     def speak(self):
#         raise NotImplementedError("Subclass must implement Method")
    
    

# class Dog(Animal):
    
#     def speak(self):
#         return self.name + " say woof!"

# class Cat(Animal):
    
#     def speak(self):
#         return self.name + " say meow!"

# fido = Dog("Fido")

# isis = Cat("Isis")

# print(fido.speak())

# print(isis.speak())

# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         raise NotImplementedError("Subclass must implement this abstarct method")
# myAnimal = Animal("gooaal")
# myAnimal.speak()

# # Special Methods

# class Book():
#     def __init__(self,title,author,pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#     def __str__(self):
#         return f"{self.title} by {self.author}"
#     def __len__(self):
#         return self.pages

# b = Book("Python rock","Jose",200)
# print(b)
# str(b)
# len(b)

# # del b

# print(b)

# Assignment



# class Cylinder:
#     pi = 3.14
#     def __init__(self,height,radius):
#         self.height=height
#         self.radius=radius
#     def Volume(self):
#         return self.pi*(self.radius**2)*self.height
    
#     def Surface_area(self):
#         return (2*self.pi*self.radius*self.height)+2*(self.pi*self.radius**2)
        
    
# Cyl = Cylinder(2,3)
# print(f"The volume of the cylinder is {Cyl.Volume()}")
# print(f"The Surface area of the cylinder is {Cyl.Surface_area()}")


# class Account:
#     def __init__(self,name,balance):
#         self.name = name
#         self.balance=balance
# #         self.deposited_amount = deposited_amount
# #         self.withdraw = withdraw
        
#     def __str__(self):
#         return f"Name of the account {self.name}\nAccount Balance {self.balance}"
        
# #     def Owner(self):
# #         print(f" Name of the account {self.name}\nAccount Balance {self.balance}")
        
#     def Deposit(self,Number):
#         self.balance += Number
#         print(f"{Number} was deposited \nTotal Balance is {self.balance}")
        
#     def Withdraw(self,Number2):
#         self.balance -= Number2
#         if Number2 > self.balance:
#             print(f"Insufficient fund, your balance is {self.balance}")
#         else:
#             print(f"Withdraw accepted. {Number2} was withdrawn.\nRemaining balance is {self.balance}")
        
        
# Acc = Account("Mayowa",1000)
# print(Acc)
# # Account.balance()
# # Account.Deposit()
# # Account.deposited_amount()
# # Acc.Owner()
# # Acc.Deposit(200)
# # Acc.Withdraw(150)
# # print(Acc)
       
        

# Error Handling

# # Error and Exceptions in python
# # Error in python are issues that arises when the interpreter encounters something it doesn't understand or cant process.
# # Common types Include:
# #Exceptions are events that disrupt the normal flow of a range. They can be handled using try-except block. e.g

# try:
#     result = 10/0
# except ZeroDivisionError:
#     print(f"Cannot divide by zero.")
# except NameError:
#     print("A variable is not defined")
# except Exception as e:
#     print(f"An error occured: {e}")
# else:
#     print(result)
#     print("operation successful")
# finally:
#     print("execution done")



# while True:
#     try:
#         age = int(input("Please enter your age: "))
#         break
#     except ValueError:
#         print("Invalid input. Please enter a valid integer for your age.")
# print(f"Your age is {age}")

# # Creating or Raising Custom Exception
# class InsufficientFundsError(Exception):
#     def __init__(self,message="Insufficient funds in the account"):
#         self.message = message
#         super().__init__(self.message)
        
# # Bank Account Class:
# class BankAccount:
#     def __init__(self,balance = 6600):
#         self.balance = balance
        
        
#     def deposit(self,amount):
#         if amount<=0:
#             raise ValueError("Deposit amount must be positive.")
#         self.balance += amount
#         print(f"Deposited ${amount}. New balance is ${self.balance}.")
#     def withdraw(self,amount):
#         if amount <=0:
#             raise ValueError("Withdrawal amount must be positive.")
#         if amount > self.balance:
#             raise InsufficientFundsError(f"Attempted to withdraw ${amount}, but only ${self.balance} available.")
#         self.balance -=amount
#         print(f"Withdrew ${amount}. New balance is ${self.balance}.")
        
# Samson = BankAccount()
# Samson.deposit(74678)
# Samson.withdraw(40)
# Samson.withdraw(400)

        
    
        

# account = BankAccount(100) # Creating a new account with $100
# try:
#     account.deposit(50)
#     account.withdraw(20)
# except InsufficientFundsError as e:
#     print(e)
# except ValueError as e:
#     print(e)
    
# print("worked fine")

# # This approach ensures that specific business logic errors, like insufficient funds, are clearly communicated and handled appropriately in the application.
# # The function of good software is to make the complex appear to br simple

# # Error Vs Exceptions
# #Errors occur during the compilation of the code,while exception occurs during the execution of the code.
# #Errors are usually syntax-related problems that prevent the code from being executed, while exceptions are runtime-related
# #problems that occur when the code tries to perform an invalid operation.

# # Best Practices
# #Be specific with exceptions: Catch specific exceptions instead of using a broad except block.
# #Clean-up actions: Use the finally block for clean-up actions that must run no matter what.
# # Avoid bare except clauses: Catching all exceptions silently can hide bugs.

# while True:
#     try:
#         age = input("enter your age: ")
#     except KeyboardInterrupt:
#         print("\nYou have decided to end the program")



# class NegativeNumberError(Exception):
#     def __init__(self,message="This is a negative number. Input a positive number"):
#         self.message = message
#         super().__init__(self.message)
    
# class Numbers:
#     def __init__(self,number):
#         self.number = number
        
#     def check_positive(self):
#         if self.number <0:
#             raise NegativeNumberError
# Num = Numbers(-67)
# try:
#     Num.check_positive()
# except NegativeNumberError as e:
#     print(e)
# else: print("Positive Number")
# finally: print("Operation Done")
        

# try:
#     first_num = float(input("Enter first number"))
#     second_num = float(input("Enter second number"))
#     result = first_num/second_num
# except ZeroDivisionError:
#     print("Denominator ")

# class NegativeNumberError(Exception):
#     def __init__(self,message="This is a negative number. Input a positive number"):
#         self.message = message
#         super().__init__(self.message)
# class Exercise:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def safe_divide(a,b):
#         return self.a/self.b
#     if self.b=0:
#         raise ZeroDivisionError

# def safe_divide(a,b):
#     try:
#         a = float(a)
#         b = float(b)
        
#         result = a/b
        
#         if b ==0:
#             raise ZeroDivisionError
#         else:return result
    
# #     except Exception as e:
# #         print(f"Error Occured: {e}")
        
#     except ZeroDivisionError:
#         return f"Cannot divide by Zero"
    
#     except ValueError:
#         return f"Value Error. Input are not numbers"
#     except TypeError:
#         return f"TypeError. Input is not a valid number"
#     except NameError:
#         return f"NameError. Input is not a valid number"
    

# try:        
#     safe_divide(10,hgdgc)
# except NameError: 
#     print("NameError. Input is not a valid number")




# File Handling



# # Opening a file
# # File = open("filename.txt","mode")
# # Modes: "r":Read(default mode, file must exist)
# #"w": Write(create a new file or truncates an existing one).
# # "a": Append(create a new file or write to the end of an existing)
# # "b": Binary mode (useful for non-text files)

# file = open("mynote.txt","r")

# content =file.read()  #reads entire file
# print(content)

# file = open("mynote.txt","r")
# content1 = file.readlines()
# print(content1)



# file = open("mynote.txt","r")
# content2 = file.readline()
# print(content2)

# file = open("mynote.txt","r")
# content =file.read()  #reads entire file
# print(content)


# file.seek(7)

# content1 = file.readlines()
# print(content1)


# with open("mynote.txt","w") as file:
#     file.write("plantain is the best thing in Nigeria! \n")
#     file.writelines("Chelsea is the worst club in the world\n")
#     file.writelines("""Sqi is good
# He is bad
# They are not good for eachother""")
# file = open("mynote.txt","r")
# print(file.read())



# file = open("mynote.txt","r")
# content =file.read()  #reads entire file
# print(content)


# with open("mynote.txt","w") as file:
#     file.write("plantain is the best thing in Nigeria! \n")
#     file.writelines("Chelsea is the worst club in the world\n")
#     file.writelines("""Sqi is good
# He is bad
# They are not good for eachother""")
# # file = open("mynote.txt","r")
# # print(file.read())
# with open("mynote.txt","r") as file:
#     print(file.read())



# with open("mynote.txt","a") as file:
#     file.write("This would be added at the end\n")

# with open("mynote.txt","r") as file:
#     print(file.read())
    
# file.close()

# Modules and Packages

# A modules is a single file containing python code that can be imported and used in other python program. Modules allow you to
# organize and reuse code.

# import datetime
# time = datetime.datetime.today()
# time1 = datetime.datetime.now()



# print(time)
# print(time1)


# specific_date = datetime.date(2024,2,22)
# print(specific_date)
# print(type(specific_date))

# # Formatted Dates
# date_string = "2024-07-30 14:53:20"
# parsed_date = datetime.datetime.strptime(date_string,"%Y-%m-%d %H:%M:%S")
# print(datetime.time(2,33,23,33))
# print(datetime.date(2024,10,23))
# print(parsed_date)

# import math

# y = math.sqrt(49)
# print(y)

# y = math.sqrt(9)
# print(y)

# z = math.pow(5,3)
# print(z)

# print(math.pi)

# i = math.radians(90)
# print(i)
# print(math.sin(i))

# print(math.log(10))
# print(math.log10(100))

# !pip install beautifulsoup4

# import requests

# from bs4 import BeautifulSoup

# url = "https://www.jumia.com"
# response = requests.get(url)
# if reponse.status_code==200:
#     soup = BeautifulSoup(response.content,'html.parser')
#     header = soup.find('hi')
    
#     if header:
#         print("Header:",header.get_text())
        
#     main_content = soup.find('main')
#     if main_content:
#         print("Main content:",main_content.get_text())
#     else:
#         paragraphs =  soup.find_all('p')
#         for p in paragraphs:
#             print("Paragrahp:",p.get_text())
# else:
#     print("Failed to retrieve the webpage. Status code:,",response.status_code)

# # Regular Expressions
# # They are sequence of characters that define search patterns.
# # They are used for string matching and manupulation

# # Key functions:
# # re.compile(pattern): compile a regex pattern into a regex object
# # re.search(pattern,string): searches for the pattern in the string and returns the first match object
# # re.match(pattern,string): checks for a match only at the begining of a date string
# # re.findall(pattern,string): returns all non-overlapping matches of the pattern in the sting in the list
# #re.iter(pattern,string): returns an iterator yielding mach 

# import re

# # Simple serach
# pattern = r"\bclass\b"
# text = "We are in a python class learning python"
# match = re.search(pattern,text)
# if match:
#     print("match found: ",match.group())

# # "\d" = where they are digit
# # "\D" = where we dont have digits
# # "\w" = where we have digit, letter and underscore
# # "\W" = where we dont have letters digit and underscore
# # "\s" = where we have space tab and line breaks
# # "\S"=  where we dont have space tab and line breaks
# # "\b"= To search the position of a particular words and match a word boundary
# # "\B" = To search the position of a particular word and doesnt have to be word bound
# # "\." = Match
# # "\*" = to match*
# # 

# # Find all Occurence
# pattern = r"\d"
# text = "there are 6 guys and 0 ladies in our python class")

# # replace text
# pattern = r"\s+"
# text = "this is  a python class"
# sub = re.sub(pattern," ",text)
# print(sub)

# # matching patterns
# # match email address
# import re
# pattern = r"[a-zA-Z0-9_.-]+@[a-zA-z0-9.-]+\.[a-zA-Z]+"
# text = "my email is peteremmanuel@gmail.com"
# match = re.search(pattern,text)
# print(match.group())


# # Extarcting date
# text = "the event is on 2023-03-14, and the deadline is on 2025-05-09."
# pattern = r"\b\d{4}-\d{2}-\d{2}"
# matches = re.findall(pattern,text)
# print(matches)

# # validating input using regex
# import re
# phone_number = input("please enter your phone: ")
# pattern = r"^\(\+\d{3}\) \d{10}"
# if re.match(pattern,phone_number):
#     print("valid phone number")
# else:
#     print("invalid phone number")

# import re
# phone_number = "+234 803 456 7890"
# pattern = r"\+\d{3} \d{3} \d{3} \d{4}"
# matches = re.findall(pattern,phone_number)
# print(matches)


# pattern = r"\s+,\s*"
# text = "apple , banana, juice, mango"
# fruits = re.split(pattern,text)
# print("Fruits:",fruits)

# pattern = r"\s,\s"
# text = "apple, banana, juice , mango"
# fruits = re.split(pattern,text)
# print("Fruits:",fruits)

# pattern = r"\s*,\s*"
# text = "apple , banana, juice, mango,pineapple"
# fruits = re.split(pattern,text)
# print("Fruits:",fruits)

# # Using Groups and Capturing
# text = "Emails: misheal@gmail.com,stephen@google.com"
# pattern = r"(\w+)@(\w+\.[\w+]{2,4})"
# matches = re.findall(pattern,text)
# print(matches)

# for x,y in matches:
#     print("User: ",x)

# # Named Group
# text = "Contact: john.doe008@company.com"
# pattern = r"(?P<user>\w+\.*\w+)@(?P<domain>\w+.\w+)"
# match = re.search(pattern,text)
# if match:
#     print("User: ", match.group("user"))
#     print("Domain: ", match.group("domain"))
    

# # compilling regular expression
# text = "This is a text of regex patterns with four letter word."
# pattern = r"\b\w{4}"
# compilex = re.compile(pattern)
# matches = compilex.findall(text)
# print("Four letter words: ",matches)

# # compilling regular expression
# text = "This is a text of regex patterns with four letter word."
# pattern = r"\b\w{4}"
# compilex = re.compile(pattern)
# matches = compilex.search(text)
# print("Four letter words: ",matches.group())

# # Named Group
# text = "Contact: john.doe@company.com"

# import re
# text = "This  is  a test"
# pattern = r"\s+"
# new_test = re.sub(pattern," ",text)
# print("New text:",new_test)

# # Assignment 

# # String methods Vs regex
# # String methods adv
# #1. Simplicity
# #2. Performance
# #3. Readability

# # when to use regex
# #1.complex pattern
# #2.flexibility

# # multiple Operations
# # Use built-in methods for simple and common string operations where performance, readibility , and simplicity are key.
# # Use regex when dealing with complex string or when you need the flexibility to match, search, or manupulate strings based on inticate rules.
# # If a task can be accomplished using built-in methods without significant loss of class or performance,



# text = "abcdefghijklmnopqrstuvwxyz"
# # # upper_= text.upper()
# # print(upper_)
# new_list = " "
# for i in text:
#     new_list.append(i)
#     if i not in new_list and i in:
#         new_list.append(i)
        
    



# import time


# import time
# def traffic():
#     while True:
#         Lane1_cars = int(input("What is the number of cars for lane1: "))
#         Lane2_cars = int(input("What is the number of cars for Lane2: "))
#         Lane3_cars = int(input("What is the number of cars for lane3: "))
        
        
#         print(Lane1_cars)
#         print(Lane2_cars)
#         print(Lane3_cars)
        
    
#         if Lane1_cars > Lane2_cars and Lane1_cars > Lane3_cars:
#             print("Lane1_cars go first")
#             time.sleep(10)
#             if Lane2_cars>Lane3_cars:
#                 print("Lane2_cars get ready")
#                 time.sleep(6)
#                 print("Lane3_cars stop")
#             elif Lane3_cars>Lane2_cars:
#                 print("Lane3_cars get ready")
#                 time.sleep(6)
#                 print("Line2_cars stop")
            
#         if Lane2_cars > Lane1_cars and Lane2_cars > Lane3_cars:
#             print("Lane2_cars go first")
#             time.sleep(10)
#             if Lane1_cars>Lane3_cars:
#                 print("Lane1_cars get ready")
#                 time.sleep(10)
#                 print("Lane3_cars stop")
#             elif Lane3_cars>Lane1_cars:
#                 print("Lane3_cars get ready")
#                 time.sleep(6)
#                 print("Line1_cars stop")
    
#         if Lane3_cars > Lane2_cars and Lane3_cars > Lane1_cars:
#             print("Lane1_carsgo first")
#             time.sleep(10)
#             if Lane2_cars>Lane1_cars:
#                 print("Lane2_cars get ready")
#                 time.sleep(6)
#                 print("Lane1_cars stop")
#             elif Lane1_cars>Lane2_cars:
#                 print("Lane1_cars get ready")
#                 time.sleep(6)
#                 print("Line2_cars stop")
    


# # traffic()

# # GitHub



# # Create a Repository on GitHub:-
# #-Copy the repository URL
# # Clone the Repository
# # -open your terminal or command prompt

# # SQL

# # SQL- structured query language is used to manage and manupulate relational database, python with its extensive libraries, provides an easy way to interact with sql database
# # sqlite- is a lightweight, disk-based database that doesnt require a seperate server process. Python has built in support for sqlite with sqlite3

# import sqlite3

# # Creating a database or connecing to one if it exisits
# conn = sqlite3.connect("Item_7.db")

# # Creating a cursor object
# cursor = conn.cursor()

       




# #         print(line)

# # import re
# # def extract_data(file_path,email_file,phone_file):
# #     email_pattern = r"[a-zA-Z0-9_.+-]@[a-zA-Z0-9-.]+"
# #     phone_pattern = r"\+\d{1,2} \d{3} \d{3} \d{4}"

# #     with open(file_path,'r') as reviews_file, open(email_file,'w') as emails_file, open(phone_file,'w') as phones_file:
# #         for line in reviews_file:
# #             emails = re.findall(email_pattern, line)
# #             phones = re.findall(phone_pattern, line)

# #         print(emails)
# #         print(phones)

# # extract_data()
