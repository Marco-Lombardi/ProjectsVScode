from abc import ABC, abstractclassmethod

class CodificatoreMessaggio(ABC):
    @abstractclassmethod
    def codfica(self, testoInChiaro):
        pass
class DecodificatoreMessaggio(ABC):
    @abstractclassmethod
    def decodifica(self, testoCodificato):
        pass
    
class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, chiave):
        self.chiave = chiave
        
    def codifica(self, TestoInChiaro):
        
        return ''.join(self._sposta_carattere(c, self.chiave) for c in TestoInChiaro)
    
    def decodifica(self, TestoCodficato):
        
        return ''.join(self._sposta_carattere(c, -self.chiave) for c in TestoCodficato)
    
    def _sposta_carattere(self, c, chiave):
        
        if c.isalpha():
            
            base = ord('a') if c.islower() else ord('A')
            return chr((ord(c) - base + chiave) % 26 + base)
        else:
            return c
class CifratoreACombinazione(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, n):
        self.n = n
        
    def codifica(self, TestoInChiaro):
        risultato = TestoInChiaro
        for _ in range(self.n):
            risultato = self._combinazioni(risultato)
            return risultato
    def decodifica(self, TestoCodificato):
        risultato = TestoCodificato 
        for _ in range(self.n):
            risultato = self._decodifica_combinazioni(risultato)
            return risultato
    def _combinazione(self, testo):
        metà = (len(testo) + 1) // 2
        prima_metà = testo[:metà]    
        seconda_metà = testo[metà:]
        combinato = []
        
        for i in  range (len(seconda_metà)):
            combinato.append(prima_metà[i])
            combinato.append(seconda_metà[i])
            
            if len(prima_metà) > len(seconda_metà):
                combinato.append(prima_metà[i])
                
                return ''.join(combinato)
            
    def _decodifica_combinazione(self, testo):
        metà = len(testo + 1) // 2
        prima_metà = testo[:metà]
        seconda_metà = testo[metà:]
        decodificato = []
        
        i, j = 0, 0 
        while j < len(seconda_metà):
            decodificato.append(prima_metà[i])
            decodificato.append(seconda_metà[j])
            
            i += 1
            j += 1
            
            if i < len(prima_metà):
                decodificato.append(prima_metà[i]) 
                
                return ''.join(decodificato)
            
                      
                    
        
             
            
       







