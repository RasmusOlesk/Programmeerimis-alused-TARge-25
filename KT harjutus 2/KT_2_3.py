def has_min_length(password):
    return len(password) >= 8


def has_number(password):
    return any(ch.isdigit() for ch in password)


def has_symbol(password):
    return any(not ch.isalnum() for ch in password)


def check_password(password):
    """Tagastab listi reeglitest, mis EI OLE täidetud."""
    errors = []

    if not has_min_length(password):
        errors.append("Parool peab olema vähemalt 8 tähemärki pikk")

    if not has_number(password):
        errors.append("Parool peab sisaldama vähemalt ühte numbrit")

    if not has_symbol(password):
        errors.append("Parool peab sisaldama vähemalt ühte sümbolit (mitte täht ega number)")

    return errors


def print_summary(attempts, success):
    print("\n--- PROGRAMMI KOKKUVÕTE ---")
    print(f"Kokku proovimisi: {attempts}")
    print("Tulemus:", "Parool edukalt loodud" if success else "Parooli loomine katkestati")


if __name__ == "__main__":
    print("Parooli kontrolli programm")
    print("Reeglid:")
    print(" - Vähemalt 8 tähemärki")
    print(" - Vähemalt üks number")
    print(" - Vähemalt üks sümbol (mitte täht ega number)")
    print("Tühja sisestusega saab programmi katkestada.\n")

    attempts = 0
    success = False

    while True:
        password = input("Sisesta parool: ").strip()
        attempts += 1

        if password == "":
            print("Programm katkestati tühja sisestusega.")
            break

        errors = check_password(password)

        if not errors:
            print("Parool on piisavalt tugev!")
            success = True
            break
        else:
            print("Parool ei vasta nõuetele:")
            for err in errors:
                print(" -", err)
            print()

    print_summary(attempts, success)
