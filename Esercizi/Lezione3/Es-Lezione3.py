#Marco Lombardi
#23/04/2024

#Exercise 4.1: Pizza
Pizza: list = ["Margherita", "Capricciosa", "Boscaiola"]
for pizza in Pizza:
    print(pizza)

#Exercise 4.2: Animals
Animals: list = ["Gatto", "Leone", "Ghepardo"]
for felino in Animals:
    print(felino)
for felino in Animals:
    if felino == "Gatto":
        print(f'Il {felino} è un felino e sarebbe un ottimo animale domestico per le famiglie.')
    elif felino == "Leone":
        print(f'Il {felino} è un felino e sarebbe un maestoso animale domestico per chi ha spazio aperto.')
    elif felino == "Ghepardo":
        print(f'Il {felino} è un felino e sarebbe un elegante animale domestico per chi ama la velocità.')
for felino in Animals:
    print(f'Il {felino} è un felino')


# Exercise 4.3: Counting to Twenty

for number in range(1, 21):
    print(number)

# Exercise 4.4: One Milion
numberlist: list = []
for number in range(1, 100000):
   numberlist.append(number)
print(numberlist)

#Exercise 4.5: Summing a Milion
numberlist: list = []
for number in range(1, 100000):
   numberlist.append(number)
print(min(numberlist))
print(max(numberlist))
print(sum(numberlist))

#Exercise 4.6: Odd Numbers

for odd in range(1, 21, 2):
    print(odd)

#Exercise 4.7: Threes
for three in range(0, 31, 3):
 print(three)

#Exercise 4.8: Cubes
cubelist: list = []
for number in range(0, 10):
   cubenumber: int = number**2
   cubelist.append(cubenumber)
print(cubelist)   

#Exercise 4.9: Cube Comprehension
cubecomprehension: list = [number**2 for number in range(0, 10)]
print(cubecomprehension)

#Exercise 4.10: Slices

es10list: list = ("Gatto", "Cane", "Gallina", "Margherita", "Boscaiola", "Uno", "Due", "Tre", "Quattro")

x = slice(0, 3)
y = slice(3, 6)
z = slice(6, 9)
print(es10list[x], es10list[y], es10list[z])

# Exercise 4.11: My Pizzas, Your Pizzas

pizzacopia: list = Pizza[:]

Pizza.append("Napoli")
pizzacopia.append("Bianca")
print(Pizza, pizzacopia)

for pizze in Pizza:
    print(f"Le mie pizze preferite sono {pizze}")
for pizze in pizzacopia:
    print(f"le pizze preferite del mio amico sono {pizze}")  

#Exercise 4.12: More Loops
#I understand this exercise

#Exercise 4.15: Code Review
#Rewrite Exercise: 4.10
es10list: list = ("Gatto", "Cane", "Gallina", 
                  "Margherita", "Boscaiola", "Uno", 
                  "Due", "Tre", "Quattro")

x = slice(0, 3)
y = slice(3, 6)
z = slice(6, 9)
print(es10list[x], es10list[y], es10list[z])

#Rewrite Exercise 4.2:

Animals: list = ["Gatto", "Leone", "Ghepardo"]
for felino in Animals:
    print(felino)
