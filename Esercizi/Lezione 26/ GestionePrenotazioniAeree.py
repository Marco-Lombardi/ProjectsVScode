from abc import ABC, abstractmethod
import math

# Classe astratta Volo
class Volo(ABC):
    def __init__(self, codice, capacita_massima):
        self.codice = codice
        self.capacita_massima = capacita_massima
        self.prenotazioni = 0

    @abstractmethod
    def prenota_posto(self, posti, classe_servizio=None):
        pass

    @abstractmethod
    def posti_disponibili(self):
        pass

# Classe VoloCommerciale
class VoloCommerciale(Volo):
    def __init__(self, codice, capacita_massima):
        super().__init__(codice, capacita_massima)
        self.posti_economica = math.ceil(capacita_massima * 0.7)
        self.posti_business = math.ceil(capacita_massima * 0.2)
        self.posti_prima = capacita_massima - (self.posti_economica + self.posti_business)
        self.prenotazioni_economica = 0
        self.prenotazioni_business = 0
        self.prenotazioni_prima = 0

    def posti_disponibili(self):
        return {
            'posti disponibili': self.capacita_massima - self.prenotazioni,
            'classe economica': self.posti_economica - self.prenotazioni_economica,
            'classe business': self.posti_business - self.prenotazioni_business,
            'prima classe': self.posti_prima - self.prenotazioni_prima
        }

    def prenota_posto(self, posti, classe_servizio):
        if self.prenotazioni >= self.capacita_massima:
            print(f"Volo {self.codice} al completo!")
            return

        if classe_servizio not in ['economica', 'business', 'prima']:
            print("Classe richiesta non valida!")
            return

        if classe_servizio == 'economica':
            disponibili = self.posti_economica - self.prenotazioni_economica
            if posti <= disponibili:
                self.prenotazioni_economica += posti
                self.prenotazioni += posti
                print(f"{posti} posti prenotati su {self.codice} in classe economica.")
            else:
                print(f"Non è possibile riservare {posti} posti in classe economica. Numero posti disponibili: {disponibili}")

        elif classe_servizio == 'business':
            disponibili = self.posti_business - self.prenotazioni_business
            if posti <= disponibili:
                self.prenotazioni_business += posti
                self.prenotazioni += posti
                print(f"{posti} posti prenotati su {self.codice} in classe business.")
            else:
                print(f"Non è possibile riservare {posti} posti in classe business. Numero posti disponibili: {disponibili}")

        elif classe_servizio == 'prima':
            disponibili = self.posti_prima - self.prenotazioni_prima
            if posti <= disponibili:
                self.prenotazioni_prima += posti
                self.prenotazioni += posti
                print(f"{posti} posti prenotati su {self.codice} in prima classe.")
            else:
                print(f"Non è possibile riservare {posti} posti in prima classe. Numero posti disponibili: {disponibili}")

# Classe VoloCharter
class VoloCharter(Volo):
    def __init__(self, codice, capacita_massima, costo):
        super().__init__(codice, capacita_massima)
        self.costo = costo

    def posti_disponibili(self):
        return self.capacita_massima - self.prenotazioni

    def prenota_posto(self, posti=None, classe_servizio=None):
        if self.prenotazioni == 0:
            self.prenotazioni = self.capacita_massima
            print(f"Volo charter {self.codice} prenotato completamente per €{self.costo}.")
        else:
            print(f"Il volo charter {self.codice} è già prenotato.")

# Classe CompagniaAerea
class CompagniaAerea:
    def __init__(self, nome, prezzo_standard):
        self.nome = nome
        self.prezzo_standard = prezzo_standard
        self.flotta = []

    def aggiungi_volo(self, volo):
        self.flotta.append(volo)

    def rimuovi_volo(self, volo):
        self.flotta.remove(volo)

    def mostra_flotta(self):
        print(f"Ecco la flotta della compagnia aerea {self.nome}:")
        for volo in self.flotta:
            print(f"{volo.codice}")

    def guadagno(self):
        guadagno_totale = 0.0
        for volo in self.flotta:
            if isinstance(volo, VoloCommerciale):
                guadagno_totale += (volo.prenotazioni_economica * self.prezzo_standard)
                guadagno_totale += (volo.prenotazioni_business * self.prezzo_standard * 2)
                guadagno_totale += (volo.prenotazioni_prima * self.prezzo_standard * 3)
        return round(guadagno_totale, 2)

