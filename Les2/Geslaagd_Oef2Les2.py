Resultaat = float(input("Hoeveel punten behaalde je:"))
Score = float(input("Wat was het maximaal te behalen score:"))
Procent = Resultaat/Score
print(f"{round(Procent*100, 1)}%")
if Procent < 0.5:
    print("Jammer, niet geslaagd")

if Procent >= 0.5:
    print("Proficiat, geslaagd")