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




     














   
    







   
    
    

    

