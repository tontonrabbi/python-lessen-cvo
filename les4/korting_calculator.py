# korting_calculator.py – gemaakt door [PWEMA]
print("=" * 45)
print(" Korting Checker - PrimaBouw BV")
print("=" * 45)
totaalbedrag = float(input("Voer het totale orderbedrag in (€): "))
# Testen van de basisvoorwaarde
if totaalbedrag > 1000:
    print("Hoera! Deze klant heeft recht op een volumekorting.")
else:
    print("Status: Standaard tarief van toepassing (geen korting).")


if totaalbedrag >= 2500:
    korting_pct = 15
elif totaalbedrag >= 1000:
    korting_pct = 10
elif totaalbedrag >= 500:
    korting_pct = 5
else:
    korting_pct = 0

# Berekeningen

kortingsbedrag = totaalbedrag * (korting_pct / 100)
eindbedrag = totaalbedrag - kortingsbedrag
print("-" * 45)
print(f"Bruto orderbedrag : €{totaalbedrag:.2f}")
print(f"Kortingspercentage: {korting_pct}%")
print(f"Kortingsbedrag : €{kortingsbedrag:.2f}")
print(f"Netto te betalen : €{eindbedrag:.2f}")
print("=" * 45)
