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

guest: list = ["Gino", "Mimmo", "Luigi", "Alberto", "Laura", "Erica",]    

for word in guest:
    print(f'Ciao {word} ti va di venire a mangiare una pizza a casa mia')

#Exercise 3.5

guest.copy
guest.remove("Luigi")
guest.append("Maria")
for word in guest:
    print(f'Ciao {word} ti va di venire a mangiare una pizza a casa mia')
    
#Exercise 3.6

for word in guest:
    print(f'Ciao {word} ho trovato un tavolo piu grande')
guest.insert(0,"Tiziana")
guest.insert(4, "Carlo")
guest.append("Giulia")
for word in guest:
 print(f'Ciao {word} ho trovato un tavolo piu grande')

# Exercise 3.7

print("Posso invitare solo 2 persone")


print(f'ciao {guest.pop(0)} mi dispiace non posso invitarti')
print(f'ciao {guest.pop(1)} mi dispiace non posso invitarti')
print(f'ciao {guest.pop(2)} mi dispiace non posso invitarti')
print(f'ciao {guest.pop(3)} mi dispiace non posso invitarti')
print(f'ciao {guest.pop(4)} mi dispiace non posso invitarti')
print(f'ciao {guest.pop(0)} mi dispiace non posso invitarti')
print(f'ciao {guest.pop(1)} mi dispiace non posso invitarti')
print(f'ciao {guest.pop(0)} sei ancora invitato')
print(f'ciao {guest.pop(0)} sei ancora invitato')
print(guest)

# Exercise 3.8

World: list = ["Germiana", "Francia", "Norvegia", "Finlandia", "Svezia"]
print(sorted(World))
print(World)
print(sorted(World))
print(World)
World.reverse()
print(World)
World.reverse()
print(World)
World.sort()
print(World)
World.sort()
print(World)

#Exercise 3.9

names: list =["Gino", "Mimmo", "Luigi", "Alberto", "Laura", "Erica"]
print(len(name))

#Exercise 3.10

city: list = ["Roma", "Milano", "Napoli", "Torino", "Palermo", "Genova"]
print(city)
print(sorted(city))
print(len(city))

#Exercise 6.1

Person: dict = {"Nome": "Marco", "Cognome": "Lombardi", "Età": 23, "Città": "Zagarolo"}
print(Person)

#Exercise 6.2

favourite: dict = {
    'Marco': 7,
    'Anna': 15,
    'Luca': 3,
    'Sara': 22,
    'Giovanni': 10
}

for persona, numero in favourite.items():
    print(f"{persona} ha il numero preferito {numero}.")
    
#Exercise 6.3

glossario = {
    'variabile': 'Un nome che fa riferimento a un valore.',
    'funzione': 'Un blocco di codice riutilizzabile.',
    'lista': 'Una collezione di elementi ordinati.',
    'dizionario': 'Una collezione di coppie chiave-valore.',
    'loop': 'Un modo per eseguire lo stesso blocco di codice più volte.'
}

for parola, significato in glossario.items():
    print(f"{parola}: {significato}\n")

#Exercise 6.7

persona1 = {
    'nome': 'Marco',
    'cognome': 'Rossi',
    'età': 30,
    'città': 'Roma'
}

persona2 = {
    'nome': 'Anna',
    'cognome': 'Bianchi',
    'età': 25,
    'città': 'Milano'
}

persona3 = {
    'nome': 'Luca',
    'cognome': 'Verdi',
    'età': 35,
    'città': 'Napoli'
}

persone = [persona1, persona2, persona3]

for persona in persone:
    print(f"Nome: {persona['nome']}")
    print(f"Cognome: {persona['cognome']}")
    print(f"Età: {persona['età']}")
    print(f"Città: {persona['città']}\n")

#Exercise 6.8

animale1 = {
    'specie': 'Cane',
    'proprietario': 'Marco'
}

animale2 = {
    'specie': 'Gatto',
    'proprietario': 'Anna'
}

animale3 = {
    'specie': 'Pappagallo',
    'proprietario': 'Luca'
}

animali_domestici = [animale1, animale2, animale3]

for animale in animali_domestici:
    print(f"Specie: {animale['specie']}")
    print(f"Proprietario: {animale['proprietario']}\n")


















