class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore
        self.disponibile = True

    def __str__(self):
        stato = 'Disponibile' if self.disponibile else 'Non disponibile'
        return f"Titolo: {self.titolo}, Autore: {self.autore}, Stato: {stato}"

class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def aggiungi_libro(self, libro):
        self.catalogo.append(libro)
        return f"Libro '{libro.titolo}' aggiunto al catalogo."

    def presta_libro(self, titolo):
        for libro in self.catalogo:
            if libro.titolo == titolo:
                if libro.disponibile:
                    libro.disponibile = False
                    return f"Libro '{titolo}' prestato con successo."
                else:
                    return f"Libro '{titolo}' non disponibile per il prestito."
        return f"Libro '{titolo}' non trovato nel catalogo."

    def restituisci_libro(self, titolo):
        for libro in self.catalogo:
            if libro.titolo == titolo:
                if not libro.disponibile:
                    libro.disponibile = True
                    return f"Libro '{titolo}' restituito con successo."
                else:
                    return f"Libro '{titolo}' non era stato prestato."
        return f"Libro '{titolo}' non trovato nel catalogo."

    def mostra_libri_disponibili(self):
        libri_disponibili = [libro.titolo for libro in self.catalogo if libro.disponibile]
        if libri_disponibili:
            return "Libri disponibili per il prestito:\n" + "\n".join(libri_disponibili)
        else:
            return "Nessun libro disponibile per il prestito."

# Test Cases
biblioteca = Biblioteca()

# Aggiunta di libri al catalogo
print(biblioteca.aggiungi_libro(Libro("Il Signore degli Anelli", "J.R.R. Tolkien")))
print(biblioteca.aggiungi_libro(Libro("1984", "George Orwell")))
print(biblioteca.aggiungi_libro(Libro("To Kill a Mockingbird", "Harper Lee")))

# Prestito di un libro
print(biblioteca.presta_libro("1984"))

# Visualizzare i libri disponibili
print(biblioteca.mostra_libri_disponibili())

# Restituzione di un libro
print(biblioteca.restituisci_libro("1984"))

# Visualizzare i libri disponibili dopo la restituzione
print(biblioteca.mostra_libri_disponibili())

###############################

class MovieCatalog:
    def __init__(self):
        self.catalog = {}

    def add_movie(self, director_name, movies):
        """Aggiunge uno o più film a un regista specifico nel catalogo."""
        if director_name in self.catalog:
            self.catalog[director_name].update(movies)
        else:
            self.catalog[director_name] = set(movies)

    def remove_movie(self, director_name, movie_name):
        """Rimuove un film specifico dall'elenco dei film di un regista."""
        if director_name in self.catalog:
            if movie_name in self.catalog[director_name]:
                self.catalog[director_name].remove(movie_name)
                if not self.catalog[director_name]:
                    del self.catalog[director_name]
                return True
        return False

    def list_directors(self):
        """Elenca tutti i registi presenti nel catalogo."""
        return list(self.catalog.keys())

    def get_movies_by_director(self, director_name):
        """Restituisce tutti i film di un regista specifico."""
        return list(self.catalog.get(director_name, []))

    def search_movies_by_title(self, title):
        """Trova tutti i film che contengono una certa parola nel titolo."""
        result = {}
        for director, movies in self.catalog.items():
            matching_movies = [movie for movie in movies if title.lower() in movie.lower()]
            if matching_movies:
                result[director] = matching_movies
        return result if result else "Nessun film trovato con la parola cercata nel titolo."

# Esempio di utilizzo
catalog = MovieCatalog()
catalog.add_movie("Quentin Tarantino", ["Pulp Fiction", "Kill Bill", "Django Unchained"])
catalog.add_movie("Christopher Nolan", ["Inception", "Dunkirk", "Tenet"])

# Aggiungere un altro film a Quentin Tarantino
catalog.add_movie("Quentin Tarantino", ["Reservoir Dogs"])

# Rimuovere un film da Christopher Nolan
catalog.remove_movie("Christopher Nolan", "Dunkirk")

# Elencare tutti i registi
print("Registi nel catalogo:", catalog.list_directors())

# Ottenere i film di un regista specifico
print("Film di Quentin Tarantino:", catalog.get_movies_by_director("Quentin Tarantino"))

# Cercare film per titolo
print("Film che contengono 'Bill':", catalog.search_movies_by_title("Bill"))
