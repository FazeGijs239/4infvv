tijd=float(input("Hoeveel seconden tel je tussen bliksem en donder? "))

lengte= tijd*343 / 1000

print(f"Het onweer is ongeveer {round(lengte, 1)} km ver.")

if lengte < 3:
    print("Opgelet! Het onweer is dichtbij. Ga snel naar binnen!")