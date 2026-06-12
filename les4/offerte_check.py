# offerte_check.py – gemaakt door Rabbi

print("=" * 45)
print(" Offerte Evaluatie Systeem - PrimaBouw BV")
print("=" * 45)

# --- Inputvalidatie winst ---
winst_input = input("Geschatte winst (€): ")
if winst_input.replace('.', '', 1).isdigit():
    winst = float(winst_input)
else:
    print("Ongeldige invoer! Winst wordt 0.")
    winst = 0

# --- Inputvalidatie personeel ---
pers_input = input("Beschikbaar personeel (aantal): ")
if pers_input.isdigit():
    personeel = int(pers_input)
else:
    print("Ongeldige invoer! Personeel wordt 0.")
    personeel = 0

# --- Risicofactor ---
risico = input("Risicofactor (Laag / Medium / Hoog): ").lower()

print("\n--- RESULTAAT PROJECTBEOORDELING ---")

# --- Beslissingsboom ---
if personeel < 3:
    print("PROJECTSTATUS: On hold (te weinig personeel)")
elif risico == "hoog" and winst < 20000:
    print("PROJECTSTATUS: Geweigerd (hoog risico + lage winst)")
else:
    print("PROJECTSTATUS: Goedgekeurd")

print("=" * 45)
