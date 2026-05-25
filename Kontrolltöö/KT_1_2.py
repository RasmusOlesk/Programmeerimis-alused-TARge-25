import random


    def generate_limits():
        """Genereerib juhusliku kasvuvahemiku (min_increase, max_increase)."""
        # Veendume, et max_increase > min_increase
        min_inc = random.randint(1, 5)
        max_inc = random.randint(min_inc + 1, min_inc + 10)
        return min_inc, max_inc


    def get_first_number():
        """Küsib kasutajalt esimese täisarvu."""
        while True:
            value = input("Sisesta esimene täisarv: ").strip()
            if value.lstrip("-").isdigit():
                return int(value)
            print("See ei ole täisarv. Proovi uuesti.")


    def get_next_number(previous, min_inc, max_inc):
        """
        Küsib järgmist arvu.
        Tagastab (is_correct, number).
        """
        value = input(f"Sisesta arv, mis on {min_inc} kuni {max_inc} võrra suurem kui {previous}: ").strip()

        if not value.lstrip("-").isdigit():
            return False, None

        number = int(value)

        # kontrolli kas number on lubatud vahemikus
        if previous + min_inc <= number <= previous + max_inc:
            return True, number

        return False, number


    def print_summary(numbers, mistakes):
        """Prindib kokkuvõtte."""
        print("\n--- PROGRAMMI KOKKUVÕTE ---")
        print(f"Korrektseid sisestusi: {len(numbers)}")
        print(f"Eksimusi kokku: {mistakes}")
        print("Sisestatud arvud:")
        for n in numbers:
            print(" -", n)


    if __name__ == "__main__":
        print("Tere tulemast arvumängu!")
        print("Iga järgmine arv peab olema eelmisest suurem, kuid mitte liiga palju suurem.")
        print("Piirid määratakse juhuslikult iga sammu jaoks.")
        print("Programm lõppeb 3 eksimuse järel või kui järgmine nõutav arv peaks ületama 100.\n")

        mistakes = 0
        numbers = []

        # esimene arv
        current = get_first_number()
        numbers.append(current)

        while mistakes < 3:
            # genereeri uued piirid
            min_inc, max_inc = generate_limits()

            # kontrolli, kas järgmine nõutav arv võib üldse olla <= 100
            if current + min_inc > 100:
                print("\nJärgmine nõutav arv peaks olema üle 100. Programm lõppeb.")
                break

            is_correct, nxt = get_next_number(current, min_inc, max_inc)

            if not is_correct:
                mistakes += 1
                print(f"Viga! Eksimusi: {mistakes}/3")
            else:
                numbers.append(nxt)
                current = nxt

        print_summary(numbers, mistakes)
