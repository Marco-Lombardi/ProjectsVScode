# Marco Lombardi
# 18/04/2024

print("Hello World!")

# Exercise 2.3

#This variable contains a name

name: str = "Mario"

message: str = f"Ciao {name} ti va di imparare un po di python insieme"

print(message)

#Exercise 2.4 

name: str = "Mario"

# This variable print a name in lowercase

name_lower: str = name.lower()

# This variable print a name in uppercase
name_upper: str = name.upper()

print(f"{name}, {name_upper}, {name_lower},")

#Exercise 2.5

print("Albert Einstein once said, \"A Person who never made a mistake never tried anything new\"")

#Exercise 2.6

name_famous: str = "Albert Einstein"

phrase: str = f"{name_famous} once said, \"A Person who never made a mistake never tried anything new\""

#Exercise 2.8

filename: str = "python_notes.txt"

print(filename.removesuffix(".txt"))

#Exercise 3.1
names: list =["Gino", "Mimmo", "Luigi", "Alberto", "Laura", "Erica"]

for word in names:
    print(f'{word}')

#Exercise 3.2

names: list =["Gino", "Mimmo", "Luigi", "Alberto", "Laura", "Erica"]

for word in names:
    print(f'Ciao {word} come stai?')

#Exercise 3.3

car: list = ["Maserati", "Lamborghini", "Ferrari", "Rolls Royce"]

for vehicle in car:
    print(f'I would like to own a {vehicle} car.')

#Exercise 3.4    

name: list = ["Gino", "Mimmo", "Luigi", "Alberto", "Laura", "Erica",]    

for word in name:
    print(f'Ciao {word} ti va di venire a mangiare una pizza a casa mia')










