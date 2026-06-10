from animals.lion import Lion
from animals.elephant import Elephant
from animals.monkey import Monkey
from zoo.zoo import Zoo


def create_animal():
    """
    Loob uue looma kasutaja sisendi põhjal.

    Funktsioon küsib kasutajalt:
        - looma liigi (Lõvi, Elevant, Ahv)
        - looma nime
        - looma vanuse

    Tagastab:
        Animal: vastava liigi objekt (Lion, Elephant või Monkey).

    Kui kasutaja sisestab tundmatu liigi numbri,
    luuakse vaikimisi Monkey objekt.
    """
    print("\nVali loomaliik:")
    print("1 - Lõvi")
    print("2 - Elevant")
    print("3 - Ahv")

    choice = input("Sisesta number: ")

    name = input("Sisesta looma nimi: ")
    age = int(input("Sisesta looma vanus: "))

    if choice == "1":
        return Lion(name, age)
    elif choice == "2":
        return Elephant(name, age)
    elif choice == "3":
        return Monkey(name, age)
    else:
        print("Tundmatu valik, loon vaikimisi ahvi.")
        return Monkey(name, age)


def load_from_file(zoo):
    """
    Laeb loomad failist 'loomaaed.txt' ja lisab need Zoo objekti.

    Faili iga rida peab olema kujul:
        nimi;liik;vanus;tervis

    Args:
        zoo (Zoo): Zoo objekt, kuhu loomad lisatakse.

    Kui faili pole olemas, alustatakse tühja loomaaedaga.
    """
    try:
        with open("loomaaed.txt", "r", encoding="utf-8") as f:
            for line in f:
                name, species, age, health = line.strip().split(";")
                age = int(age)
                health = int(health)

                # Loome õige looma objekti
                if species == "Lion":
                    animal = Lion(name, age)
                elif species == "Elephant":
                    animal = Elephant(name, age)
                elif species == "Monkey":
                    animal = Monkey(name, age)
                else:
                    continue

                animal.set_health(health)
                zoo.add_animal(animal)

        print("✔ Loomad loetud failist.")
    except FileNotFoundError:
        print("Faili pole veel, alustan tühja loomaaedaga.")


def save_to_file(animal):
    """
    Salvestab ühe looma andmed faili 'loomaaed.txt'.

    Andmed lisatakse faili lõppu (append-režiim), et olemasolevad loomad ei kaoks.

    Args:
        animal (Animal): loom, kelle andmed salvestatakse.

    Faili formaat:
        nimi;liik;vanus;tervis
    """
    with open("loomaaed.txt", "a", encoding="utf-8") as f:
        f.write(f"{animal.name};{animal.__class__.__name__};{animal.age};{animal.get_health()}\n")
    print(f"✔ Loom '{animal.name}' lisatud faili.")


def delete_from_file(zoo):
    """
    Kustutab looma failist ja Zoo objektist.

    Kui mitu looma kannavad sama nime:
        - kasutajale kuvatakse kõik vasted
        - kasutaja valib, millise täpselt kustutada

    Args:
        zoo (Zoo): Zoo objekt, kust loom eemaldatakse.

    Kustutamine toimub nii failist kui ka Zoo.animals listist.
    """
    name = input("Sisesta kustutatava looma nimi: ")

    # Loeme kõik failist
    try:
        with open("loomaaed.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("❗ Faili pole veel loodud.")
        return

    # Otsime kõik sama nimega loomad
    matches = [line for line in lines if line.startswith(name + ";")]

    if not matches:
        print("❗ Sellise nimega looma ei leitud failist.")
        return

    # Kui mitu looma sama nimega → küsi, millise kustutame
    if len(matches) > 1:
        print("\nLeidsin mitu looma sama nimega:")
        for i, line in enumerate(matches, start=1):
            print(f"{i}. {line.strip()}")

        choice = int(input("Vali number, millise kustutad: "))
        to_delete = matches[choice - 1]
    else:
        to_delete = matches[0]

    # Kirjutame faili uuesti ilma valitud loomata
    with open("loomaaed.txt", "w", encoding="utf-8") as f:
        for line in lines:
            if line != to_delete:
                f.write(line)

    print("✔ Loom kustutatud failist.")

    # Kustutame sama looma ka Zoo objektist
    parts = to_delete.strip().split(";")
    del_name = parts[0]
    del_species = parts[1]
    del_age = int(parts[2])

    for a in zoo.animals:
        if a.name == del_name and a.__class__.__name__ == del_species and a.age == del_age:
            zoo.animals.remove(a)
            break

    print("✔ Loom kustutatud ka programmist.")


if __name__ == "__main__":
    """
    Programmi käivitamise plokk.

    Tegevused:
        1. Luua Zoo objekt
        2. Lugeda loomad failist
        3. Kuvada menüü
        4. Lubada kasutajal loomi lisada, kustutada ja kuvada
        5. Lõpetada programm kasutaja käsul
    """
    zoo = Zoo()
    load_from_file(zoo)

    while True:
        print("\n--- MENÜÜ ---")
        print("1 - Lisa loom")
        print("2 - Näita loomaaeda")
        print("3 - Kustuta loom")
        print("4 - Lõpeta")

        choice = input("Vali tegevus: ")

        if choice == "1":
            animal = create_animal()
            zoo.add_animal(animal)
            save_to_file(animal)

        elif choice == "2":
            zoo.show_all()

        elif choice == "3":
            delete_from_file(zoo)

        elif choice == "4":
            print("Programm lõpetatud.")
            break

        else:
            print("Tundmatu valik.")
