telefoniraamat = {}

"""Siin Laeb telefoniraamatu andmed failist telefoniraamat.txt"""
def download_from_file():
    try:
        with open("telefoniraamat.txt", "r", encoding="utf-8") as f:
            for row in f:
                row = row.strip()
                if ", Telefoninumber: " in row:
                    name, number = row.split(", Telefoninumber: ", 1)
                    telefoniraamat[name] = number
    except FileNotFoundError:
        pass

"""Salvestab telefoniraamatu sisu faili telefoniraamat.txt"""
def save_file():
    with open("telefoniraamat.txt", "w", encoding="utf-8") as f:
        for name, number in telefoniraamat.items():
            f.write(f"{name}, Telefoninumber: {number}\n")

"""Lisab uue kontakti telefoniraamatusse."""
def lisa_kontakt():
    name = input("Sisesta nimi: ")
    number = input("Sisesta telefoninumber: ")
    telefoniraamat[name] = number
    save_file()
    print(f"Lisatud: {name} – {number}\n")

"""Otsib kontakti kas nime või telefoninumbri järgi"""
def search_contact():
    print("1. Otsi nime järgi")
    print("2. Otsi numbri järgi")
    choice = input("Vali otsingu tüüp: ")
    if choice == "1":
        name = input("Sisesta nimi: ")
        if name in telefoniraamat:
            print(f"{name} number on {telefoniraamat[name]}\n")
        else:
            print("Sellist nime ei leitud.")
            add = input("Kas soovid selle nime lisada? (jah/ei): ")
            if add.lower() == "jah":
                number = input("Sisesta telefoninumber: ")
                telefoniraamat[name] = number
                save_file()
                print(f"Lisatud: {name} – {number}\n")
    elif choice == "2":
        number = input("Sisesta telefoninumber: ")
        found = False
        for name, num in telefoniraamat.items():
            if num == number:
                print(f"Numbrile {number} vastab nimi {name}\n")
                found = True
                break
        if not found:
            print("Sellist numbrit ei leitud.")
            add = input("Kas soovid selle numbri lisada? (jah/ei): ")
            if add.lower() == "jah":
                nimi = input("Sisesta nimi: ")
                telefoniraamat[name] = number
                save_file()
                print(f"Lisatud: {name} – {number}\n")
    else:
        print("Tundmatu valik.\n")

"""Kuvab kogu telefoniraamatu sisu"""
def show_all():
    print("\n--- Kogu telefoniraamat ---")
    if not telefoniraamat:
        print("Telefoniraamat on tühi.\n")
        return
    for name, number in telefoniraamat.items():
        print(f"{name}: {number}")
    print()


if __name__ == "__main__":
    download_from_file()
    while True:
        print("1. Lisa kontakt")
        print("2. Otsi kontakti")
        print("3. Kuva kogu telefoniraamat")
        print("4. Lõpeta")
        choice = input("Vali tegevus: ")
        if choice == "1":
            lisa_kontakt()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            show_all()
        elif choice == "4":
            print("Programmi töö lõpetatud.")
            break
        else:
            print("Tundmatu valik.\n")
