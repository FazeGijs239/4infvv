Prijs_zonnepanelen= float(input("Wat is de prijs van je zonnepannelen?:"))
Procent= Prijs_zonnepanelen/100*20
if Procent <= 600:
    print(f"Je krijgt een premie van {Procent} euro.")
if Procent > 600:
    print("Je krijgt een premie van 600 euro.")