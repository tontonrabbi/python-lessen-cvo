


naam = input("Naam van de klant: ")
aantal_prod = int(input("Aantal producten: "))

if aantal_prod < 0:
    print("FOUT: Het aantal mag niet negatief zijn.")
else:
    prijs_per_stuk = float(input("Prijs per stuk: "))
    btw_bedrag = float(input("BTW-percentage (6, 12 of 21): "))

    
    subtotaal = round(aantal_prod * prijs_per_stuk, 2)
    btw_bedrag1 = round(subtotaal * (btw_bedrag / 100), 2)
    totaalbedrag = round(subtotaal + btw_bedrag, 2)

 
    print("================================")
    print(f"Factuur voor: {naam}")
    print(f"Aantal producten: {aantal_prod}")
    print(f"Prijs per stuk:  € {prijs_per_stuk:.2f}")
    print("--------------------------------")
    print(f"Subtotaal:       € {subtotaal:.2f}")
    print(f"BTW ({btw_bedrag1}%):   € {btw_bedrag:.2f}")
    print(f"TOTAAL:          € {totaalbedrag:.2f}")
    print("================================")

