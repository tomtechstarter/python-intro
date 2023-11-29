from auto import Auto

class Van(Auto):
    typ = "Van"
    def __init__(self, marke, farbe, model, hat_stehoehe):
        super().__init__( marke, farbe, model )
        self.hat_stehoehe = hat_stehoehe