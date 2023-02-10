# name = input("what is your name? ")
# fav_color = input("what is your fav color?")
# print(name + ' likes ' + fav_color)


# user_weight = input('enter your weight in pounds: ')
# weight_convert = int(user_weight) * 0.45
# weight_in_kilo = weight_convert
# print(weight_in_kilo)

#
# age = input("input present year:  ")
# brith_year = int(age)- 1996
# print(brith_year)

# course = '''Hi john,
# here is our email
# thank you'''

# is_hot = False
# is_cold = False
# if is_hot:
#     print("it is a hot day")
# elif is_cold:
#     print("its a cold day, wear warm clothes")
# else:
#     print("enjoy your day")

#
# is_goodscore = True
# is_badscore = False
#
# if is_goodscore:
#     print("you need to pay 10% down payment")
# elif is_badscore:
#     print("you need to pay 20% down payment")
# else:
#     print("")

# A program that prints the numbers from 1 to 100, but for multiples of three, it should print "Fizz"
# instead of the number, and for multiples of five it should print "Buzz". For numbers which are
# multiples of both three and five, it should print "FizzBuzz".
# for num in range(0,101):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz: "+str(num))
#     elif num % 3 == 0:
#         print("Fizz:" +str(num))
#     elif num % 5 == 0:
#         print("Buzz:" +str(num))
#     else:
#         print(num)


# program to print the numbers from 1 to n, where n is an integer entered by a user,
# but for multiples of three, it should print "Fizz" instead of the number, and for
# multiples of five it should print "Buzz". For numbers which are multiples of both
# three and five, it should print "FizzBuzz".
# number = input('Enter number')
# for number in range(0, int(number)):
#     if number % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz: "+str(num))
#     elif number % 3 == 0:
#         print("Fizz:" +str(num))
#     elif number % 5 == 0:
#         print("Buzz:" +str(num))
#     else:
#         print(number)


# price_of_house = 1000000
# buyer_credits_good = False
# buyer_credit_bad = True
# if buyer_credits_good:
#     down_payment= price_of_house * 0.1
#     print(f"down payment : N{down_payment}");
# elif buyer_credit_bad:
#     down_payment = price_of_house * 0.2
#     print(f"down payment : N{down_payment}");


# name_char_length = "ibr"
# if len(name_char_length)> 50:
#     print("name must not be more than 50 char!")
# elif len(name_char_length) < 3:
#     print("name must be 3 char long ")
# else:
#     print("name looks good!")

# weight = int(input("enter your weight: "))
# unit = input("kg or Pds: ")
#
# if unit.upper() == "KG":
#     print(f"weight in kg is:{weight * 0.45}")
# elif unit.upper() == "PDS":
#     print(f"weight in Pds is:{weight // 0.45 }")

#

command = ""


# while True:
#     command = input("> ").lower()
#     if command == "start":
#         print("Start the car...")
#     elif command == "stop":
#         print("car stopped...")
#     elif command == "help":
#         print("""
#     start- to start the car
#     stop- to stop the car
#     quit- to quit
#     """)
#     elif command == "quit":
#          break
# else:
#     print("i don't understand the command")

# prices = [10, 40, 60, 30]
# total = 0
# for price in prices:
#     total += price
# print(total)

# numbers = [2,2,2,2,5,5]
# for x in numbers:
#     print('*' * x)

# numbers = [5,6,7,8,9,20]
# max_numb= numbers[0]
# for number in numbers:
#     if number > max_numb:
#         max_numb = number
# print(max_numb)


# program to calculate user's age in second
# try:
#     dob = int(input(("enter your date of birth in years: ")))
#     present_year = 2023
#     age_years = present_year - dob
#     # to convert age to days
#     age_days = age_years * 365
#
#     # to convert age to hours
#     age_hours = age_days * 24
#
#     # to convert age to mins
#     age_mins = age_hours * 60
#
#     # to convert age to seconds
#     age_seconds = age_mins * 60
#     print(f"You're {age_years} years old")
#     print(f"You're {age_days} days")
#     print(f"You're {age_mins} mins")
#     print(f"You're {age_seconds} seconds")
# except ValueError:
#     print("invalid value, please enter in digits")

#
#
#
#
#  Program to know the country users has visited by their inputs
# print("Welcome to the countries app.")
# print("You have visited 0 countries so far.")
# add = "a"
# list_county = "l"
# quit_country = "q"
# country_visited = []
# user_input = input("Enter 'a' to add a country you've visited, 'l' to list country visited or 'q' to quit: ")
# while user_input != "q":
#     add_c = input("'a' to add a country you've visited, 'l' to list country visited or 'q' to quit: ")
#     if add_c == "a":
#        user_country_input = input("Enter country you've visited: ")
#        country_visited.append(user_country_input)
#     if add_c == "l":
#         print(country_visited)
#     elif add_c == "q":
#         quit()


