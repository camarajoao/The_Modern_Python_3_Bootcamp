# #Write a function called product that accepts two parameters and returns the product of the two parameters (multiply them together)
# def product(x,y):
#     return x * y

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# #Write a function called return_day. this function takes in one parameter (a number from 1-7) and returns the day of the week (1 is Sunday, 2 is Monday, 3 is Tuesday etc.).
# #If the number is less than 1 or greater than 7, the function should return None
# days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
# keys = list(range(1,len(days_of_week) + 1))
# week = dict(zip(keys, days_of_week))
# def return_day(num):
#     if num in week:
#         return week[num]
#     return None

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# #Write a function called last_element. This function takes in one parameter (a list) and returns the last value in the list. It should return None if the list is empty.
# def last_element(x):
#     if x != []:
#         return x[len(x)-1]
#     return None

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# #Write a function called number_compare. This function takes in two parameters (both numbers).
# #If the first is greater than the second, this function returns "First is greater" If the second number is greater than the first, the function returns "Second is greater" Otherwise the function returns "Numbers are equal"
# def number_compare(x, y):
#     if x &gt; y:
#         return  "First is greater"
#     elif y &gt; x:
#         return "Second is greater"
#     else:
#         return "Numbers are equal"

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# #Write a function called single_letter_count. This function takes in two parameters (two strings). The first parameter should be a word and the second should be a letter.
# #The function returns the number of times that letter appears in the word. The function should be case insensitive (does not matter if the input is lowercase or uppercase).
# #If the letter is not found in the word, the function should return 0.
# def single_letter_count(x, y):
#     count = x.lower().count(y.lower())
#     return count
# print(single_letter_count("Hello World", "y"))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Write a function called multiple_letter_count. This function takes in one parameter (a string) and returns a dictionary with the keys being the letters and the values being the count of the letter.
# def multiple_letter_count(x):
#     count = {}
#     newString = x.replace(" ", "")
#     for char in newString.lower():
#         if char in count:
#             count[char]+=1
#         else:
#             count[char]=1
#     return count
# print(multiple_letter_count('hello world'))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# #Write a function called list_manipulation. This function should take in four parameters (a list, command, location and value).
# #If the command is "remove" and the location is "end", the function should remove the last value in the list and return the value removed
# #If the command is "remove" and the location is "beginning", the function should remove the first value in the list and return the value removed
# #If the command is "add" and the location is "beginning", the function should add the value (fourth parameter) to the beginning of the list and return the list
# #If the command is "add" and the location is "end", the function should add the value (fourth parameter) to the end of the list and return the list
# def list_manipulation(collection, command, location, value=None):
#     if command == "remove" and location == "end":
#         value = collection.pop()
#         return value
#     elif command == "remove" and location == "beginning":
#         value = collection.pop(0)
#         return value
#     elif command == "add" and location == "beginning":
#         collection.insert(0, value)
#         return collection
#     elif command == "add" and location == "end":
#         collection.append(value)
#         return collection
#     else:
#         return "Error"
# print(list_manipulation([1,2,3], 'add', 'end', 4))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# #Write a function called is_palindrome. A Palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward.
# #This function should take in one parameter and returns True or False depending on whether it is a palindrome. As a bonus, allow your function to ignore whitespace and capitalization so that is_palindrome('a man a plan a canal Panama') returns True.
# def is_palindrome(x):
#     newString = x.replace(" ", "").lower()
#     if newString == newString[::-1]:
#         return True
#     else:
#         return False
# print(is_palindrome('a man a plan a canal Panama'))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Write a function called frequency. This function accepts a list and a search_term (this will always be a primitive value) and returns the number of times the search_term appears in the list.
# def frequency(collection, searchTerm):
#     count = 0
#     for item in collection:
#         if searchTerm == item:
#             count += 1
#     return count
# print(frequency([1, 2, 3, 4, 4, 4], 4))

# #alternate solution
# def frequency(collection, searchTerm):
#     return collection.count(searchTerm)
# print(frequency([1, 2, 3, 4, 4, 4], 4))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Write a function called multiply_even_numbers. This function accepts a list of numbers and returns the product of all even numbers in the list.
# def multiply_even_numbers(collection):
#     total = 1
#     for num in collection:
#         if num % 2 == 0:
#             total = total * num
#     return total
# print(multiply_even_numbers([2,3,4,5,6]))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Write a function called capitalize. This function accepts a string and returns the same string with the first letter capitalized.  You may want to use slices to help you out.
# def capitalize(x):
#     firstLetter = x[0].upper()
#     restString = x[1:]
#     newString = f"{firstLetter}{restString}"
#     return newString
# print(capitalize("jamaica"))

# # alternate solution
# def capitalize(x):
#     return x[:1].upper() + x[1:]
# print(capitalize("jamaica"))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# #Write a function called compact. This function accepts a list and returns a list of values that are truthy values, without any of the falsey values.
# def compact(l):
#     return [val for val in l if val]
# print(compact([0,1,2,"",[], False, {}, None, "All done"]))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Write a function called intersection. This function should accept two lists and return a list with the values that are in both input lists.
# def intersection(listOne, listTwo):
#     return [value for value in set(listOne) & set(listTwo)]
# print(intersection([1,2,3], [2,3,4]))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Write a function called partition. This function accepts a list and a callback function (which you can assume returns True or False).
# # The function should iterate over each element in the list and invoke the callback function at each iteration.
# # If the result of the callback function is True , the element should go into the first list (i.e. the "truthy" list).
# # If the result of the callback function is False , the element should go into the second list (i.e. the "falsy" list).
# def partition(lst, fn):
#     return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]