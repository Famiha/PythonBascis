import Cobra
import pydoc
from math import *
 print("Hello World")
# # Drawing A shape
print("|\ ")
print("| \ ")
print("|  \  ")
print("|   \ ")
print("`````")
#
      # VARIABLES
charecter_name = "Bob"
charecter_age = "35"

print("My name is ",charecter_name)
print("My age is", charecter_age)

    Strings with functions
 To make the variable upper-case/lower-case
phase = "Cool Girl"

print(phase.upper())
print(phase.lower())
print(phase.lower() + " is cool.")
# To count the Length
print(len(phase))
#  to call out a charecter
print(phase[8])
#  to call out either charecter or number
print(phase.index("C"))
# to replace smth
print(phase.replace("Cool", "Worst"))

        #   Numbers
# TO PRINT NUMBERS
num_1 = 5
print(2+ num_1 )
print(3+4)
print(3*(4+6))
# print(10 % 3)
# print(str(num_1)+ " Is my fav")
#
# #  Num functions
# my_num = -10
# # absolute value
# print(abs(my_num))
# # Power value
# print(pow(2,2))
# # Takes maximum value
# print(max(4,16))
# #  Takes minimum value
# print(min(4,16))
# # Rounds a number
# print(round(3.6))
# # Takes any number before decimal
# print(floor(32.45))
# #  Round as whole number no matter what
# print(ceil(3.1))
# # Root
# print(sqrt(4))
#
# name = input(str("Enter your name: "))
# print("HI", name)
# age = input("Enter your age: ")
# print("You re", age , "years old")
#
#
# # Calculator
# # num_1st = float(input("Enter a number: "))
# # num_2nd = float(input("Enter a number: "))
# # result = num_1st +  num_2nd
# # print(result)
#                #Mad lib#
# # color = str(input("Enter a color: "))
# # plural_noun = str(input("Enter a plural noun: "))
# # celebrity_name = str(input("Enter a celebrity name: "))
# # print("Roses are " + color)
# # print( plural_noun + " are blue")
# # print("I love " + celebrity_name)
#
#                  #List#
# # # List helps us with lots of datas
# friends = [ "Kevin", "Jim", "Pam", "Dwight" ,"Michael"]
# # #  colon means everything after including
# # print(friends[0:])
# # #  anything after colon works like a range
# # print(friends[0:4])
# # # change the value
# # friends[0] = "Creed"
# # print(friends[0])
# # #        List functions
# # lucky_numbers = [4, 6, 8, 2]
# # # to add list
# # friends.extend(lucky_numbers)
# # print(friends)
# # # to add a item
# friends.append("Kelly")
# print(friends)
# to add in between before the index of choice
# friends.insert(0,"Ryan")
# print(friends)
# # to remove a element
# friends.remove("Jim")
# print(friends)
# # to clear everything
# friends.clear()
# print(friends)
# to remove the last element from the list
# friends.pop()
# print(friends)
# # to check if soth is in the list
# print(friends.index('Dwight'))
# # to count how many times a items comes in the same list
# print(friends.count("Pam"))
# #  to sort in alphaberical order
# friends.sort()
# print(friends)
# #  to reverse the entire list
# friends.reverse()
# print(friends)
#  to copy the same list
# friends2 = friends.copy()
# print(friends2)
         # Tuples#
         # tuples are written with normal parenthesis
         # CONTAINER to store multiple pieces of info
# #It cant be changed at alllll like all the list functions
# coordinates = (4, 5)
# print(coordinates[-1])
#  functions : used for a specific task
# define and naming
# def say_hi(name, age ):
#     print('Hello ' + name + " .You are" + age + " years old.")
# # calling to execute
# say_hi("Mike"," 6")
#                   # Return statements
# #          Returns a specific statement or something you want
#
# def cube_num(num):
#     return num*num*num
# #  after return function no code gets executed
#
# # print(cube_num(3))
# result = cube_num(3)
# # storing in a variable
# print(result)
#
# #  if statements
# is_female = True
# is_tall = False
# # if is_female == True and is_tall == True:
  print("You are female")
 else:
    print("You are a male")
  print("Hallaleuh")
    print("YoU ARE A male >>>")

if is_female== True and is_tall== True:
    print("You are a female")
#  added if statements elif is the same
elif is_female and  is_tall:
    print('you are female and also tall')
elif is_female and not is_tall:
    print("You are female and short")
else:
    print('Man Power')

# ANother way to use if-statements
def big_num(num_1, num2, num3):
    if num_1 >= num2 and num_1 >= num3:
