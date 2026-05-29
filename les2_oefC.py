# 1. Vraag twee gehele getallen
getal1 = int(input("Geef het eerste getal: "))
getal2 = int(input("Geef het tweede getal: "))

# 2. Berekeningen
som = getal1 + getal2
verschil = getal1 - getal2
product = getal1 * getal2
deling = getal1 / getal2

# 3. Resultaten afdrukken
print(f"Som: {som}")
print(f"Verschil: {verschil}")
print(f"Product: {product}")
print(f"Deling: {deling}")

# Vraag een getal aan de gebruiker
getal = int(input("Geef een geheel getal: "))

# 1. Even of oneven via modulo
if getal % 2 == 0:
    print("even")
else:
    print("oneven")

# 2. Kwadraat berekenen
kwadraat = getal ** 2
print(f"Kwadraat: {kwadraat}")