# Function to print out emoji output
# def emoji_word_output(message):
#     words = message.split(" ")
#     emojis = {
#         ":)": "😁",
#         ":(": "😒"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output
#
# message = input(">")
# print(emoji_word_output(message))

class Mammal:
    def walk(self):
        print("walk")


# class Dog(Mammal):
#     def bark(self):
#         print("bark")
#     pass
#
#
# class Cat(Mammal):
#     def be_annoying(self):
#         print("be annoying")
#     pass
#
#
# dog1= Dog()
# dog1.bark()
#
# cat1 = Cat()
# cat1.be_annoying()


# def sayhi(name, age):
#     return (f"hello {name}, you're {age} ")
#
#
# print(sayhi("ibrahim", 27))
# sayhi("Akorede", 15)

# Write a program that prompts the user to enter the size of the hard drive specified
# by the manufacturer, on the hard drive box, and outputs the actual storage
# capacity of the hard drive.

# hard_drive_size = int(input("enter the size of the hard drive specified by the manufacturer in gb: "))
# computer_default = 37.25
# actual_hddsize = (hard_drive_size * computer_default) / 40
# print(actual_hddsize)


# # Write a program that does the get milk factory profits
# total_amount_milk = int(input("enter the total of milk produced in the morning: "))
#
# carton_milkInLiters = 3.78
# productionCostInLiters = 250
# profitInLiters = 180
# milk_cartons = carton_milkInLiters * total_amount_milk
# print(f"{milk_cartons.__round__()} number of milk cartons needed to hold milk.")
# cost_of_production = productionCostInLiters * total_amount_milk
# print(f"{cost_of_production} cost of producing milk.")
# profits = profitInLiters * total_amount_milk
# print(f"{profits} the profits made")

# puzzle = [
# ['P','G','T','H','S','S','M','A','L','L','F','O','R','W','A','R','D','J'],
# ['U','N','T','T','O','N','H','E','I','R','N','B','T','M','V','E','E','W'],
# ['Y','I','D','R','H','O','O','N','G','C','E','U','E','T','I','R','S','O'],
# ['A','S','R','O','U','R','P','I','O','N','O','B','S','N','S','R','L','R'],
# ['L','S','A','U','P','O','E','A','T','E','I','C','O','E','C','O','A','H'],
# ['R','A','U','T','O','R','C','E','M','U','O','L','Y','U','O','H','M','T'],
# ['E','P','G','O','I','H','O','I','P','R','T','F','B','G','N','D','D','E'],
# ['Y','B','G','F','N','R','T','V','E','O','A','I','N','B','R','D','U','E'],
# ['A','T','N','B','T','S','E','B','E','S','I','I','T','A','I','M','N','R'],
# ['L','S','I','O','S','K','O','T','N','R','L','N','W','S','A','R','K','F'],
# ['P','I','T','U','E','A','T','E','R','E','T','R','T','E','B','B','D','S'],
# ['B','S','O','N','R','A','A','T','V','A','O','I','T','E','L','U','H','L'],
# ['L','S','O','D','W','K','E','A','A','F','U','S','M','J','R','O','S','A'],
# ['O','A','H','S','E','K','R','F','R','M','E','Q','R','E','T','N','E','C'],
# ['C','L','S','R','S','T','O','E','B','A','C','K','B','O','A','R','D','S'],
# ['K','L','S','A','N','U','W','G','A','M','E','M','I','T','F','L','A','H'],
# ['A','A','B','C','L','O','C','K','I','R','E','F','E','R','E','E','S','M'],
# ['I','B','T','H','P','T','E','N','D','R','A','U','G','T','N','I','O','P'],
# ]
#
# words= str(input("Enter the word to search for in UPPERCASE: "))
# def capitalize_word_in_crossword(puzzle, words):
#     for rownum, row in enumerate(puzzle):
#         for word in words:
#             find_index=''.join(row).lower().find(word)
#             if find_index>0:
#                 for i in range(find_index, len(word)+1):
#                     puzzle[rownum][i]=puzzle[rownum][i].upper()
#
#     for colindex in range(len(puzzle[0])):
#         for word in words:
#             puzzle=[row[colindex] for row in puzzle]
#             find_index=''.join(colvalues).lower().find(word)
#             if find_index>0:
#                 for i in range(find_index, len(word)+1):
#                     puzzle[i][colindex]=puzzle[i][colindex].upper()
#     return puzzle
# print("Input: "+str(puzzle))
# print("Output: "+str(capitalize_word_in_crossword(puzzle, words)))

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(max(thislist))
print(thislist)
