class Documento:
    
    def __init__(self, testo=""):
        
        self.testo = testo
        
    def getText(self):
            
        return self.testo
        
    def setText(self, testo):
        
        self.testo = testo
        
    def isInText(self, keyword):
            
        return keyword in self.testo
    
class Email(Documento):
    
    def __init__(self, testo="", mittente="", destinatario="", titolo=""):
        
        super().__init__(testo)
        
        self.mittente = mittente
        
        self.destinatario = destinatario
        
        self.titolo = titolo
        
    def getMittente(self):
        
      return self.mittente
    
    def setMittente(self, mittente):
        
        self.mittente = mittente
        
    def getDestinatario(self):
        
        return self.destinatario
    
    def setDestinatario(self, destinatario):
        
        self.destinatario = destinatario
        
    def getTitolo(self):
        
        return self.titolo
    
    def setTitolo(self, titolo):
        
        self.titolo = titolo
        
    def getText(self):
        
        return (f"Da: {self.mittente}, A: {self.destinatario}\n" f"Titolo:{self.titolo}\n" f"Messaggio:{self.testo}")
    
    def writeToFile(self, percorso):
        
        with open(percorso, 'w') as file:
            
         file.write(self.getText())   
         
class File(Documento):
    
    def __init__(self, testo="", nomePercorso=""):
        
        super().__init__(testo)
        
        self.nomePercorso = nomePercorso
        
    def getNomePercorso(self):
        
        return self.nomePercorso
    
    def setNomePercorso(self, nomePercorso):
        
        self.nomePercorso = nomePercorso
        
    def leggiTestoDaFile(self):
        
        with open(self.nomePercorso, 'r') as file:
            
         self.testo = file.read()   
         
    def getText(self):
        
        return (f"Percorso:{self.nomePercorso}\n" f"Contenuto: {self.testo}")  
    
    #### CODICE DRIVER ####
    
    email = Email(mittente="Gino@ciao.it", destinatario="Mimmo@ciao.it", titolo="ciao", testo="ciao")
    
    percorso_file = ""
    
    with open(percorso_file, 'w') as file:
        
        file.write("Questo è il contenuto del file")
        
    file_documento = file(nomePercorso=percorso_file)
    
    file_documento = leggiTestoDaFile()
    
    print("Testo dell'email:")
    
    print(email.getText())
    
    print("\n Testo del file:")
    print(file_documento.getText())
    
        
    
    
           
            
                                      
        
                 
        
        
            
            
        
        
        
        
        
    
        
        
    



