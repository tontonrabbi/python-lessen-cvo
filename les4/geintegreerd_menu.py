

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

    # --- INPUTVALIDATIE MENU ---
    if not keuze.isdigit():
        print(" Ongeldige invoer! Gebruik alleen cijfers.")
        continue

    # Zet om naar int
    keuze = int(keuze)

    # --- OPTIE 1: BTW-CALCULATOR ---
    if keuze == 1:
        print("\n--- [OPSTARTEN BTW-CALCULATOR] ---")

        bedrag_input = input("Bedrag excl. btw: ")
        if bedrag_input.replace('.', '', 1).isdigit():
            bedrag = float(bedrag_input)
        else:
            print("Ongeldige invoer! Bedrag wordt 0.")
            bedrag = 0

        tarief_input = input("BTW-tarief (%): ")
        if tarief_input.replace('.', '', 1).isdigit():
            tarief = float(tarief_input)
        else:
            print("Ongeldige invoer! Tarief wordt 0%.")
            tarief = 0

        btw = bedrag * tarief / 100
        totaal = bedrag + btw
        print(f"Totaal incl. btw: €{totaal:.2f}")

    # --- OPTIE 2: KORTINGSCALCULATOR ---
    elif keuze == 2:
        print("\n--- [OPSTARTEN KORTINGSCALCULATOR] ---")

        bedrag_input = input("Orderbedrag (€): ")
        if bedrag_input.replace('.', '', 1).isdigit():
            totaalbedrag = float(bedrag_input)
        else:
            print("Ongeldige invoer! Orderbedrag wordt 0.")
            totaalbedrag = 0

        klant = input("Type klant (Standaard / Zilver / Goud): ").lower()

        # Volumekorting
        if totaalbedrag >= 2500:
            korting_pct = 15
        elif totaalbedrag >= 1000:
            korting_pct = 10
        elif totaalbedrag >= 500:
            korting_pct = 5
        else:
            korting_pct = 0

        # Extra klantkorting
        if klant == "goud":
            extra = 5
        elif klant == "zilver":
            extra = 2
        else:
            extra = 0

        totaal_korting = korting_pct + extra
        korting = totaalbedrag * (totaal_korting / 100)
        eind = totaalbedrag - korting

        print(f"Klanttype: {klant.capitalize()}")
        print(f"Extra korting: {extra}%")
        print(f"Totaal kortingspercentage: {totaal_korting}%")
        print(f"Te betalen: €{eind:.2f}")

    # --- OPTIE 3: WERFVEILIGHEID ---
    elif keuze == 3:
        print("\n--- [OPSTARTEN WERF-VEILIGHEID] ---")

        wind_input = input("Windsnelheid (km/u): ")
        if wind_input.replace('.', '', 1).isdigit():
            wind = float(wind_input)
        else:
            print("Ongeldige invoer! Windsnelheid wordt 0.")
            wind = 0

        if wind > 60:
            print("CRITIEK GEVAAR: Stoppen!")
        elif wind > 30:
            netten = input("Zijn de netten gemonteerd? (ja/nee): ")
            if netten.lower() == "ja":
                print("Werken toegestaan, maar voorzichtig.")
            else:
                print("VERBODEN zonder netten!")
        else:
            regen = input("Hevige regen of ijzel? (ja/nee): ")
            if regen.lower() == "ja":
                print("ladheid! Antislip verplicht.")
            else:
                print("Veilig om te werken.")

        print("\n--- EXTRA CONTROLE TORENKRAAN ---")
        hoogte_input = input("Kraanmast hoogte (m): ")
        if hoogte_input.replace('.', '', 1).isdigit():
            hoogte = float(hoogte_input)
        else:
            print("Ongeldige invoer! Hoogte wordt 0.")
            hoogte = 0

        if wind > 45 and hoogte > 20:
            print("KRAAN VERBODEN!")
        elif wind > 55 or hoogte > 40:
            print("Alleen gecertificeerde masters!")
        else:
            print("Kraan veilig.")

    # --- OPTIE 4: AFSLUITEN ---
    elif keuze == 4:
        print("Bedankt voor het gebruiken van het PrimaBouw systeem. Tot ziens!")
        break

    # --- FOUTIEVE KEUZE ---
    else:
        print("Ongeldige keuze! Kies 1 t/m 4.")
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

    # --- INPUTVALIDATIE MENU ---
    if not keuze.isdigit():
        print("Ongeldige invoer! Gebruik alleen cijfers.")
        continue

    # Zet om naar int
    keuze = int(keuze)

    # --- OPTIE 1: BTW-CALCULATOR ---
    if keuze == 1:
        print("\n--- [OPSTARTEN BTW-CALCULATOR] ---")

        bedrag_input = input("Bedrag excl. btw: ")
        if bedrag_input.replace('.', '', 1).isdigit():
            bedrag = float(bedrag_input)
        else:
            print("Ongeldige invoer! Bedrag wordt 0.")
            bedrag = 0

        tarief_input = input("BTW-tarief (%): ")
        if tarief_input.replace('.', '', 1).isdigit():
            tarief = float(tarief_input)
        else:
            print("Ongeldige invoer! Tarief wordt 0%.")
            tarief = 0

        btw = bedrag * tarief / 100
        totaal = bedrag + btw
        print(f"Totaal incl. btw: €{totaal:.2f}")

    # --- OPTIE 2: KORTINGSCALCULATOR ---
    elif keuze == 2:
        print("\n--- [OPSTARTEN KORTINGSCALCULATOR] ---")

        bedrag_input = input("Orderbedrag (€): ")
        if bedrag_input.replace('.', '', 1).isdigit():
            totaalbedrag = float(bedrag_input)
        else:
            print("Ongeldige invoer! Orderbedrag wordt 0.")
            totaalbedrag = 0

        klant = input("Type klant (Standaard / Zilver / Goud): ").lower()

        # Volumekorting
        if totaalbedrag >= 2500:
            korting_pct = 15
        elif totaalbedrag >= 1000:
            korting_pct = 10
        elif totaalbedrag >= 500:
            korting_pct = 5
        else:
            korting_pct = 0

        # Extra klantkorting
        if klant == "goud":
            extra = 5
        elif klant == "zilver":
            extra = 2
        else:
            extra = 0

        totaal_korting = korting_pct + extra
        korting = totaalbedrag * (totaal_korting / 100)
        eind = totaalbedrag - korting

        print(f"Klanttype: {klant.capitalize()}")
        print(f"Extra korting: {extra}%")
        print(f"Totaal kortingspercentage: {totaal_korting}%")
        print(f"Te betalen: €{eind:.2f}")

    # --- OPTIE 3: WERFVEILIGHEID ---
    elif keuze == 3:
        print("\n--- [OPSTARTEN WERF-VEILIGHEID] ---")

        wind_input = input("Windsnelheid (km/u): ")
        if wind_input.replace('.', '', 1).isdigit():
            wind = float(wind_input)
        else:
            print("Ongeldige invoer! Windsnelheid wordt 0.")
            wind = 0

        if wind > 60:
            print("CRITIEK GEVAAR: Stoppen!")
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
        hoogte_input = input("Kraanmast hoogte (m): ")
        if hoogte_input.replace('.', '', 1).isdigit():
            hoogte = float(hoogte_input)
        else:
            print("Ongeldige invoer! Hoogte wordt 0.")
            hoogte = 0

        if wind > 45 and hoogte > 20:
            print("KRAAN VERBODEN!")
        elif wind > 55 or hoogte > 40:
            print("Alleen gecertificeerde masters!")
        else:
            print("Kraan veilig.")

    # --- OPTIE 4: AFSLUITEN ---
    elif keuze == 4:
        print("Bedankt voor het gebruiken van het PrimaBouw systeem. Tot ziens!")
        break

    # --- FOUTIEVE KEUZE ---
    else:
        print("Ongeldige keuze! Kies 1 t/m 4.")
