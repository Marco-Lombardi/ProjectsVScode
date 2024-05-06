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

	





    
    
    


        

   
    

    



   


    


   


    


    