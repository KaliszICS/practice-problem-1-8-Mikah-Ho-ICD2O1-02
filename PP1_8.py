'''
  Lesson: Boolean Logic
  Author: Mikah Ho
  Date Created: Sept 26, 2024
  Date Last Modified: Sept 28, 2024
'''

def q1():
  #Write Assignment code here
  bool1 = True
  bool2 = False
  print(bool1 and bool2)
  print(bool1 or bool2)

def q2():
  #Write Assignment code here
  integer = input("Enter an integer: ")
  print(int(integer) != 0)

def q3():
  #Write Assignment code here
  number = float(input("Enter a number: "))
  print(number >= 0 and number <= 10)

def q4():
  #Write Assignment code here
  food = input("Input food: ")
  drink = input("Input drink: ")
  print(food != "pizza" or drink != "pop")

def q5():
  #Write Assignment code here
  integer1 = input("Enter an integer: ")
  even = int(integer1) % 2 == 0
  print(f"The integer {integer1} is {even}.")

#Do not edit code after this
#Comment out the following code when running tests

# q1()
# q2()
# q3()
# q4()
# q5()
