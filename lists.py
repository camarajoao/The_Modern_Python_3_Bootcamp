# list = [1,2,3,4,5]
# print(len(list))
# listTwo = list(range(1,6))
# print(listTwo) #[1, 2, 3, 4, 5]
# print(len(listTwo)) #5
# print(listTwo[-1]) #5
# print(listTwo[0]) #1

# list.append(6)
# print(list) #[1,2,3,4,5,6]

# list.extend([7,8,9])
# print(list) #[1,2,3,4,5,6,7,8,9]

# list.insert(0, 0) #insert takes 2 arguments. the first argument is the index which you want to insert the second argument.
# print(list)

# list.insert(len(list), 10)
# print(list)

# list.remove(2) #remove the first instance of the item passed as argument

# list.pop() #remove last item of list
# print(list)

# list.pop(1) #remove the item which index is passed as argument
# print(list)

# list.clear() #remove all items from list
# print(list)

# sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# result = ""
# for sound in sounds:
#     result += sound.upper()
# print(result)

# names = ['joao', 'thais', 'joao', 'tom']
# print(names.count('joao')) #will count the number of times 'joao' appears in the list

# names.reverse() #reverse the order of the list
# print(names)

# words = ['Coding', 'is', 'fun']
# print(' '.join(words)) #returns Coding is fun

#slice method
# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
# print(colors[3:]) #will return ['green', 'blue', 'indigo', 'violet'] 
# print(colors[:3]) #will return ['red', 'orange', 'yellow']
# print(colors[1:3]) #will return ['orange', 'yellow']
# print(colors[1::2]) #will return ['orange', 'green', 'indigo']

# friends = ['ross', 'rachel', 'phoebe', 'monica', 'chandler', 'joey']
# friends.sort() #['chandler', 'joey', 'monica', 'phoebe', 'rachel', 'ross']
# print([friend[0].upper() + friend[1:] for friend in friends]) #['Chandler', 'Joey', 'Monica', 'Phoebe', 'Rachel', 'Ross']

# numbers = [1,2,3,4,5]
# doubled_numbers = [num * 2 for num in numbers] #[2, 4, 6, 8, 10]
# print(doubled_numbers)

# answer = [name[0] for name in ["Elie", "Tim", "Matt"]]
# print(answer)
# answer2 = [num for num in [1,2,3,4,5,6] if num % 2 == 0]
# print(answer2)

# answer3 = [name[::-1].lower() for name in ["Elie", "Tim", "Matt"]]
# print(answer3)

# answer4 = [value for value in [1,2,3,4] if value in [3,4,5,6]]
# print(answer4)

# answer5 = [num for num in range(1,101) if num%12 == 0]
# print(answer5)

# answer6 = [char for char in 'amazing' if char not in 'aeiou']
# print(answer6)

# answer7 = [[num for num in range(0,3)] for num in range(0,3)]
# print(answer7)

# answer8 = [[num for num in range(0,10)] for i in range(0,10)]
# print(answer8)