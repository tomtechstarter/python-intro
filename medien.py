class Medium():
    def __init__(self, titel, jahr):
        self.titel = titel
        self.jahr = jahr

    def print(self):
        print(f"Hallo {self.titel}")

class Film(Medium):
    def __init__(self, titel, jahr, regisseur):
        super().__init__(titel, jahr)
        self.regisseur = regisseur
        # print("DEBUG: Film erstellt")
        # auch hier könnte jeder erdenkliche Code stehen
    
    def print_anders(self):
        print(f"Tschüss {self.regisseur}")

medium = Medium("Harry Potter", 2001)
film = Film("Frodo", 2391, "Jackie Chan")

# Unterklassen könnten alles was die Oberklasse kann
# Die Oberklasse kann nur was die Oberklasse kann

medium.print()
# medium.print_anders() # ist in Unterklasse definiert und nicht an die Oberklasse vererbt

film.print() # wird von der Oberklasse vererbt, funktioniert also
film.print_anders() 
