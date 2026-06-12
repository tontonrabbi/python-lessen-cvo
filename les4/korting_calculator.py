

# korting_calculator.py – gemaakt door Rabbi

print("=" * 45)
print(" Korting Checker - PrimaBouw BV")
print("=" * 45)

totaalbedrag = float(input("Voer het totale orderbedrag in (€): "))
klant = input("Type klant (Standaard / Zilver / Goud): ").lower()

# --- Volumekorting ---
if totaalbedrag >= 2500:
    korting_pct = 15
elif totaalbedrag >= 1000:
    korting_pct = 10
elif totaalbedrag >= 500:
    korting_pct = 5
else:
    korting_pct = 0

# --- Extra klantkorting ---
if klant == "goud":
    extra = 5
elif klant == "zilver":
    extra = 2
else:
    extra = 0

# Totaal percentage
totaal_korting = korting_pct + extra

# --- Output die jij vroeg ---
print(f"Klanttype: {klant.capitalize()}")
print(f"Extra korting op basis van klanttype: {extra}%")
print(f"Totaal kortingspercentage: {totaal_korting}%")
