studenten = [
    {'name': 'Max', 'noten': [85, 90, 92]},
    {'name': 'Lisa', 'noten': [88, 87, 90]},
    {'name': 'Kerstin', 'noten': [78, 85, 80]}
]

def durchschnitt_berechnen(noten):
    # Code hier schreiben

# Test
for student in studenten:
    durchschnitt = durchschnitt_berechnen(student['noten'])
    print(f"{student['name']}: Durchschnitt = {durchschnitt}")
