keuze = "0"

while keuze != "3":
    print("\n--- MENU ---")
    print("1) BTW berekenen")
    print("2) Temperatuur omrekenen")
    print("3) Stoppen")

    keuze = input("Maak een keuze: ")

    if keuze == "1":
        bedrag = float(input("Bedrag (excl. btw): "))
        btw_percentage = float(input("BTW-percentage: "))
        btw_bedrag = bedrag * btw_percentage / 100
        totaal = bedrag + btw_bedrag
        print(f"Bedrag incl. btw: {totaal:.2f} euro")

    elif keuze == "2":
        fahrenheit = float(input("Temperatuur in °F: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit:.1f} °F = {celsius:.1f} °C")

    elif keuze == "3":
        print("Programma gestopt.")

    else:
        print("Ongeldige keuze.")

