class Media:
    def __init__(self, title=""):
        self.title = title
        self.reviews = []
    
    def set_title(self, title):
        self.title = title
    
    def get_title(self):
        return self.title
    
    def aggiungiValutazione(self, voto):
        if 1 <= voto <= 5:
            self.reviews.append(voto)
        else:
            print("Voto non valido. Inserisci un valore tra 1 e 5.")
    
    def getMedia(self):
        if not self.reviews:
            return 0
        return sum(self.reviews) / len(self.reviews)
    
    def getRate(self):
        media = self.getMedia()
        if media < 1.5:
            return "Terribile"
        elif media < 2.5:
            return "Brutto"
        elif media < 3.5:
            return "Normale"
        elif media < 4.5:
            return "Bello"
        else:
            return "Grandioso"
    
    def ratePercentage(self, voto):
        if not self.reviews:
            return 0.0
        count = self.reviews.count(voto)
        return (count / len(self.reviews)) * 100
    
    def recensione(self):
        print(f"Titolo del Media: {self.get_title()}")
        print(f"Voto Medio: {self.getMedia():.2f}")
        print(f"Giudizio: {self.getRate()}")
        for i in range(1, 6):
            print(f"{self.getRateFromValue(i)}: {self.ratePercentage(i):.2f}%")
    
    def getRateFromValue(self, value):
        if value == 1:
            return "Terribile"
        elif value == 2:
            return "Brutto"
        elif value == 3:
            return "Normale"
        elif value == 4:
            return "Bello"
        elif value == 5:
            return "Grandioso"

class Film(Media):
    def __init__(self, title=""):
        super().__init__(title)


# Creazione di oggetti di tipo Film
film1 = Film("The Shawshank Redemption")
film2 = Film("The Godfather")

# Aggiunta di valutazioni ai film
valutazioni_film1 = [5, 4, 5, 5, 4, 5, 5, 3, 4, 4]
valutazioni_film2 = [5, 5, 4, 5, 4, 3, 5, 5, 5, 5]

for voto in valutazioni_film1:
    film1.aggiungiValutazione(voto)

for voto in valutazioni_film2:
    film2.aggiungiValutazione(voto)

# Richiamo del metodo recensione per entrambi i film
film1.recensione()
print("\n")
film2.recensione()

        
        
        
           
        
         
        
    
     
     
     
     
     
     
     
     
     
     

        
    
    
        
         
     
     
     
     
        
    
    
    

        
        
        
        
        
        
        
        
        
        

    
    
        

        
        
        
        
        
        
        
        
        
        
        
                                                   
        
        
                
        
        

        
                
    