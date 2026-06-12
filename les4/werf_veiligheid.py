# werf_veiligheid.py – gemaakt door Kris Dierickx
print("=" * 45)
print("     Veiligheids-Assistent PrimaBouw BV")
print("=" * 45)

wind_kmh = float(input("Wat is de actuele windsnelheid op de werf (km/u)? "))
if wind_kmh > 60:
    print("10RITIEK GEVAAR: Stoppen met alle werkzaamheden! Evacueer de stellingen.")
elif wind_kmh > 30:
    # Genest niveau 1: De wind is matig tot krachtig. Status hangt af van veiligheidsnetten.
    netten = input("Zijn de verplichte veiligheidsnetten gemonteerd? (ja/nee): ")  
    if netten.lower() == "ja":
        print("WAARSCHUWING: Werken toegestaan, maar wees alert op rukwinden.")
    else:
        print("GEVAAR: Werken op hoogte VERBODEN zonder gemonteerde netten!")
else:
    # Genest niveau 2: Veilige wind, maar hoe zit het met neerslag?
    regen = input("Is er sprake van hevige regen of ijzel? (ja/nee): ")
    
    if regen.lower() == "ja":
        print("WAARSCHUWING: Risico op gladheid. Werken toegestaan met antislip-schoeisel.")
    else:
        print("VEILIG: Normale werkomstandigheden op de stellingen.")
