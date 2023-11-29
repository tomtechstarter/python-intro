class Auto():
    typ = "PKW"
    def __init__(self, marke, farbe, model):
        self.marke = marke
        self.farbe = farbe
        self.model = model

    def zeige_info(self):
        print(f"Auto Marke: {self.marke}, Farbe: {self.farbe}, Model: {self.model} ")

class Van(Auto):
    typ = "Van"
    def __init__(self, marke, farbe, model, hat_stehoehe):
        super().__init__( marke, farbe, model )
        self.hat_stehoehe = hat_stehoehe

    def zeige_info(self):
        print(f"Van Marke: {self.marke}, Farbe: {self.farbe}, Model: {self.model}, hat stehöhe: {self.hat_stehoehe} ")


myVan= Van("VW", "rot", "T6", False)

myVan.zeige_info()