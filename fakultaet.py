# Input
zahl=int(input("Gib eine Zahl ein:")) 

# Funktionen
def berechne_fakultaet(n):
    if n == 0 | n == 1:
        print(f"Abbruchbedingung erreicht")
        return 1
    else:
        print(f"Meine aktuell Zahl ist {n}")
        res= n * berechne_fakultaet(n-1)
        return res
    
# Test 
result=berechne_fakultaet(zahl)  
print(f"Die Fakultät von {zahl} lautet: {result}")