# Codice driver
def main():
    # Creazione di un volo commerciale
    volo_commerciale = VoloCommerciale("COM123", 100)
    print(f"Posti disponibili sul volo commerciale {volo_commerciale.codice}:")
    print(volo_commerciale.posti_disponibili())
    volo_commerciale.prenota_posto(70, 'economica')
    print(volo_commerciale.posti_disponibili())
    volo_commerciale.prenota_posto(20, 'business')
    print(volo_commerciale.posti_disponibili())
    volo_commerciale.prenota_posto(70, 'prima')
    print(volo_commerciale.posti_disponibili())
    volo_commerciale.prenota_posto(10, 'prima')
    print(volo_commerciale.posti_disponibili())
    volo_commerciale.prenota_posto(1, 'economica')
    print(volo_commerciale.posti_disponibili())

    # Creazione di un volo charter
    volo_charter = VoloCharter("CHA456", 200, 20000.0)
    print(f"Posti disponibili sul volo charter {volo_charter.codice}: {volo_charter.posti_disponibili()}")
    volo_charter.prenota_posto()
    volo_charter.prenota_posto()

    # Creazione di un altro volo commerciale
    volo_commerciale2 = VoloCommerciale("COM456", 100)
    volo_commerciale2.prenota_posto(100, 'economica')

    # Creazione di una compagnia aerea
    compagnia = CompagniaAerea("ITA", 100.0)
    compagnia.aggiungi_volo(volo_commerciale)
    compagnia.aggiungi_volo(volo_commerciale2)
    compagnia.mostra_flotta()
    print(f"Dalla vendita dei biglietti aerei, la compagnia aerea {compagnia.nome} ha guadagnato {compagnia.guadagno()} euro")

    # Scrivere l'output su file
    with open("report.txt", "w") as f:
        f.write(f"Posti disponibili sul volo commerciale {volo_commerciale.codice}:\n")
        f.write(str(volo_commerciale.posti_disponibili()) + "\n")
        f.write(f"70 posti prenotati su {volo_commerciale.codice} in classe economica.\n")
        f.write(str(volo_commerciale.posti_disponibili()) + "\n")
        f.write(f"20 posti prenotati su {volo_commerciale.codice} in classe business.\n")
        f.write(str(volo_commerciale.posti_disponibili()) + "\n")
        f.write(f"Non è possibile riservare 70 posti in prima classe. Numero posti disponibili: 10\n")
        f.write(str(volo_commerciale.posti_disponibili()) + "\n")
        f.write(f"10 posti prenotati su {volo_commerciale.codice} in prima classe.\n")
        f.write(str(volo_commerciale.posti_disponibili()) + "\n")
        f.write(f"Volo {volo_commerciale.codice} al completo!\n")
        f.write(f"Posti disponibili sul volo charter {volo_charter.codice}: {volo_charter.posti_disponibili()}\n")
        f.write(f"Volo charter {volo_charter.codice} prenotato completamente per €20000.\n")
        f.write(f"Il volo charter {volo_charter.codice} è già prenotato.\n")
        f.write(f"100 posti prenotati su {volo_commerciale2.codice} in classe economica.\n")
        f.write(f"Ecco la flotta della compagnia aerea {compagnia.nome}:\n")
        for volo in compagnia.flotta:
            f.write(f"volo commerciale {volo.codice}\n")
        f.write(f"Dalla vendita dei biglietti aerei, la compagnia aerea {compagnia.nome} ha guadagnato {compagnia.guadagno()} euro\n")

if __name__ == "__main__":
    main()