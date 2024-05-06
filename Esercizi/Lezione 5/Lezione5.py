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


	





    
    
    


        

   
    

    



   


    


   


    


    