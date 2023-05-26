# # function to print in python is print(). You run the command python + the name of the file to run the file in the cmd
# print("Hello")

# #to interpolate (number variable inside string), add f before the string and variable inside {}
# guess = 8
# print(f"your guess of {guess} was incorrect!")

# decimal = 12.5
# integer = int(decimal) #int() will convert a decimal to an integer integer -- int(decimal) = 12
# num = 12
# num = float(num) #float() will convert an integer into a float -- float(num) = 12.0

# my_list = [1, 2, 3]
# my_list_as_a_string = str(my_list) #str() will convert numbers to strings

# name = "Joao"
# print(name[0]) #will print "J"
# print(name[-1]) #will print the last letter

# #mileage converter
# print("How many kilometers did you cycle today")
# kms = input()
# miles = float(kms)/1.60934
# print(f"That is equal to {round(miles, 2)} miles")

# #input() function prompts the user to enter an input and stores the result to a variable
# name = input("Enter your name here:")
# print(f"Welcome back {name}")

# #important things to remember.
# #1 - the string MUST be equal to the conditional string, including capital letter and space.
# #2 - elif is the python version of else if in javascript
# #3 - indentation matters in if statements. The action must be indented
# #4 - the colon after the if statement MUST be used so Python understands there is a return on the next line
# name = "Arya Stark"
# if name == "Arya Stark":
#     print("Valar Morghulis")
# elif name == "Jon Snow":
#     print("You know nothing")
# else:
#     print("Carry on")

# #Even or odd
# print("Pick a number")
# num = input()
# if (int(num) % 2 == 0):
#     print('You picked an even number')
# else:
#     print('You picked an odd number')

#logical Operators
# and === && in javascript
#if a and b:
#   print(c)

# or === || in javascript
#if am_tired or is_bedtime:
#   print("go to sleep")

# not === ! in javascript
#if not is_weekend:
#   print("go to work")

# is vs ==
# a = [1, 2, 3]
# b = [1, 2, 3]
# a == b -- true because they have the same values
# a is b -- false because they are 2 different lists

#ask for age
def program():
    age = input("How old are you: ")
    if age == "":
        print('invalid')
        program()
    else:
        age = int(age)
        #between 18 and 21
        if age >= 18 and age < 21:
            print("You can enter, but need a wristband!")
        elif age >= 21:
            print("You are good to enter and can drink!")
        else:
            print("You can't enter!")

program()

