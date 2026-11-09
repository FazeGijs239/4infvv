from random import randrange
Geheim = randrange(10)+1
Geraden = float(input("Raad een getal van 1 tot en met 10: "))
if Geheim == Geraden:
    print("Gewonnen! Het getal was" + "str(Geheim getal)"+".")
if Geheim != Geraden:
    print("Helaas! Het getal was {Geheim}.")