#         return num_1
#     elif num2 >= num_1 and num2>= num3:
#         return num2
#     else:
#         return num3
# print(big_num(3, 4 , 5))
# #  A little more advanced calculator
# num_1 = float(input("Enter your first number "))
# op = input("Enter your operator ")
# num_2 = float(input("Enter your first number "))
# if op == "+":
#     print(num_1 + num_2)
# elif op == "-":
#     print(num_1 - num_2)
# elif op == "*":
#     print(num_1 * num_2)
# elif op == "/":
#     print(num_1 / num_2)
# else:
#     print("Invalid operator")

#  Dictionaries in Python
#  kEY VALUE PAIRS
# monthConversions = {
#     "Jan" : "January",
#     "Feb" : "February",
#     0: "May",
# }
# print(monthConversions["Feb"])
# print(monthConversions["Jan"])
# print(monthConversions[0])
# # Default value if not in dictionary
# print(monthConversions.get("Dec"))
# print(monthConversions.get("Dec", "Not a valid key"))
#
#
# #  WHile Loops
# i = 1
# while i < 10:
#     print(i)
#     i += 1
#
# print('done with loop')
#
#
# # Guessing Game
# secret_word = "Girafee"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit :
#         guess = input("Enter your guess: ")
#         guess_count = guess_count + 1
#     else:
#          out_of_guesses = True
# if out_of_guesses:
#     print("You lose ")
# else:
#     print("you win")

           #For Loops
#
# for x in "Giraffe Academy":
#     print(x)
# friends = ["Jim" , "Pam", "Dwight" ]
# #  lens gives the number of the charecters in the list
# for x in range(len(friends)):
#     print(x)
#
# # for index in range(10):
# #     print(index)
# # #      doesnt include last num
# #
# # for index in range(3, 20):
# #     print(index)
#
# for index in range(5):
#     print(index)
#
#     #  exponents
# print(2**3)
# # exponent with functions
# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result * base_num
#     return result
#
# print(raise_to_power(2,2))
#
#
# number_grid = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]
# ]
# # print(number_grid[0][2])
# #               row  column
#
#
# #  nested for loops
# for row in number_grid:
#     for col in row:
#         print(col)


#  Basic translator

# Giraffe language

# def translate(phrase):
#     translation =""
#     for letter in phrase:
#         if letter in "AEIOUaeiou":
#             translation = translation + "g"
#         else:
#             translation = translation + letter
#     return translation
#
# print(translate(input("Enter a phrase : ")))
#                  COMMENTS IN A DIFFERENT WAY
'''
HELLO 
'''

# Try/ except block
#((Always except for a specific errors.))
# try:
#     answer = 10/0
#     number = int(input('Enter a number: '))
#     print(number)
# except  ZeroDivisionError as err:
#     print(err)
# except ValueError:
#     print('Invalid Input')

# Reading Files
# "r" means read
# "w" means write
# "a" means append add new info
# "r+" means read and write
# readine - read a line
# readlines - read line in a array can also use index
# can be used with a for loop :


# scratch_txt = open("Jim", "r")
# # print(scratch_txt.readable())
# print(scratch_txt.readlines())
#
## cancels all other text
# scratch_txt = open("Jim", "w")
# print(scratch_txt.write("Toby"))

# adds to the  text
# scratch_txt = open("Jim", "a")
# print(scratch_txt.write("\n Kelly - over ryan "))
#
# scratch_txt = open("Jim_1", "a")
# print(scratch_txt.write("\n Kelly - over ryan "))

#  opening a html file
# jim = open("index.html", "w")
# jim.write("<p>Hi I am speak Html And Css </p>")

#  Modules and Pip
# importing python file in a python file

# done on top
# print(Cobra.Hello)

#  Pip - to install manage update different modules

         #classes and objects
# classes
# defines whats a data is
# objects
#  actual representation
# from student import question_prompt
# student1 = student("Jim", "Business", 3.1, False)
# print(student1.is_on_probation)
# from student import question
# #  Multiple Choice Quiz
# question_prompts = [
#     "What is the color of apples?\n (a)Red (b)Blue\n"
# ]
# questions = [
#     question(question_prompts[0], "a")
# ]
# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompts)
#         if answer == question.answer:
#             score = score + 1
#     print("You got " , score, "/", len(questions), "correct")
# run_test(questions)
#
# from student import Student
# student_1 = Student("Jim", 3.6)
# student_2 = Student("Pam" , 3.1)
# print(student_2.on_honor_roll())


