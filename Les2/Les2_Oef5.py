from random import randrange
Getal1 = randrange(10)+1
Getal2 = randrange(10)+1
Quotiënt = float(input(f"Hoeveel is {Getal1} X {Getal2}: "))
Uitkomst = float(Getal1)*float(Getal2)
if Quotiënt == Uitkomst:
    print("Juist, goed zo!")
if Quotiënt != Uitkomst:
    print(f"Fout! Het juiste antwoord is {round(Uitkomst)}.")