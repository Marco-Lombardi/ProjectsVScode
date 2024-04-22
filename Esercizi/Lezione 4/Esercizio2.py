#first Exercise
def word_count(s: str) -> dict[str, int]:
    # Converte la stringa in minuscolo per evitare differenze tra maiuscole e minuscole
    s = s.lower()
    
    # Rimuove i segni di punteggiatura dalla stringa
    for punctuation in '.,!?;:"':
        s = s.replace(punctuation, '')
    
    # Dividi la stringa in parole
    words = s.split()
    
    # Conta le occorrenze di ogni parola
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

# Stringa di esempio
s = "La meccanica quantistica è la teoria fisica che descrive il comportamento della materia, della radiazione e le reciproche interazioni, con particolare riguardo ai fenomeni caratteristici della scala di lunghezza o di energia atomica e subatomica, dove le precedenti teorie classiche risultano inadeguate. Come caratteristica fondamentale, la meccanica quantistica descrive la radiazione e la materia sia come fenomeni ondulatori che come entità particellari, al contrario della meccanica classica, che descrive la luce solamente come un'onda e, ad esempio, l'elettrone solo come una particella. Questa inaspettata e controintuitiva proprietà della realtà fisica, chiamata dualismo onda-particella, è la principale ragione del fallimento delle teorie sviluppate fino al XIX secolo nella descrizione degli atomi e delle molecole. La relazione tra natura ondulatoria e corpuscolare è enunciata nel principio di complementarità e formalizzata nel principio di indeterminazione di Heisenberg. Esistono numerosi formalismi ma"
result = word_count(s)
print(result)

#Second exercise

def word_count(s: str) -> dict[str, int]:
    # Converte la stringa in minuscolo per evitare differenze tra maiuscole e minuscole
    s = s.lower()
    
    # Rimuove i segni di punteggiatura dalla stringa
    for punctuation in '.,!?;:"':
        s = s.replace(punctuation, '')
    
    # Dividi la stringa in parole
    words = s.split()
    
    # Conta le occorrenze di ogni parola
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # Filtra le parole che appaiono più di una volta
    repeated_words = {word: count for word, count in word_count.items() if count > 1}
    
    return repeated_words

# Stringa di esempio
s = "La meccanica quantistica è la teoria fisica che descrive il comportamento della materia, della radiazione e le reciproche interazioni, con particolare riguardo ai fenomeni caratteristici della scala di lunghezza o di energia atomica e subatomica, dove le precedenti teorie classiche risultano inadeguate. Come caratteristica fondamentale, la meccanica quantistica descrive la radiazione e la materia sia come fenomeni ondulatori che come entità particellari, al contrario della meccanica classica, che descrive la luce solamente come un'onda e, ad esempio, l'elettrone solo come una particella. Questa inaspettata e controintuitiva proprietà della realtà fisica, chiamata dualismo onda-particella, è la principale ragione del fallimento delle teorie sviluppate fino al XIX secolo nella descrizione degli atomi e delle molecole. La relazione tra natura ondulatoria e corpuscolare è enunciata nel principio di complementarità e formalizzata nel principio di indeterminazione di Heisenberg. Esistono numerosi formalismi ma"
result = word_count(s)
print(result)

        






   



