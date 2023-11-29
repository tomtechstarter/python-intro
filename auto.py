class Auto():
    typ = "PKW"

    def __init__(self, marke, farbe, model):
        self.marke = marke
        self.farbe = farbe
        self.model = model

    def zeige_info(self):
        print(f"Auto Marke: {self.marke} , Farbe: {self.farbe}, Model: {self.model} ")


my_auto= Auto("Audi", "rot", "80")
my_auto_zwei = Auto("Audi", "schwarz", "RS6")
my_auto.typ
my_auto.zeige_info()





