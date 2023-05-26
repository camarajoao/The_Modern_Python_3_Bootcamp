# dictionaries are the same as objects in javascript
# artist = {
#     "first": "Neil",
#     "last": "Young",
# }
# full_name = artist['first'] + " " + artist['last']
# # full_name = f"{artist['first']} {artist['last']}" alternative
# print(full_name)

# for value in artist.values():
#     print(value)
# for key in artist.keys():
#     print(key)
# for item in artist.items():
#     print(item)

# donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# total_donations = 0
# for value in donations.values():
#     total_donations += value
# print(total_donations)


# bakery_stock = {
#     "almond croissant" : 12,
#     "toffee cookie": 3,
#     "morning bun": 1,
#     "chocolate chunk cookie": 9,
#     "tea cake": 25
# }
# food = "almond croissant"
# if food in bakery_stock:
#     print(f"{bakery_stock[food]} left")
# else:
#     print("We don't make that")


# game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"]
# initial_game_state = dict.fromkeys(game_properties, 0)
# print(initial_game_state)


# inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}
# stock_list = inventory.copy()
# stock_list.update({'cookie': 18})
# stock_list.pop('cake')
# print(stock_list)


# songs = [
#     {'title': 'song1', 'artist': 'artist1', 'duration': 2.5},
#     {'title': 'song2', 'artist': 'artist2', 'duration': 4},
#     {'title': 'song3', 'artist': 'artist3', 'duration': 3.5}
# ]
# for song in songs:
#     print(song['duration'])

# shorter = [song['duration'] for song in songs if song['duration'] < 3]
# print(shorter)


# newDict = {num: num**2 for num in [1,2,3,4,5]}
# print(newDict)

# person = {
#     'name': 'joao',
#     'city': 'vancouver',
#     'team': 'flamengo'
# }

# yellying_person = {k.upper(): v.upper() for k,v in person.items()}
# print(yellying_person)


# numDict = {num:('even' if num % 2 == 0 else 'odd') for num in range(1, 11)}
# print(numDict)


# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]

# # make sure your solution is assigned to the answer variable so the tests can work!
# answer = {list1[i]: list2[i] for i in range(0,3)}
# print(answer)


# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
# answer = {person[i][0]: person[i][1] for i in range(0,3)}
# answer = dict(person) #alternate solution
# print(answer)

# answer = dict.fromkeys("aeiou", 0)
# print(answer)


# answer = {count: chr(count) for count in range(65, 91)}
# print(answer)

# sets
# math_students = {'Matthew', 'Helen', 'Prashant', 'James', 'Aparna'}
# biology_students = {'Jane', 'Matthew', 'Charlotte', 'Mesut', 'Oliver', 'James'}

# union - will return the names of students without repeating them
# print(math_students | biology_students)
# {'Oliver', 'Matthew', 'James', 'Aparna', 'Prashant', 'Charlotte', 'Jane', 'Helen', 'Mesut'}

# intersection - will return the names of students who are on both lists
# print(math_students & biology_students)
# {'James', 'Matthew'}


# numbers = (1, 2, 3, 4)
# print(type(numbers))

# value = (1,)
# print(type(value))

# values = [10, 20, 30]
# static_values = tuple(values)
# print(static_values)


# stuff = [1,3,1,5,2,5,1,2,5]
# unique_stuff = set(stuff)
# print(unique_stuff)