for felino in Animals:
    if felino == "Gatto":
        print(f'Il {felino} è un felino e sarebbe un ottimo 
              animale domestico per le famiglie.')
    elif felino == "Leone":
        print(f'Il {felino} è un felino e sarebbe un maestoso
               animale domestico per chi ha spazio aperto.')
    elif felino == "Ghepardo":
        print(f'Il {felino} è un felino e sarebbe un elegante 
              animale domestico per chi ama la velocità.')
for felino in Animals:
    print(f'Il {felino} è un felino') 

# Uncomplete Exercise

#Exercise 5.1: Test Conditional

# Define the car variable
car = 'subaru'

# Test 1: Is car == 'subaru'? I predict True.
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

# Test 2: Is car == 'audi'? I predict False.
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# Test 3: Is car != 'toyota'? I predict True.
print("\nIs car != 'toyota'? I predict True.")
print(car != 'toyota')

# Test 4: Is car.lower() == 'Subaru'? I predict True.
print("\nIs car.lower() == 'subaru'? I predict True.")
print(car.lower() == 'subaru')

# Test 5: Is car.upper() == 'SUBARU'? I predict True.
print("\nIs car.upper() == 'SUBARU'? I predict True.")
print(car.upper() == 'SUBARU')

# Test 6: Is len(car) == 6? I predict True.
print("\nIs len(car) == 6? I predict True.")
print(len(car) == 6)

# Test 7: Is car.startswith('su')? I predict True.
print("\nIs car.startswith('su')? I predict True.")
print(car.startswith('su'))

# Test 8: Is car.endswith('ru')? I predict True.
print("\nIs car.endswith('ru')? I predict True.")
print(car.endswith('ru'))

# Test 9: Is 'b' in car? I predict True.
print("\nIs 'b' in car? I predict True.")
print('b' in car)

# Test 10: Is 'x' in car? I predict False.
print("\nIs 'x' in car? I predict False.")
print('x' in car)

#Exercise 5.2: More Conditional Test

# Define variables for testing
string1 = "hello"
string2 = "HELLO"
number1 = 10
number2 = 20
list1 = [1, 2, 3, 4, 5]

# Tests for equality and inequality with strings
print("Tests for equality and inequality with strings:")
print("Is string1 == 'hello'? I predict True.")
print(string1 == 'hello')

print("\nIs string1 != string2? I predict True.")
print(string1 != string2)

# Tests using the lower() method
print("\nTests using the lower() method:")
print("Is string1.lower() == 'hello'? I predict True.")
print(string1.lower() == 'hello')

# Numerical tests
print("\nNumerical tests:")
print("Is number1 == 10? I predict True.")
print(number1 == 10)

print("Is number1 > number2? I predict False.")
print(number1 > number2)

print("Is number2 >= 20? I predict True.")
print(number2 >= 20)

print("Is number2 < 15? I predict False.")
print(number2 < 15)

# Tests using the 'and' keyword and the 'or' keyword
print("\nTests using the 'and' keyword and the 'or' keyword:")
print("Is number1 == 10 and number2 == 20? I predict True.")
print(number1 == 10 and number2 == 20)

print("Is number1 == 5 or number2 == 15? I predict False.")
print(number1 == 5 or number2 == 15)

# Test whether an item is in a list
print("\nTest whether an item is in a list:")
print("Is 3 in list1? I predict True.")
print(3 in list1)

# Test whether an item is not in a list
print("\nTest whether an item is not in a list:")
print("Is 6 not in list1? I predict True.")
print(6 not in list1)

#Exercise 5.3: Alien Colors #1

# Version that passes the if test
alien_color = 'green'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points.")

# Version that fails the if test
alien_color = 'red'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points.")

# Exercise 5.4: Alien Colors #2

# Version that runs the if block
alien_color = 'green'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points for shooting the alien.")
else:
    print("Congratulations! You just earned 10 points.")

# Version that runs the else block
alien_color = 'red'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points for shooting the alien.")
else:
    print("Congratulations! You just earned 10 points.")

# Exercise 5.5 Alien Colors #3

# Version for a green alien
alien_color = 'green'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points.")
elif alien_color == 'yellow':
    print("Congratulations! You just earned 10 points.")
else:
    print("Congratulations! You just earned 15 points.")

# Version for a yellow alien
alien_color = 'yellow'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points.")
elif alien_color == 'yellow':
    print("Congratulations! You just earned 10 points.")
else:
    print("Congratulations! You just earned 15 points.")

# Version for a red alien
alien_color = 'red'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points.")
elif alien_color == 'yellow':
    print("Congratulations! You just earned 10 points.")
else:
    print("Congratulations! You just earned 15 points.")

#Exercise: 5.6 Stages of life

age = 30

if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")

#Exercise: 5.7 Favorite Fruits

# Define the list of favorite fruits
favorite_fruits = ['apple', 'banana', 'strawberry']

# Check if 'apple' is in the list of favorite fruits
if 'apple' in favorite_fruits:
    print("You really like Apples!")

# Check if 'banana' is in the list of favorite fruits
if 'banana' in favorite_fruits:
    print("You really like Bananas!")

# Check if 'orange' is in the list of favorite fruits
if 'orange' in favorite_fruits:
    print("You really like Oranges!")

# Check if 'strawberry' is in the list of favorite fruits
if 'strawberry' in favorite_fruits:
    print("You really like Strawberries!")

# Check if 'kiwi' is in the list of favorite fruits
if 'kiwi' in favorite_fruits:
    print("You really like Kiwis!")

#Exercise 5.8: Hello Admin

usernames = ['admin', 'jaden', 'emma', 'michael', 'olivia']

# Loop through the list of usernames and print greetings
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")

#Exercise 5.9: No Admin 
#I Understand this Exercise

#Exercise 5.10: Checking Username
# Define the list of current users
current_users = ['John', 'Jane', 'Emma', 'Michael', 'Olivia']

# Define the list of new users
new_users = ['Emily', 'Jason', 'Jane', 'Liam', 'Olivia']

# Convert current_users to lowercase for case-insensitive comparison
current_users_lower = [user.lower() for user in current_users]

# Loop through the new_users list
for new_user in new_users:
    # Convert the new username to lowercase for case-insensitive comparison
    new_user_lower = new_user.lower()
    
    # Check if the new username has already been used
    if new_user_lower in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"The username '{new_user}' is available.")

# Exercise 5.11: Ordinal Numbers
# Store the numbers 1 through 9 in a list
numbers = list(range(1, 10))

# Loop through the list
for number in numbers:
    # Check the last digit of the number to determine the ordinal ending
    if number % 10 == 1:
        ordinal = "st"
    elif number % 10 == 2:
        ordinal = "nd"
    elif number % 10 == 3:
        ordinal = "rd"
    else:
        ordinal = "th"
    
    # Print the number with its proper ordinal ending
    print(f"{number}{ordinal}")        










     














   
    







   
    
    

    

