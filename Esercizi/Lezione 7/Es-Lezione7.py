def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int, int]) -> list[int]:
    for elemento, quantita in da_rimuovere.items():
        count = 0
        while elemento in lista and count < quantita:
            lista.remove(elemento)
            count += 1
    return lista

print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))
	






    
    

    


    
    

    
    