telefoniraamat = {}

def lae_failist():
    try:
        with open("telefoniraamat.txt", "r", encoding="utf-8") as f:
            for rida in f:
                rida = rida.strip()
                if ";" in rida:
                    nimi, number = rida.split(";", 1)
                    telefoniraamat[nimi] = number
    except FileNotFoundError:
        pass  # Faili pole veel – alustame tühjalt

def salvesta_faili():
    with open("telefoniraamat.txt", "w", encoding="utf-8") as f:
        for nimi, number in telefoniraamat.items():
            f.write(f"{nimi}, Telefoninumber: {number}\n")

def lisa_kontakt():
    nimi = input("Sisesta nimi: ")
    number = input("Sisesta telefoninumber: ")
    telefoniraamat[nimi] = number
    salvesta_faili()
    print(f"Lisatud: {nimi} – {number}\n")

def otsi_kontakt():
    print("1. Otsi nime järgi")
    print("2. Otsi numbri järgi")
    valik = input("Vali otsingu tüüp: ")
    if valik == "1":
        nimi = input("Sisesta nimi: ")
        if nimi in telefoniraamat:
            print(f"{nimi} number on {telefoniraamat[nimi]}\n")
        else:
            print("Sellist nime ei leitud.")
            lisa = input("Kas soovid selle nime lisada? (jah/ei): ")
            if lisa.lower() == "jah":
                number = input("Sisesta telefoninumber: ")
                telefoniraamat[nimi] = number
                salvesta_faili()
                print(f"Lisatud: {nimi} – {number}\n")
    elif valik == "2":
        number = input("Sisesta telefoninumber: ")
        leitud = False
        for nimi, num in telefoniraamat.items():
            if num == number:
                print(f"Numbrile {number} vastab nimi {nimi}\n")
                leitud = True
                break
        if not leitud:
            print("Sellist numbrit ei leitud.")
            lisa = input("Kas soovid selle numbri lisada? (jah/ei): ")
            if lisa.lower() == "jah":
                nimi = input("Sisesta nimi: ")
                telefoniraamat[nimi] = number
                salvesta_faili()
                print(f"Lisatud: {nimi} – {number}\n")
    else:
        print("Tundmatu valik.\n")

def kuva_koik():
    print("\n--- Kogu telefoniraamat ---")
    if not telefoniraamat:
        print("Telefoniraamat on tühi.\n")
        return
    for nimi, number in telefoniraamat.items():
        print(f"{nimi}: {number}")
    print()


if __name__ == "__main__":
    lae_failist()
    while True:
        print("1. Lisa kontakt")
        print("2. Otsi kontakti")
        print("3. Kuva kogu telefoniraamat")
        print("4. Lõpeta")
        valik = input("Vali tegevus: ")
        if valik == "1":
            lisa_kontakt()
        elif valik == "2":
            otsi_kontakt()
        elif valik == "3":
            kuva_koik()
        elif valik == "4":
            print("Programmi töö lõpetatud.")
            break
        else:
            print("Tundmatu valik.\n")
