def get_first_word():
    """Küsib kasutajalt esimese sõna."""
    return input("Sisesta esimene sõna: ").strip()


def get_next_word(previous):
    """Küsib järgmise sõna ja kontrollib, kas see algab õige tähega.
       Tagastab (is_correct, word)."""
    word = input("Sisesta järgmine sõna: ").strip()

    if word == "":
        return False, word

    if word[0].lower() != previous[-1].lower():
        return False, word

    return True, word


def print_summary(words):
    """Kuvab mängu kokkuvõtte."""
    print("\n--- MÄNG LÄBI ---")
    print(f"Sisestasid {len(words)} korrektset sõna.")
    print("Sõnad:")
    for w in words:
        print(" -", w)


if __name__ == "__main__":
    print("Tere tulemast sõnamängu!")
    print("Sisesta sõnu nii, et iga järgmine sõna algab eelmise sõna viimase tähega.")
    print("Lubatud on 3 eksimust. Tühi sisestus loetakse eksimuseks.\n")

    mistakes = 0
    words = []

    # esimene sõna
    previous = get_first_word()

    if previous == "":
        print("Tühi sisestus – mäng lõppes kohe.")
    else:
        words.append(previous)

        # järgmised sõnad
        while mistakes < 3:
            is_correct, current = get_next_word(previous)

            if not is_correct:
                mistakes += 1
                print(f"Viga! Eksimusi kokku: {mistakes}/3")
            else:
                words.append(current)
                previous = current

        print_summary(words)
