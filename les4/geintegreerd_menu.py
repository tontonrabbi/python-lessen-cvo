# geintegreerd_menu.py – gemaakt door Rabbi

while True:
    print("\n" + "=" * 45)
    print(" HOOFDMENU ERPM-SYSTEEM PRIMABOUW")
    print("=" * 45)
    print("1) BTW-Calculator (Les 3)")
    print("2) Kortingscalculator (Les 4)")
    print("3) Werf- & Stellingveiligheid (Les 4)")
    print("4) Applicatie afsluiten")
    print("=" * 45)

    keuze = input("Maak uw keuze (1-4): ")

    if keuze == "1":
        print("\n--- [OPSTARTEN BTW-CALCULATOR] ---")
        bedrag = float(input("Bedrag excl. btw: "))
        tarief = float(input("BTW-tarief (%): "))
        btw = bedrag * tarief / 100
        totaal = bedrag + btw
        print(f"Totaal incl. btw: €{totaal:.2f}")

    elif keuze == "2":
        print("\n--- [OPSTARTEN KORTINGSCALCULATOR] ---")
        totaalbedrag = float(input("Orderbedrag (€): "))

        if totaalbedrag >= 2500:
            korting_pct = 15
        elif totaalbedrag >= 1000:
            korting_pct = 10
        elif totaalbedrag >= 500:
            korting_pct = 5
        else:
            korting_pct = 0

        korting = totaalbedrag * (korting_pct / 100)
        eind = totaalbedrag - korting

        print(f"Korting: {korting_pct}% → €{korting:.2f}")
        print(f"Te betalen: €{eind:.2f}")

    elif keuze == "3":
        print("\n--- [OPSTARTEN WERF-VEILIGHEID] ---")
        wind = float(input("Windsnelheid (km/u): "))

        if wind > 60:
            print(" CRITIEK GEVAAR: Stoppen!")
        elif wind > 30:
            netten = input("Zijn de netten gemonteerd? (ja/nee): ")
            if netten.lower() == "ja":
                print("Werken toegestaan, maar voorzichtig.")
            else:
                print("VERBODEN zonder netten!")
        else:
            regen = input("Hevige regen of ijzel? (ja/nee): ")
            if regen.lower() == "ja":
                print("Gladheid! Antislip verplicht.")
            else:
                print("Veilig om te werken.")

        print("\n--- EXTRA CONTROLE TORENKRAAN ---")
        hoogte = float(input("Kraanmast hoogte (m): "))

        if wind > 45 and hoogte > 20:
            print("KRAAN VERBODEN!")
        elif wind > 55 or hoogte > 40:
            print("Alleen gecertificeerde masters!")
        else:
            print("Kraan veilig.")

    elif keuze == "4":
        print("Tot ziens!")
        break

    else:
        print("❌ Ongeldige keuze!")
