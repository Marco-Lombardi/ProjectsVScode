# Marco Lombardi
# 02-05-2024

# Exercise 1
# Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.

def frequency_dict(elements: list) -> dict:
      frequencies = {}
      for element in elements:
        if element in frequencies:
            frequencies[element] += 1
        else:
            frequencies[element] = 1
      return frequencies
    
print(frequency_dict(['mela', 'banana', 'mela']))

# Exercise 2

# Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un numero specificato k di posizioni. 
# La rotazione verso sinistra significa che ciascun elemento della lista viene spostato a sinistra di una posizione
# e l'elemento iniziale viene spostato alla fine della lista. Per la rotazione utilizzare lo slicing e gestire il caso
# in cui il numero specificato di posizioni sia maggiore della lunghezza della lista.

def rotate_left(elements: list, k: int) -> list:
    n = len(elements)
    
    k = k % n
    
    rotated_elements = elements[k:] + elements[:k]
    return rotated_elements


print(rotate_left([1, 2, 3, 4, 5], 2))

# Exercise 3

# Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, 
# mantenendo l'ordine originale degli elementi.
	
def remove_duplicates(list: list) -> list:
    unique_elements = []
    for element in list:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements

print(remove_duplicates([1, 2, 3, 1, 2, 4]))

# Exercise 4 

# Il codice dovrebbe stampare i numeri all'interno di una lista.
# TROVA L'ERRORE E CORREGGI IL CODICE

numbers: list[int] = [1, 2, 3, 4, 5]

for i in range(len(numbers)):
    print('Number:', numbers[i])

# Exercise 5

# Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account 
# (attivo/non attivo). L'accesso è consentito solo se il nome utente è "admin", la password corrisponde a "12345" e 
# l'account è attivo. La funzione ritorna "Accesso consentito" oppure "Accesso negato

def check_access(username: str, password: ..., is_active: bool) -> str:
    if username == "admin" and password == "12345" and is_active == True:
        return "Accesso consentito"
    else:
        return "Accesso negato"

print(check_access("admin", "12345", True))

print(check_access("admin", "54321", True))

# Exercise 6

# Scrivi una funzione che, dato un numero intero, determina se è un "numero magico". Un numero magico è 
# definito come un numero che contiene il numero 7.

def is_magic_number(num: int) -> bool:
    number_str = str(num)
    if '7' in number_str:
        return True
    else:
        return False
    
print(is_magic_number(70))

print(is_magic_number(123))

# Exercise 7
# Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, 
# cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.


def check_parentheses(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0

print(check_parentheses("()()"))
print(check_parentheses("(()))("))


    
    



    
    
    


        

   
    

    



   


    


   


    


    