
class Tier(): 

    def __init__(self, m_herkunft, m_durchschnittsalter, m_name, m_hauptnahrung, m_ist_bedroht, m_ist_vegetarisch):
        self.herkunft = m_herkunft
        self.durchschnittsalter = m_durchschnittsalter
        self.name = m_name
        self.hauptnahrung = m_hauptnahrung
        self.ist_bedroht = m_ist_bedroht
        self.ist_vegetarisch = m_ist_vegetarisch

    def zeigeInfo(self): 
        print(f"Meine Info sind {self.herkunft}")
       

mein_tier= Tier("Deutschland",10,"Schäferhund", "Hundefutter",False,False)
mein_tier.zeigeInfo()
        
