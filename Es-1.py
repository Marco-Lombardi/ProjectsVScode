class Film:
    def __init__(self, titolo, durata):
        self.titolo = titolo
        self.durata = durata

    def __str__(self):
        return f"{self.titolo} ({self.durata} min)"


class Sala:
    def __init__(self, numero, film, posti_totali):
        self.numero = numero
        self.film = film
        self.posti_totali = posti_totali
        self.posti_prenotati = 0

    def prenota_posti(self, num_posti):
        if num_posti <= 0:
            return "Numero di posti non valido."
        
        posti_disponibili = self.posti_disponibili()
        if num_posti <= posti_disponibili:
            self.posti_prenotati += num_posti
            return f"{num_posti} posti prenotati con successo per '{self.film.titolo}' in sala {self.numero}."
        else:
            return f"Prenotazione fallita. Solo {posti_disponibili} posti disponibili."

    def posti_disponibili(self):
        return self.posti_totali - self.posti_prenotati

    def __str__(self):
        return f"Sala {self.numero}: {self.film}, Posti totali: {self.posti_totali}, Posti prenotati: {self.posti_prenotati}"


class Cinema:
    def __init__(self):
        self.sale = []

    def aggiungi_sala(self, sala):
        self.sale.append(sala)

    def prenota_film(self, titolo_film, num_posti):
        for sala in self.sale:
            if sala.film.titolo == titolo_film:
                return sala.prenota_posti(num_posti)
        return f"Film '{titolo_film}' non trovato."

    def mostra_sale(self):
        return "\n".join(str(sala) for sala in self.sale)


# Esempio di utilizzo del sistema di prenotazione cinema

# Creazione dei film
film1 = Film("Interstellar", 169)
film2 = Film("Inception", 148)

# Creazione delle sale
sala1 = Sala(1, film1, 100)
sala2 = Sala(2, film2, 80)

# Creazione del cinema e aggiunta delle sale
cinema = Cinema()
cinema.aggiungi_sala(sala1)
cinema.aggiungi_sala(sala2)

# Mostra le sale disponibili
print(cinema.mostra_sale())

# Prenotazione posti
print(cinema.prenota_film("Interstellar", 10))
print(cinema.prenota_film("Inception", 5))
print(cinema.prenota_film("Interstellar", 95))  # Questo dovrebbe fallire

# Mostra le sale dopo le prenotazioni
print(cinema.mostra_sale())

######################

#Gestione Magazzino

class Prodotto:
    def __init__(self, nome, quantità):
        self.nome = nome
        self.quantità = quantità

    def __repr__(self):
        return f"Prodotto(nome='{self.nome}', quantità={self.quantità})"

class Magazzino:
    def __init__(self):
        self.prodotti = []

    def aggiungi_prodotto(self, prodotto):
        # Controlla se il prodotto esiste già nel magazzino
        for p in self.prodotti:
            if p.nome == prodotto.nome:
                p.quantità += prodotto.quantità
                return
        self.prodotti.append(prodotto)

    def cerca_prodotto(self, nome):
        for prodotto in self.prodotti:
            if prodotto.nome == nome:
                return prodotto
        return None

    def verifica_disponibilità(self, nome):
        prodotto = self.cerca_prodotto(nome)
        if prodotto:
            return f"Prodotto {nome} disponibile in quantità: {prodotto.quantità}"
        else:
            return f"Prodotto {nome} non disponibile in magazzino."

# Test del sistema di gestione del magazzino

# Creazione del magazzino
magazzino = Magazzino()

# Creazione dei prodotti
prodotto1 = Prodotto("Mela", 50)
prodotto2 = Prodotto("Arancia", 30)
prodotto3 = Prodotto("Banana", 20)

# Aggiunta dei prodotti al magazzino
magazzino.aggiungi_prodotto(prodotto1)
magazzino.aggiungi_prodotto(prodotto2)
magazzino.aggiungi_prodotto(prodotto3)

# Stampa dello stato del magazzino
print(magazzino.prodotti)

# Ricerca di un prodotto
print(magazzino.cerca_prodotto("Arancia"))

# Verifica della disponibilità di un prodotto
print(magazzino.verifica_disponibilità("Banana"))
print(magazzino.verifica_disponibilità("Pera"))
